# Fastapi-students
# 📚 FastAPI Student Management API

A simple CRUD API for managing students using **FastAPI** and **SQLite**.

---

## 🚀 Features
- Create, read, update, delete student records
- SQLite database with SQLAlchemy ORM
- Pydantic models for validation
- FastAPI interactive docs (Swagger UI)

---

## 📦 Installation

1️⃣ Clone this repository:

git clone https://github.com/<your-username>/fastapi-students.git
cd fastapi-students
2️⃣ Create a virtual environment & activate:


python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies:


pip install -r requirements.txt
▶️ Run the Application

uvicorn app.main:app --reload
Access API docs at:
Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc

📂 Project Structure


app/
 ├── main.py        # FastAPI app entry point
 ├── models.py      # SQLAlchemy models
 ├── schemas.py     # Pydantic schemas
 ├── crud.py        # CRUD operations
 ├── db.py          # Database config
📌 Example API Requests
Create a student:

POST /students
{
    "name": "John Doe",
    "age": 21,
    "year": "3rd"
}
Get all students:
json
Copy
Edit
GET /students
🛠 Tech Stack
FastAPI

SQLAlchemy

SQLite

Pydantic

🤝 Contributing
Pull requests are welcome! Please fork this repo and create a PR.

📜 License
This project is licensed under the MIT License.


---

## **📄 requirements.txt**
fastapi
uvicorn
sqlalchemy
pydantic


