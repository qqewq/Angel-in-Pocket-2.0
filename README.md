# Angel-in-Pocket 2.0

Central decision-making agent with GRA stability integration.

## Setup

```bash
# 1. Clone repository and add GRA-Core as submodule
git clone https://github.com/your-org/angel-in-pocket-2.0.git
cd angel-in-pocket-2.0
git submodule add https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library gra_core
git submodule update --init --recursive

# 2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # Linux/Mac; venv\Scripts\activate on Windows
pip install -r requirements.txt

# 3. Configure environment variables
cp config/.env.example .env
# Edit .env with real API keys and DB credentials

# 4. Run database migrations (if using SQL ORM, e.g., Alembic)
alembic upgrade head  # hypothetical

# 5. Start the backend server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# 6. Open dashboard (minimal frontend)
# http://localhost:8000/dashboard/

# Docker alternative:
docker-compose -f docker/docker-compose.yml up --build
```
