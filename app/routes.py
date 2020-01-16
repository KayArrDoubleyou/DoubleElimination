from app import app
from flask import render_template, request, redirect
#import pygal
#import json
#from datetime import datetime, timedelta
#import re


#--------------------------------------------------------------
# Main Page - Also the only page right now. Does everything
#--------------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return render_template('index.html',title='Home')
