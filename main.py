# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# app=FastAPI()
# # instance of fast api object
# # creating routing
# @app.get("/") #home url
# def readroot():
#     return {"message":"Hello Hammad"};

# @app.get("/greet")
# def greet():
#     return {"message":"Hello Hammad, Welcome to FastAPI!"};

# # # for sending data dynamically
# # @app.get("/greet/{name}")
# # def greet_name(name:str):
# #     return {"Message ": f"Hello {name}"};

# @app.get("/greet/{name}")
# def greet_name(name:str):
#      return {"Message ": f"Hello {name}"};

# # @app.get("/greet/{name}")
# # def greet_name(name:str,age:int):
# #     return {"Message ": f"Hello {name}, you are {age} years old!"};

# @app.get("/greet/{name}")
# def greet_name(name:str,age:Optional[int]=None):
#         return {"Message ": f"Hello {name}, you are {age} years old!"};
   
# #  Post
   
# class Student(BaseModel):
#      name:str
#      age:int
#      roll:int
# # now we have to write our root for post request
# @app.post("/create_student")
# def create_student(student : Student):
#      return { "name":student.name,
#              "age":student.age,
#              "roll":student.roll};

# # // request is  basically json formatted data  and fast api use pydantic model to validate the data and convert it into python object
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# # below print for data i expected to be sent in json format
# class Bus_location(BaseModel):
#     latitude:float
#     longitude:float

# @app.get("/")
# def my_setup():
#     return {"status":"I am not blank anymore"}
# # path parameter
# @app.get("/bus/{bus_id}")
# def bus_details(bus_id:int):
#     return {"bus_id":bus_id,"location":"Jhang","Status":"On Time"}


# @app.post("/bus_location")
# def bus_location(bus_id :int,location:Bus_location):
#     return{
#         "message":"Data received successfully",
#         "bus_id":bus_id,
#         "Latitude":location.latitude,
#         "Longitude":location.longitude
#     }
# import sqlite3
# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()


# @app.get("/")
# def read_root():
#     return {"message":"Hello Hammad,Welcome to FastAPI!"}

# #adding path parameter
# @app.get("/greet/{name}")
# def greet_name(name:str):
#     return {"message":f"Hello {name},Welcome to FastAPI!"}

# # 
# class Student(BaseModel):
#     name:str
#     age:int
#     roll:int

# # @app.post("/create_student")
# # def create_student(student:Student):
# #     return{
# #         "name":student.name,
# #         "age":student.age,
# #         "roll":student.roll
# #     }

# # 
# conn=sqlite3.connect("students.db",check_same_thread=False)
# cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS students(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# age INTEGER NOT NULL,
# roll INTEGER NOT NULL)
# """)
# conn.commit()

# @app.post("/create_student")
# def create_student(student:Student):
#     cursor.execute("INSERT INTO students (name,age,roll) VALUES (?,?,?)",(student.name,student.age,student.roll))
#     conn.commit()
#     return {"message":"Student created successfully","name":student.name}

# @app.get("/get_students")
# def get_students():
#     cursor.execute("SELECT * FROM students")
#     students=cursor.fetchall()
#     return {"students":students}

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app=FastAPI()
class BusLocation(BaseModel):
    longitude:float
    latitude:float

# @app.post("/bus_location")
# def bus_location(bus_id:int,location:Bus_location):
#     return{
#         "status":"successfully receieved",
#         "bus_id":bus_id,
#         "longitude":location.longitude,
#         "latitude":location.latitude
#     }
conn=sqlite3.connect("bus.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS bus_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bus_id INTEGER NOT NULL,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

@app.post("/bus_location/{bus_id}")
def record_bus_location(bus_id: int, location: BusLocation):
    cursor.execute(
        "INSERT INTO bus_logs (bus_id, longitude, latitude) VALUES (?, ?, ?)",
        (bus_id, location.longitude, location.latitude)
    )
    conn.commit()
    return {
        "status": "successfully received",
        "bus_id": bus_id,
        "longitude": location.longitude,
        "latitude": location.latitude
    }
# 4. GET route to read history
@app.get("/get_bus_location")
def get_bus_location():
    cursor.execute("SELECT * FROM bus_logs")
    bus_locations = cursor.fetchall()
    return {"bus_locations": bus_locations}