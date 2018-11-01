from flask import render_template, flash, redirect, session, url_for, request,jsonify
from app import app, db, login_manager
import os,os.path

@app.route('/')
def index():
    predictedimages = os.listdir('./app/static/img/predicted')
    predictedimages = ['img/predicted/'+file for file in predictedimages]
    humid = open('./app/static/env/humid.txt', 'r') 
    temp = open('./app/static/env/temp.txt', 'r') 
    dist = open('./app/static/env/dist.txt', 'r')  
    return render_template('index.html',images=predictedimages,distance=dist.read(),humidity=humid.read(),temperature=temp.read())

@app.route('/upload',methods=['POST'])
def upload():
    print(request.files['media'])
    file = request.files['media']
    distance = request.files['Distance']
    humidity= request.files['Humidity']
    temperature = request.files['Temperature']
    humid = open('./app/static/env/humid.txt', 'w')
    temp = open('./app/static/env/temp.txt', 'w')
    dist = open('./app/static/env/dist.txt', 'w')
    humid.write(str(humidity))
    humid.close()
    temp.write(str(temperature))
    temp.close()
    dist.write(str(distance))
    dist.close()
    newfilename= len([name for name in os.listdir('./app/static/img/unpredicted/') if os.path.isfile(os.path.join('./app/static/img/unpredicted/',name))])
    print(newfilename)
    newfilename= str(newfilename)
    file.save('app/static/img/unpredicted/'+newfilename+'.jpg')
    os.system('python app/prediction.py app/static/img/unpredicted/'+newfilename+'.jpg'+' app/static/img/predicted/'+newfilename+'.jpg'+' app/static/thumbs/img/predicted/'+newfilename+'.jpg')
    predictedimages = os.listdir('./app/static/img/predicted')
    predictedimages = ['/img/predicted/'+file for file in predictedimages]
    return render_template('index.html',images=predictedimages,distance=str(distance),humidity=str(humidity),temperature=str(temperature))
