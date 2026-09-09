from pydantic import BaseModel


class SignupRequest(BaseModel):
    username: str
    nam: str
    password: str
    age: int

