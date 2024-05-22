"""
{
 "firstName": "string",
 "lastName": "string",
 "email": "string",
 "password": "string"
}
 -> DB 유저 정보 저장
{
 "message": "회원가입 성공",
}
"""

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# model
class UserModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

@app.post("/signup")
def signup(user:UserModel):
    print("DB에 저장 중....")
    return {"message": "회원가입 성공"}