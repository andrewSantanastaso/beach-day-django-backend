from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
secret=os.getenv('SECRET_KEY')
