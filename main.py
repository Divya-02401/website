from fastapi.datastructures import FormData
import requests
import json
import sqlite3 
from fastapi.templating import Jinja2Templates
conn=sqlite3.connect("students")
cursor=conn.cursor()
try:
  conn.execute('BEGIN')
# cursor.execute("create table students ('name' varchar2(25),'course' varchar2(10), 'rollno' number(15))")
  # cursor.execute("delete from students")
  # cursor.execute("insert into students values('Divya','MCA',1234081)")
  # cursor.execute("insert into students values('Anju','MBA',1234082)")
  # cursor.execute("insert into students values('Raj','Btech',1234083)")
  # cursor.execute("insert into students values('Chetan','Mtech',1234084)")
  # cursor.execute("insert into students values('Amu','Msc',1234085)")
  # cursor.execute("UPDATE students SET Name='Raju' WHERE Roll No=1234081" )
  conn.commit()
except Exception as e:
  conn.rollback()
finally:
  cursor.close()
  conn.close()
from fastapi import FastAPI, Form, Query, Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/my-first-api")
def hello1(request: Request):
  conn=sqlite3.connect("students")
  cursor=conn.cursor()
  try:
    conn.execute('BEGIN')
    # cursor.execute("create table students ('name' varchar2(25),'course' varchar2(10), 'rollno' number(15))")
    # cursor.execute("insert into students values('divya','MCA',1234081)")
    cursor.execute("select * from students")
    students=cursor.fetchall()
    print(students)
    conn.commit()
  except Exception as e:
    conn.rollback()
  finally:
    cursor.close()
    conn.close()  
  return templates.TemplateResponse("index.html", {"request": request,"data": students})

@app.post("/add-student")
def add_student(name: str = Form(...), course: str = Form(...),rollno:str=Form(...)):
  conn=sqlite3.connect("students")
  cursor=conn.cursor()
  try:
    query=f"insert into students (course,name,rollno) values('{course}','{name}','{rollno}')"
    print(query)
    conn.execute('BEGIN')
    cursor.execute(query)
    # cursor.execute("insert into students" + name+course+rollno)   
    conn.commit()
  except Exception as e:
    conn.rollback()
  finally:
    cursor.close()
    conn.close()  
  return True  


@app.post("/delete-student")
def delete_student(rollno:str=Form(...)):
  conn = sqlite3.connect("students")
  cursor = conn.cursor()
  try:
      query = f"delete from students where (rollno) = ('{rollno}')"
      print(query)
      conn.execute('BEGIN')
      cursor.execute(query)
      conn.commit()
  except Exception as e:
      conn.rollback()
  finally:
      cursor.close()
      conn.close()
  return True

@app.post("/select-course")
async def search_student(request: Request, course_data: dict):
  conn=sqlite3.connect("students")
  cursor=conn.cursor()
  students=[]
  selected_course = course_data.get('course')

  try:
    query=f"select * from students where course = '{selected_course}'"
    # print(query)
    conn.execute('BEGIN')
    cursor.execute(query)  
    students=cursor.fetchall()
    print(students)
    conn.commit()
  except Exception as e:
    conn.rollback()
  finally:
    cursor.close()
    conn.close()  
  return students












@app.get("/my-second-api")
def hello2():
  return {"Hello world! This is my Second API."}
@app.get("/my-third-api")
def add():
  return{"adding "}

@app.get("/my-fourth-api")
def hello(name: str):
  return {'Hello ' + name + '! Have a great day.'} 
