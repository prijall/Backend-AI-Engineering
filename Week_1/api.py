from fastapi import Request, Response
from fastapi import APIRouter
import json


router=APIRouter()


@router.get("/")
def home():
    return {"Welcome to the assignment of Week 1"}

@router.get("/info")
def get_data():
    return [{
        "Name": "My name is Prijal Khadka",
        "Position": "Intern",
        "Date_of_birth": 1970,
        "Fav Number": 4
    }]

@router.get("/interest")
def get_interest():
    return {
        "Interest": "My interest lies in working with cutting edge AI technology and make AI more safe and secure. Currently, I am working in AI safety and ALignment",
        "Hobbies": "Singing, Coding/AI_Learning, bike-riding",
        "Achievements": "Coming Soon....."
    }