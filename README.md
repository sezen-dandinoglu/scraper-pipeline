## 📚 Book Data Pipeline & API

This project is an end-to-end data pipeline and API service built with Python.

## 🚀 Features

- Web scraping using BeautifulSoup
- Data cleaning and transformation
- SQLite and PostgreSQL databases with deduplication logic
- Automated scheduling using cron
- REST API built with FastAPI
- CSV export for reporting
- Dockerized for portability
- Deployed to cloud (Render)

---

## Database Support

This project supports both SQLite and PostgreSQL database backends.

- `database_sqlite.py` is used for local learning and lightweight development.
- `database_postgres.py` is used for production-like usage with PostgreSQL.
- Environment variables are managed with `.env`.

Required environment variable:

```env
DATABASE_URL=postgresql://username:password@host/dbname

.env is ignored by Git for security.

---

## Automation & Logs

The pipeline can be scheduled locally using cron.

Runtime logs are written to `log.txt`, but this file is ignored by Git because it is generated locally and may contain environment-specific information.

---

## 📐 Updated Architecture

```text
Scraper
  ↓
Data Cleaning
  ↓
SQLite / PostgreSQL
  ↓
Deduplication
  ↓
Analytics
  ↓
CSV Export + FastAPI
  ↓
Render / Docker

---

## 🔌 API Endpoints

### Get all books

GET /books


### Get price summary

GET /summary


Example response:

```json
{
  "max_price": 57.25,
  "min_price": 13.99,
  "avg_price": 38.05
}

---

🐳 Docker

Build the image:

docker build -t scraper-pipeline-api .

Run the container:

docker run -p 8000:8000 scraper-pipeline-api

Access:

http://localhost:8000/docs

---

⚙️ Local Setup
pip install -r requirements.txt
uvicorn app:app --reload

---

⏰ Scheduler

The pipeline is automated using cron:

* 9 * * * python main.py

---

📂 Project Structure
.
├── app.py
├── main.py
├── scraper.py
├── database.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── books_sample.csv
├── summary_sample.csv

---

🌐 Live Demo
https://scraper-pipeline.onrender.com/docs

---

🧠 What I Learned
Building end-to-end data pipelines
API development with FastAPI
Working with SQLite and SQL aggregation
Automating tasks with cron
Containerization with Docker
Deploying services to the cloud

---

📌 Notes
SQLite is used for simplicity
Free hosting environments may not persist data permanently
