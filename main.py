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
  cursor.execute("insert into students values('Divya','MCA',1234081)")
  cursor.execute("insert into students values('Anju','MBA',1234082)")
  cursor.execute("insert into students values('Raj','Btech',1234083)")
  cursor.execute("insert into students values('Chetan','Mtech',1234084)")
  cursor.execute("insert into students values('Amu','Msc',1234085)")
  cursor.execute("UPDATE students SET Name='Raju' WHERE Roll No=1234081" )
  conn.commit()
except Exception as e:
  conn.rollback()
finally:
  cursor.close()
  conn.close()
from fastapi import FastAPI, Request
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
  # return {json.dumps(students)}
    # api_url="http://localhost:8000/my-first-api"
    # form_data={
    # 'param1':'name',
    # 'param2':'course',
    # 'param3':'roll no'
    # }
    # body = b"".join(
    # chunk
    # for chunk in form_data.body
    # )
    # response = requests.post(api_url, data=body, headers=form_data.headers)
    # if response.status_code == 200:
    #     print("Form submitted successfully!")
    #     print("Response:", response.text)
    # else:
    #     print("Failed to submit form. Status code:", response.status_code)
    #     print("Error message:", response.text)
  return templates.TemplateResponse("index.html", {"request": request,"data": students})

@app.get("/my-second-api")
def hello2():
  return {"Hello world! This is my Second API."}
@app.get("/my-third-api")
def add():
  return{"adding "}

@app.get("/my-fourth-api")
def hello(name: str):
  return {'Hello ' + name + '! Have a great day.'} 

@app.get("/welcome-to-programming")
def fun():
  return{ "Okay, Everyone knows that the programming is fun. To learn programming you need to be smart, intelligent and brillant like Chetan Sharma---The Full Stack Developer at Deloitte. And he helped me in learning API'S. Thank You so much Chetan Sharma!"}