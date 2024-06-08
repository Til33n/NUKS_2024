import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import webbrowser
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import requests
from flask import Flask, render_template, request, jsonify
import sys

import smtplib, ssl
from email.message import EmailMessage
import sqlite3
from database import show_all, add_one, delete_one, add_many, data_lookup    #SQLite 3
import database

#USED FOR SHOWING CURRENT DATA IN DATABASE AND GENERAL DEBUGGING 

test_data = [   
    ('11','12','13','14','24'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('21','22','23','24','24'),   # ?,?,?
    ('31','32','33','34','24'),
    ('31','32','33','34','24'),
    ('41','42','43','44','24'),   # ?,?,?    TUPLE PLACEHOLDER WITH ?
    ('51','52','53','54','24'),   # ?,?,?
    ('61','62','63','64','24'),   # ?,?,? 
      ]

dummy_entry = [('X','X','X','X','X'), ]  
test_entry = "Picture.jpg"

#print(database.get_file())
#database.add_one_last(test_entry)
#database.add_many(dummy_entry)
#database.delete_all()
#database.delete_last_input()
#print(type(database.get_file()))
#input_data = [('11','12','13','14','24')]
#database.add_many(input_data)
database.show_all()     



