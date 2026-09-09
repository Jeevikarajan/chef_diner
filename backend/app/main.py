from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import Request, Form
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base, get_db
from app.models import User, Dialogue
from app.schemas import SignupRequest
from fastapi.responses import FileResponse, RedirectResponse
from pathlib import Path
from sqlalchemy import text, func
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="SECRET_KEY"
)
BASE_DIR = Path(__file__).resolve().parent.parent
CLIENT_DIR = BASE_DIR.parent / "frontend"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"message": "Chef Diner backend is running", "database": result.scalar()}

@app.post("/signup_page")
def signup(
    username: str = Form(...),
    nam: str = Form(...),
    password: str = Form(...),
    age: int = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = pwd_context.hash(password)

    user = User(
        username=username,
        name=nam,
        age=age,
        password_hash=hashed_password,
        score=0,
        is_active=True
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}

@app.post("/index")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == username,
        User.is_active == True
    ).first()

    if not user or not pwd_context.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    request.session["user_id"] = user.id

    return {"redirect": "/open_page.html"}


def is_logged_in(request: Request):
    return request.session.get("user_id") is not None


@app.get("/open_page.html")
def open_page(request: Request):
    if not is_logged_in(request):
        return RedirectResponse(url="/index.html")

    return FileResponse(CLIENT_DIR / "open_page.html")


@app.get("/game.html")
def game_page(request: Request):
    if not is_logged_in(request):
        return RedirectResponse(url="/index.html")

    return FileResponse(CLIENT_DIR / "game.html")



@app.get("/get-dialogue")
def get_dialogue(
    request: Request,
    db: Session = Depends(get_db)
):
    if not is_logged_in(request):
        raise HTTPException(status_code=401, detail="Not authenticated")

    dialogue = db.query(Dialogue).filter(
        Dialogue.is_active == True
    ).order_by(func.random()).first()

    if not dialogue:
        return {
            "Dialogue_Text": "No dialogue found.",
            "Response": ""
        }

    return {
        "Dialogue_Text": dialogue.dialogue_text,
        "Response": dialogue.correct_answer,
        "Explanation": dialogue.explanation
    }

class ScoreRequest(BaseModel):
    score: int

@app.post("/update-score")
def update_score(
    data: ScoreRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.score > user.score:
        user.score = data.score
        db.commit()

    return {"message": "Score updated successfully"}

@app.get("/display-score")
def display_score(
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"Score": user.score}

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/index.html")

app.mount("/", StaticFiles(directory=CLIENT_DIR, html=True), name="client")