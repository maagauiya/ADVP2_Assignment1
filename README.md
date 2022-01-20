# To Do List with authentication

**Installation**<br />
pip install Django<br />
pip install psycopg2<br />
pip install Jinja2 <br />

**Usage**<br />
from django.shortcuts import redirect, render <br />
from .models import* <br />
from django.contrib.auth import authenticate, login <br />

**Examples**<br />
You can write to the text label your task and <br />
press button create then it will shows in list also you can <br />
refresh, delete and update the tasks
