# Chef Diner

A cybersecurity awareness game where players identify whether everyday digital situations are safe or suspicious.

Players respond to scenarios using **Accept** or **Reject**, earn points for correct decisions, and have their highest score saved to their account.

## Features

* User registration and login
* Secure password hashing with bcrypt
* Session-based authentication
* Random cybersecurity scenarios
* Accept/Reject decision-based gameplay
* Lives and scoring system
* Persistent high scores
* PostgreSQL database
* Database seeding for game scenarios

## Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Passlib / bcrypt

**Database**

* PostgreSQL
* Neon

## Project Structure

Chef_Diner-main/
├── client/
│   ├── index.html
│   ├── signup_page.html
│   ├── open_page.html
│   ├── game.html
│   └── ...
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── seed.py
│   ├── requirements.txt
│   └── .env
│
├── .gitignore
└── README.md

## API Endpoints

| Method | Endpoint         | Purpose                 |
| ------ | ---------------- | ----------------------- |
| POST   | `/signup_page`   | Register a user         |
| POST   | `/index`         | Login                   |
| GET    | `/logout`        | Logout                  |
| GET    | `/get-dialogue`  | Get a random scenario   |
| POST   | `/update-score`  | Update the user's score |
| GET    | `/display-score` | Get the user's score    |

## Setup

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Chef_Diner.git
cd Chef_Diner

### 2. Create and activate a virtual environment
cd backend
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file inside `backend/`:

DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key

### 5. Start the backend
uvicorn app.main:app --reload

### 6. Seed the game scenarios
In another terminal, from the `backend` directory:
python seed.py


The application will be available at:
http://127.0.0.1:8000


