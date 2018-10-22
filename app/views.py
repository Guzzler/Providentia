from flask import render_template, flash, redirect, session, url_for, request,jsonify
from app import app, db, login_manager


@app.route('/')
def index():
    return render_template('index.html')
