# 🦸‍♂️ Superheroes API

A comprehensive Django REST API for managing superhero data with full CRUD operations, filtering, statistics, and interactive documentation.

##  Features

- **Full CRUD Operations**: Create, read, update, and delete superheroes
- **Advanced Filtering**: Filter by universe, power level, status, and more
- **Statistics Endpoint**: Get insights about your superhero collection
- **Interactive Documentation**: Swagger UI and ReDoc integration
- **Health Monitoring**: Built-in health check endpoints
- **Docker Support**: Containerized deployment ready
- **CI/CD Pipeline**: Automated testing with Dagger
- **Database Seeding**: Pre-populated with sample superhero data

##  Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Database Seeding](#-database-seeding)
- [Docker Deployment](#-docker-deployment)
- [Development](#-development)
- [Testing](#-testing)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)

##  Quick Start

### Prerequisites

- Python 3.9+
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/CyrilBaah/Superheroes-API.git
cd Superheroes-API
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env  # Create your environment file
# Edit .env with your preferred settings
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Seed the Database (Optional)

```bash
python manage.py populate_superheroes
```

### 7. Start the Server

```bash
python manage.py runserver
```

 **Your API is now running at** `http://localhost:8000`

##  Installation

### Method 1: Local Development

1. **Clone and navigate to the project:**
   ```bash
   git clone https://github.com/CyrilBaah/Superheroes-API.git
   cd Superheroes-API
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file with your settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_TYPE=sqlite  # or postgres for production
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Method 2: Using Scripts

Use the provided convenience scripts:

```bash
# Start the server with migrations
./scripts/run-server.sh

# Run tests
./scripts/run-unittest.sh

# Run linting
./scripts/run-linters.sh
```

##  API Endpoints

### Base URL
```
http://localhost:8000/api/
```

### Superheroes Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/superheroes/` | List all superheroes |
| `POST` | `/api/superheroes/` | Create a new superhero |
| `GET` | `/api/superheroes/{id}/` | Get a specific superhero |
| `PUT` | `/api/superheroes/{id}/` | Update a superhero |
| `PATCH` | `/api/superheroes/{id}/` | Partially update a superhero |
| `DELETE` | `/api/superheroes/{id}/` | Delete a superhero |
| `GET` | `/api/superheroes/stats/` | Get superhero statistics |

### Health Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health/` | Basic health check |
| `GET` | `/health/detailed/` | Detailed health information |

### Filtering & Search

The API supports advanced filtering:

```bash
# Filter by universe
GET /api/superheroes/?universe=Marvel

# Filter by power level
GET /api/superheroes/?power_level=8

# Filter active superheroes
GET /api/superheroes/?is_active=true

# Search by name
GET /api/superheroes/?search=Spider

# Combine filters
GET /api/superheroes/?universe=DC&power_level__gte=7&is_active=true
```

### Example API Usage

#### Create a Superhero
```bash
curl -X POST http://localhost:8000/api/superheroes/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Iron Man",
    "real_name": "Tony Stark",
    "alias": "The Armored Avenger",
    "age": 45,
    "height": "185.00",
    "weight": "85.00",
    "powers": "Genius intellect, powered armor suit, flight, repulsors",
    "power_level": 8,
    "origin_story": "Billionaire inventor who built a powered suit of armor",
    "universe": "Marvel",
    "is_active": true,
    "is_villain": false
  }'
```

#### Get Statistics
```bash
curl http://localhost:8000/api/superheroes/stats/
```

##  Database Seeding

The project includes a management command to populate the database with sample superhero data.

### Seed with Sample Data

```bash
# Add sample superheroes to the database
python manage.py populate_superheroes

# Clear existing data and add fresh samples
python manage.py populate_superheroes --clear
```

### Sample Heroes Included

The seed command includes popular superheroes from various universes:
- **Marvel**: Spider-Man, Iron Man, Captain America, Thor, Hulk
- **DC**: Batman, Superman, Wonder Woman, Flash, Green Lantern
- **Custom**: Original characters with unique abilities

Each hero comes with:
- Complete profile information
- Powers and abilities
- Origin stories
- Physical attributes
- Power level ratings (1-10)


## Development

### Project Structure

```
Superheroes-API/
├── base/                   # Django project settings
├── superheroes/           # Main app with superhero models
├── health/                # Health check app
├── scripts/               # Utility scripts
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
├── Dockerfile            # Container configuration
└── README.md             # This file
```

##  Testing

### Run All Tests

```bash
python manage.py test

# With coverage
coverage run --source='.' manage.py test
coverage report
```

### Run Specific Tests

```bash
# Test superheroes app only
python manage.py test superheroes

# Test health app only
python manage.py test health

# Verbose output
python manage.py test -v 2
```

### Demo Scripts

Test the API with provided demo scripts:

```bash
# Test health endpoints
python scripts/demo_health.py

# Test superhero endpoints
python scripts/demo_superheroes.py

# Demo all heroes functionality
python scripts/demo_heroes.py
```

##  API Documentation

### Interactive Documentation

Once the server is running, visit these URLs for interactive API documentation:

- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

### Admin Interface

Access the Django admin interface at:
- **Admin Panel**: http://localhost:8000/admin/

Create a superuser to access the admin:
```bash
python manage.py createsuperuser
```

##  Development Tools

### Code Quality

```bash
# Format code with Black
./scripts/run-black.sh

# Sort imports with isort
./scripts/run-isort.sh

# Lint with flake8
./scripts/run-flake8.sh

# Run all linters
./scripts/run-linters.sh
```

### CI/CD Pipeline

The project includes a Dagger-based CI/CD pipeline:

```bash
# Run the full CI pipeline
./scripts/run-dagger-ci.sh

# View pipeline dashboard
./scripts/run-dagger-dashboard.sh
```

##  Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: `python scripts/run-unittest`
5. **Run linters**: `./scripts/run-linters.sh`
6. **Commit changes**: `git commit -m 'Add amazing feature'`
7. **Push to branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages
- Ensure all tests pass before submitting

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Support

If you have any questions or run into issues:

1. Check the [Issues](https://github.com/CyrilBaah/Superheroes-API/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

---

**Happy coding!**

