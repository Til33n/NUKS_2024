import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from flask import Flask, render_template, request, jsonify, send_file
import smtplib, ssl
from email.message import EmailMessage
import database                                                                                                   # SQLite 3
from database import show_all, add_one, delete_one, add_many, data_lookup, get_last_returned, delete_last_input   # SQLite 3
import numpy as np
from datetime import datetime
from fastapi import File, UploadFile, HTTPException, FastAPI
from flask import Flask, send_from_directory, current_app, jsonify

import requests
import sys
import os
import webbrowser
import requests
import sys

app = FastAPI()



@app.get("/")       # MAIN  index  PAGE 
async def root():
    print("tralala")
    return FileResponse('index.html', media_type='text/html')



@app.get("/input_form")  # MAIN database data fetch and write to database 
def hello(first_email: str = "" ,
          second_email: str = "",
               message: str = "",
         file_location: str = "" ): 

    random_number = np.random.randint(5000, 9999) # generate a EMAIL verification code 
    email_contant = 'Vefification_CODE = '+ str(random_number) 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:    # sending the EMAIL adress thru port 465
        server.login('email.send.377@gmail.com', 'pvudgpgpdxidatja')
        server.sendmail('email.send.377@gmail.com', first_email , email_contant)
        now = datetime.now()            # give current time of process
        current_time = now.strftime("%H:%M:%S")
        input_data = [(first_email, random_number ,second_email ,current_time, message , file_location )]
        database.add_many(input_data)   # adding and saving input data to database
    return FileResponse('authentication.html', media_type='text/html')



@app.get("/verify_email")  # Email verify 
def hello(Verification_code: str = ""):

    code = database.get_code()
    if (str(code) == Verification_code):
    #if ("1" == Verification_code):      # option for faster debugging 
        return FileResponse('upload_file.html', media_type='text/html')
    else: 
        database.delete_last_input()    # if authentication fails, it deletes the last database input
        return FileResponse('index.html', media_type='text/html')  # return back to main page



@app.post("/upload_file")  # UPLOAD file
async def uplaod_2(file: UploadFile = File(...)):   
    file_pth = file.filename
    with open("uploads/" + file_pth, "wb") as F:    
        F.write(await file.read())
                         
    filename = file_pth
    print(filename)
    first_email,random_number ,second_email ,current_time, message = database.get_last_returned()
    input_data = [(first_email,random_number ,second_email ,current_time, message , filename)]         # temporary buffer
    database.delete_last_input()    # delete old data from database
    database.add_many(input_data)   # add bufferand the name of the uploaded file to the last argument


    email_contant = '212.101.137.119/8000/fetch_file/' + str(filename) +"\n" + str(message)  
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('email.send.377@gmail.com', 'pvudgpgpdxidatja')
        server.sendmail('email.send.377@gmail.com', second_email , email_contant)

    #return {"STATUS": "File upload successfull and download URL sent to recepients EMAIL adress:"+ str(second_email)}
    return FileResponse('last_page.html', media_type='text/html' )


#http://212.101.137.119:8000/fetch_file/Picture.jpg

@app.get("/fetch_file/{path}")
def pred_image(path:str):
    print("path",path)
    file_path = "/home/uporabnik/project/uploads" + "/" + path
    return FileResponse(file_path)
        
if __name__ == "__main__":
    uvicorn.run(app, host="212.101.137.119", port=8000)
    app.run(debug = True)






   


   
