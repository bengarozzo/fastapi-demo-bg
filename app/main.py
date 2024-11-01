#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/hoos")
def greet():
    return {"message": "go hoos!"}


@app.get("/")  # zone apex
def zone_apex():
    return {"Good Day Sunshine": "Ben!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}")
def square(a: int):
    return {"square": a * a}

@app.get("/multiply/{c}/{d}")
def multiply(c:int, d: int):
        return{"product": c * d}

@app.get("/goodbye")
def say_goodbye():
    return {"message": "Goodbye!"}
