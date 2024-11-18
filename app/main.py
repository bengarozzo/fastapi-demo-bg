#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}
