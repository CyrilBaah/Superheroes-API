import time
from typing import Optional

from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse, HttpRequest, HttpResponse


class SimpleRateLimitMiddleware:
    """Simple in-memory rate limiting middleware using Django's LocMemCache.

    Configuration (optional) via Django settings:
      RATE_LIMIT_REQUESTS = int (default: 100)
      RATE_LIMIT_WINDOW = int seconds (default: 60)

    Notes:
    - Uses request.user.id when authenticated, otherwise falls back to REMOTE_ADDR.
    - LocMemCache is not shared between processes; in multi-worker deployments
      each worker will have its own counters.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = getattr(settings, "RATE_LIMIT_REQUESTS", 100)
        self.time_window = getattr(settings, "RATE_LIMIT_WINDOW", 60)
        # path prefixes where rate limiting should apply (e.g. API endpoints)
        self.path_prefixes = getattr(settings, "RATE_LIMIT_PATH_PREFIXES", ["/api/", "/health/"])

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # Only apply rate limiting to configured path prefixes
        try:
            path = request.path or request.META.get("PATH_INFO", "")
        except Exception:
            path = request.META.get("PATH_INFO", "")

        if not any(path.startswith(p) for p in self.path_prefixes):
            return self.get_response(request)

        key = self.get_cache_key(request)
        # key can be None if we can't determine an identity; in that case skip
        if key is None:
            return self.get_response(request)

        history = cache.get(key, []) or []
        now = time.time()
        # keep only timestamps inside the window
        history = [ts for ts in history if now - ts < self.time_window]

        if len(history) >= self.rate_limit:
            # oldest timestamp still in the window
            retry_after = int(self.time_window - (now - history[0]))
            data = {
                "error": "Rate limit exceeded. Try again later.",
                "retry_after": retry_after,
            }
            return JsonResponse(data, status=429)

        history.append(now)
        # set timeout = window so the cache entry expires automatically
        cache.set(key, history, timeout=self.time_window)
        return self.get_response(request)

    def get_cache_key(self, request: HttpRequest) -> Optional[str]:
        try:
            user = getattr(request, "user", None)
            if user and getattr(user, "is_authenticated", False):
                return f"rl:user:{user.id}"
        except Exception:
            # If accessing user throws, fall back to IP below
            pass

        # Fall back to client IP
        ip = request.META.get("REMOTE_ADDR") or request.META.get("HTTP_X_FORWARDED_FOR")
        if not ip:
            return None
        # If X-Forwarded-For contains multiple IPs, take the first
        if "," in ip:
            ip = ip.split(",")[0].strip()
        return f"rl:anon:{ip}"
