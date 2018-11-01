from flask import render_template, flash, redirect, session, url_for, request,jsonify
from app import app, db, login_manager
import os,os.path

@app.route('/')
def index():
    predictedimages = os.listdir('./app/static/img/predicted')
    predictedimages = ['img/predicted/'+file for file in predictedimages]
    return render_template('index.html',images=predictedimages)

@app.route('/upload',methods=['POST'])
def upload():
    print(request.files['media'])
    file = request.files['media']
    newfilename= len([name for name in os.listdir('./app/static/img/unpredicted/') if os.path.isfile(os.path.join('./app/static/img/unpredicted/',name))])
    print(newfilename)
    newfilename= str(newfilename)
    file.save('app/static/img/unpredicted/'+newfilename+'.jpg')
    os.system('python app/prediction.py app/static/img/unpredicted/'+newfilename+'.jpg'+' app/static/img/predicted/'+newfilename+'.jpg')
    predictedimages = os.listdir('./app/static/img/predicted')
    predictedimages = ['/img/predicted/'+file for file in predictedimages]
    return render_template('index.html',images=predictedimages)
