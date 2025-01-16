# import libararies
from fastapi import FastAPI, Query
from pydantic import BaseModel

class Signup_info(BaseModel) : # dict of data that the user will Enter thiem
    name : str
    email : str
    passwd : str

class Message(BaseModel) : # class to send messages for user
    message : str

app = FastAPI() # the main app

users = [] # list to save data of users

@app.post("/signup") # the post request to create account on signup page
def sign_up(name:str,email:str, passwd:str):
    user = Signup_info(name=name, passwd=passwd, email=email)# dict of user
    users.append(user)# add data of user
    return Message(message="success") # print success

def solve_prob(email, passwd, n=len(users)-1) :
    if email == users[n].email and passwd == users[n].passwd :
        if email == "admin" and passwd == "admin" :
            return users
        return Message(message="success login.")
    elif n == 0 : return Message(message="email or password is incorrect. please again.")
    solve_prob(email=email,passwd=passwd,n=n-1)

@app.get("/login")# the get request to compare the user input with data in login page
def log_in(email:str, passwd:str) :
    return solve_prob(email=email, passwd=passwd)# run solve_prob in log_in func

@app.get("/robots.txt")
def robots():
    return Message(message="fuck you.")