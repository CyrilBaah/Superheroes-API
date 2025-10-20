# Superheroes API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2025-FF6B35?style=for-the-badge)

**A production-ready Django REST API for managing superheroes with CI/CD pipelines, Docker support, and comprehensive testing.**

[Features](#features) • [Installation](#installation) • [API Documentation](#api-documentation) • [Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Code Quality](#code-quality)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**Superheroes API** is a modular, scalable Django REST framework application designed to demonstrate best practices in API development, testing, and deployment. This project serves as both a functional API and an educational resource for developers learning modern backend development workflows.

### Key Highlights

- ✅ RESTful API design principles
- ✅ Comprehensive test coverage with unittest and pytest
- ✅ Automated CI/CD pipelines using Dagger
- ✅ Containerized deployment with Docker
- ✅ Code quality tools (Black, Flake8, isort)
- ✅ Health check endpoints for monitoring
- ✅ Open-source and Hacktoberfest-friendly

---

## ✨ Features

- **CRUD Operations**: Complete Create, Read, Update, Delete functionality for superhero entities
- **Health Monitoring**: Dedicated health check endpoints for service availability
- **Database Migrations**: Automated database schema management with Django migrations
- **API Documentation**: Auto-generated OpenAPI schema (schema.yml)
- **Testing Suite**: Comprehensive unit and integration tests
- **Linting & Formatting**: Pre-configured code quality tools
- **Docker Support**: Ready-to-deploy containerized application
- **CI/CD Ready**: Automated testing and deployment pipelines
- **Demo Scripts**: Ready-to-use demonstration scripts

---

## 📁 Project Structure

```
Superheroes-API/
│
├── base/                          # Django project settings
│   ├── __init__.py                # Package initializer
│   ├── settings.py                # Main configuration file
│   ├── urls.py                    # Root URL routing
│   ├── wsgi.py                    # WSGI application
│   └── asgi.py                    # ASGI application
│
├── health/                        # Health check application
│   ├── __init__.py                # Package initializer
│   ├── admin.py                   # Admin panel configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Health data models
│   ├── views.py                   # Health endpoint views
│   ├── urls.py                    # Health URL routing
│   ├── tests.py                   # Health endpoint tests
│   └── migrations/                # Database migrations
│       └── __init__.py
│
├── superheroes/                   # Superheroes application
│   ├── __init__.py                # Package initializer
│   ├── admin.py                   # Admin panel configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Superhero data models
│   ├── serializers.py             # DRF serializers
│   ├── views.py                   # API views
│   ├── urls.py                    # Superhero URL routing
│   ├── tests.py                   # Superhero tests
│   ├── management/                # Custom management commands
│   │   ├── __init__.py
│   │   └── commands/
│   │       └── __init__.py
│   └── migrations/                # Database migrations
│       └── __init__.py
│
├── scripts/                       # Utility and CI/CD scripts
│   ├── demo_health.py             # Health API demonstration
│   ├── demo_heroes.py             # Heroes CRUD demonstration
│   ├── demo_superheroes.py        # Superheroes demo
│   ├── test_health.py             # Health endpoint testing
│   ├── run-test.sh                # Test runner script
│   ├── run-linters.sh             # Code quality checker
│   ├── run-black.sh               # Code formatter
│   ├── run-isort.sh               # Import sorter
│   ├── run-flake8.sh              # Linter script
│   ├── run-dagger-ci.sh           # CI pipeline runner
│   ├── run-dagger-dashboard.sh    # Dagger dashboard
│   └── README.md                  # Scripts documentation
│
├── .github/                       # GitHub configuration
│   └── workflows/                 # GitHub Actions workflows
│       └── *.yml                  # CI/CD workflow files
│
├── .gitignore                     # Git ignore rules
├── dagger_pipeline.py             # Dagger CI/CD pipeline
├── DAGGER_PIPELINE.md             # Pipeline documentation
├── Dockerfile                     # Docker container definition
├── requirements.txt               # Python dependencies
├── .isort.cfg                     # Python file organizer 
├── schema.yml                     # OpenAPI schema
├── manage.py                      # Django management script
├── .flake8                        # Flake8 configuration 
├── LICENSE                        # MIT License
└── README.md                      # Project documentation
```

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.8 or higher
- **pip** (Python package manager)
- **Git** (version control)
- **Docker** (optional, for containerized deployment)
- **Virtual environment** tool (venv or virtualenv)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CyrilBaah/Superheroes-API.git
cd Superheroes-API
```

### 2. Create Virtual Environment

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## 💻 Usage

### Starting the Server

```bash
python manage.py runserver
```

### Running Demo Scripts

```bash
# Health check demo
python scripts/demo_health.py

# Heroes CRUD demo
python scripts/demo_heroes.py

# Superheroes demo
python scripts/demo_superheroes.py
```

---

## 📚 API Documentation

### Base URL

```
http://127.0.0.1:8000
```

### Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| `GET` | `/health/` | API health status | No |
| `GET` | `/api/superheroes/` | List all superheroes | No |
| `POST` | `/api/superheroes/` | Create a new superhero | No |
| `GET` | `/api/superheroes/<id>/` | Retrieve a specific superhero | No |
| `PUT` | `/api/superheroes/<id>/` | Update a superhero | No |
| `PATCH` | `/api/superheroes/<id>/` | Partially update a superhero | No |
| `DELETE` | `/api/superheroes/<id>/` | Delete a superhero | No |

### Example Requests

#### Get All Superheroes

```bash
curl -X GET http://127.0.0.1:8000/api/superheroes/
```

#### Create a Superhero

```bash
curl -X POST http://127.0.0.1:8000/api/superheroes/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Iron Man",
    "alias": "Tony Stark",
    "powers": ["Genius Intellect", "Powered Armor Suit", "Flight"]
  }'
```

#### Get a Specific Superhero

```bash
curl -X GET http://127.0.0.1:8000/api/superheroes/1/
```

### Example Response

```json
{
  "id": 1,
  "name": "Iron Man",
  "alias": "Tony Stark",
  "powers": ["Genius Intellect", "Powered Armor Suit", "Flight"],
  "created_at": "2025-10-14T10:30:00Z",
  "updated_at": "2025-10-14T10:30:00Z"
}
```

### Health Check Response

```json
{
  "status": "healthy",
  "timestamp": "2025-10-14T10:30:00Z",
  "service": "Superheroes API"
}
```

---

## 🧪 Testing

### Run All Tests

```bash
bash scripts/run-test.sh
```

Or using Django's test command:

```bash
python manage.py test
```

### Run Specific Tests

```bash
# Health endpoint tests
python scripts/test_health.py

# Superheroes tests
python manage.py test superheroes

# Health tests
python manage.py test health
```

### Test Coverage

```bash
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t superheroes-api .
```

### Run Container

```bash
docker run -p 8000:8000 superheroes-api
```

### Using Docker Compose (if available)

```bash
docker-compose up
```

The API will be accessible at `http://localhost:8000/`

---

## ⚙️ CI/CD Pipeline

This project uses **Dagger** for CI/CD automation.

### Run CI Pipeline

```bash
bash scripts/run-dagger-ci.sh
```

### Launch Dagger Dashboard

```bash
bash scripts/run-dagger-dashboard.sh
```

### Pipeline Stages

1. **Linting**: Code quality checks (Flake8, Black, isort)
2. **Testing**: Unit and integration tests
3. **Build**: Docker image creation
4. **License Check**: License compliance verification

For more details, see [DAGGER_PIPELINE.md](DAGGER_PIPELINE.md)

---

## 🎨 Code Quality

### Run All Linters

```bash
bash scripts/run-linters.sh
```

### Individual Tools

#### Black (Code Formatter)

```bash
bash scripts/run-black.sh
# or
black .
```

#### isort (Import Sorter)

```bash
bash scripts/run-isort.sh
# or
isort .
```

#### Flake8 (Linter)

```bash
bash scripts/run-flake8.sh
# or
flake8 .
```

### Pre-commit Hooks (Recommended)

```bash
pip install pre-commit
pre-commit install
```

---

## 🤝 Contributing

We welcome contributions from the community! This project is **Hacktoberfest-friendly**.

### How to Contribute

1. **Fork the repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Superheroes-API.git
   cd Superheroes-API
   ```

3. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clean, documented code
   - Add tests for new features
   - Update documentation as needed

5. **Run tests and linters**
   ```bash
   bash scripts/run-test.sh
   bash scripts/run-linters.sh
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your descriptive commit message"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**
   - Go to the original repository
   - Click 'New Pull Request'
   - Select your branch
   - Fill in the PR template
   - Submit for review

### Contribution Guidelines

- ✅ Follow PEP 8 style guidelines
- ✅ Write meaningful commit messages
- ✅ Add tests for new features
- ✅ Update documentation
- ✅ Ensure all tests pass
- ✅ Run linters before submitting
- ✅ One feature per pull request

### Code of Conduct

Please be respectful and constructive in all interactions. We're here to learn and build together!

---

## 👥 Contributors

Thanks to all the amazing contributors who have helped make this project better!

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/CyrilBaah">
            <img src="https://avatars.githubusercontent.com/u/82481611?v=4" width="100;" alt="CyrilBaah"/>
            <br />
            <sub><b>CyrilBaah</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Parthav46">
            <img src="https://avatars.githubusercontent.com/u/25856645?v=4" width="100;" alt="Parthav46"/>
            <br />
            <sub><b>Parthav Patel</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Sougata2006">
            <img src="https://avatars.githubusercontent.com/u/177567075?v=4" width="100;" alt="Sougata2006"/>
            <br />
            <sub><b>Sougata Paul</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Divy13ansh">
            <img src="https://avatars.githubusercontent.com/u/181671379?v=4" width="100;" alt="Divy13ansh"/>
            <br />
            <sub><b>Divyansh Chawla</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Lagmator22">
            <img src="https://avatars.githubusercontent.com/u/133108827?v=4" width="100;" alt="Lagmator22"/>
            <br />
            <sub><b>Lagmator22</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/okay-anshu">
            <img src="https://avatars.githubusercontent.com/u/216655710?v=4" width="100;" alt="okay-anshu"/>
            <br />
            <sub><b>Himanshu Pascalcase</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/CristiCode">
            <img src="https://avatars.githubusercontent.com/u/59974081?v=4" width="100;" alt="CristiCode"/>
            <br />
            <sub><b>Cristina</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Bhavishya2912">
            <img src="https://avatars.githubusercontent.com/u/69957211?v=4" width="100;" alt="Bhavishya2912"/>
            <br />
            <sub><b>Bhavishya</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/kristenking">
            <img src="https://avatars.githubusercontent.com/u/68170283?v=4" width="100;" alt="kristenking"/>
            <br />
            <sub><b>Kristina Degtiareva</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/aritracodes-69">
            <img src="https://avatars.githubusercontent.com/u/117724889?v=4" width="100;" alt="aritracodes-69"/>
            <br />
            <sub><b>Aritra Ghosh</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/BhagwatiOracle">
            <img src="https://avatars.githubusercontent.com/u/165559253?v=4" width="100;" alt="BhagwatiOracle"/>
            <br />
            <sub><b>Bhagwati</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/davidzcode">
            <img src="https://avatars.githubusercontent.com/u/32526223?v=4" width="100;" alt="davidzcode"/>
            <br />
            <sub><b>David</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/Deepakrameshkumar">
            <img src="https://avatars.githubusercontent.com/u/98309550?v=4" width="100;" alt="Deepakrameshkumar"/>
            <br />
            <sub><b>Deepak A</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/SrinjoyeeDey">
            <img src="https://avatars.githubusercontent.com/u/178504847?v=4" width="100;" alt="SrinjoyeeDey"/>
            <br />
            <sub><b>Srinjoyee_Dey</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Django** and **Django REST Framework** communities
- **Hacktoberfest 2025** participants
- All open-source contributors
- **Dagger** for CI/CD automation

---

## 📧 Contact

For questions, suggestions, or support:

- **Repository**: [https://github.com/CyrilBaah/Superheroes-API](https://github.com/CyrilBaah/Superheroes-API)
- **Issues**: [GitHub Issues](https://github.com/CyrilBaah/Superheroes-API/issues)
- **Pull Requests**: [GitHub PRs](https://github.com/CyrilBaah/Superheroes-API/pulls)

---

<div align="center">

**Made with ❤️ by the open-source community**

⭐ Star this repository if you find it helpful!

</div>

---

## 🔐 Rate Limiting

This project includes a comprehensive rate limiting system with both custom middleware and DRF throttling capabilities.

### Features

- **Custom Middleware**: Simple in-memory rate limiting using Django's `LocMemCache`
- **DRF Throttling**: Built-in Django REST Framework throttling support
- **Configurable Limits**: Environment-based configuration for easy customization
- **IP-based Tracking**: Anonymous users tracked by IP address
- **User-based Tracking**: Authenticated users tracked by user ID
- **Graceful Error Handling**: Clear 429 responses with retry information

### Configuration

#### Environment Variables

Create a `.env` file with the following variables:

```bash
# Rate Limiting Configuration
RATE_LIMIT_REQUESTS=100          # Number of requests allowed per window
RATE_LIMIT_WINDOW=60             # Time window in seconds

# DRF Throttling (optional)
DRF_USER_RATE=100/minute         # Rate for authenticated users
DRF_ANON_RATE=20/minute          # Rate for anonymous users
```

#### Default Settings

- **Custom Middleware**: 100 requests per 60 seconds
- **DRF Throttling**: 100/minute for users, 20/minute for anonymous
- **Path Prefixes**: `/api/` and `/health/` endpoints are rate limited

### API Response When Rate Limited

When a user exceeds the rate limit, they receive:

```json
{
    "error": "Rate limit exceeded. Try again later.",
    "retry_after": 49
}
```

- **HTTP Status**: `429 Too Many Requests`
- **Content-Type**: `application/json`
- **retry_after**: Seconds to wait before retrying

### Testing Rate Limits

Use the provided test script to verify rate limiting behavior:

```bash
# Start the development server
python manage.py runserver

# Test rate limiting (in another terminal)
python scripts/test_rate_limit.py \
  --url http://127.0.0.1:8000 \
  --endpoints /api/superheroes/ /health/ \
  --requests 120 \
  --delay 0.05
```

### Quick Test with Lower Limits

For faster testing, temporarily reduce the limits:

```bash
export RATE_LIMIT_REQUESTS=5
export RATE_LIMIT_WINDOW=60
python manage.py runserver
```

### Implementation Details

- **Middleware Location**: `base/middleware.py`
- **Settings Configuration**: `base/settings.py`
- **Test Script**: `scripts/test_rate_limit.py`
- **Cache Backend**: LocMemCache


