BookWish – Reading Wishlist

- Frontend (Presentation Tier): HTML + CSS templates  
- Backend (Application Tier):Python (Flask)  
- Database (Data Tier): PostgreSQL  
- Deployment: Docker + GitHub Actions CI  

---

Features

- Add books with title, author, and notes 
- Update status: Want to Read → Reading → Finished**  
- Edit or delete books  
- Filter list by status  
- Server-side validation + flash messages  
- Unit tests with pytest

---

## Architecture

```
+--------------------------+
|   Frontend (HTML/CSS)    |  --> User sees book list & forms
+--------------------------+
             │
             ▼
+--------------------------+
| Backend (Flask/Python)   |  --> Routes, validation, business logic
+--------------------------+
             │
             ▼
+--------------------------+
|  Database (PostgreSQL)   |  --> Books table
+--------------------------+
```

---

## Project Structure
```
bookwish/
├─ app/
│  ├─ __init__.py        # Flask app factory
│  ├─ db.py              # SQLAlchemy init
│  ├─ models.py          # Book model
│  ├─ routes.py          # App routes
│  ├─ forms.py           # Dataclass forms
│  ├─ validators.py      # Validation logic
│  ├─ templates/         # HTML templates
│  │  ├─ base.html
│  │  ├─ index.html
│  │  └─ edit.html
│  └─ static/styles.css  # Styling
├─ migrations/schema.sql # DB schema
├─ tests/test_app.py     # Unit tests
├─ requirements.txt      # Python deps
├─ Dockerfile            # Web service container
├─ docker-compose.yml    # Local dev stack
├─ .env.example          # Sample env vars
└─ .github/workflows/ci.yml # GitHub Actions CI
```

---

## Guide

### 1. Clone the repo
```bash
git clone git link
cd bookwish
```
### Author: Meghana Vipparthi

### 2. Setup environment
```bash
cp .env.example .env
```

### 3. Run with Docker
```bash
docker-compose up --build
```

App runs at http://localhost:5000

### 4. Run tests
```bash
docker-compose run web pytest
```

---

## Database Schema

```sql
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(160) NOT NULL,
  author VARCHAR(120) NOT NULL,
  notes TEXT,
  status VARCHAR(20) NOT NULL DEFAULT 'want',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```
