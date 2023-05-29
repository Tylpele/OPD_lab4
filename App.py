import math
from flask import Flask, render_template, request
import os

app = Flask(__name__)

img_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = img_folder
links_figur=["http://127.0.0.1:5000/ball", "http://127.0.0.1:5000/cone", "http://127.0.0.1:5000/cylinder", "http://127.0.0.1:5000/prism",
             "http://127.0.0.1:5000/pyramid", "http://127.0.0.1:5000/quader"]

@app.route('/')
@app.route('/index')
def get_gallery():
    image_list = os.listdir("static/images")
    image_list=['images/'+i for i in image_list]
    slov={}
    for i in range(len(image_list)):
        slov[links_figur[i]]=image_list[i]
    return render_template("index.html", slov=slov)

@app.route('/ball', methods=['post', 'get'])
def ball():
    radius=0
    aim=0
    if request.method == 'POST':
        radius = float(request.form.get('radius'))
        aim=int(request.form.get('aim'))
    result=abs(round((4/3)*math.pi*radius**3, aim))
    return render_template('ball.html', result=result)


@app.route('/cone', methods=['post', 'get'])
def cone():
    radius = 0
    height = 0
    aim = 0
    if request.method == 'POST':
        radius = float(request.form.get('radius'))
        height = float(request.form.get('height'))
        aim = int(request.form.get('aim'))
    result = abs(round((1/3)*math.pi*radius**2*height, aim))
    return render_template('cone.html', result=result)


@app.route('/cylinder', methods=['post', 'get'])
def cylinder():
    radius = 0
    height = 0
    aim = 0
    if request.method == 'POST':
        radius = float(request.form.get('radius'))
        height = float(request.form.get('height'))
        aim = int(request.form.get('aim'))
    result = abs(round(math.pi * radius ** 2 * height, aim))
    return render_template('cylinder.html', result=result)


@app.route('/prism', methods=['post', 'get'])
def prism():
    squre=0
    height = 0
    aim = 0
    if request.method == 'POST':
        squre = float(request.form.get('squre'))
        height = float(request.form.get('height'))
        aim = int(request.form.get('aim'))
    result = abs(round(squre * height, aim))
    return render_template('prism.html', result=result)


@app.route('/pyramid', methods=['post', 'get'])
def pyramid():
    squre = 0
    height = 0
    aim = 0
    if request.method == 'POST':
        squre = float(request.form.get('squre'))
        height = float(request.form.get('height'))
        aim = int(request.form.get('aim'))
    result = abs(round((1/3)*squre * height, aim))
    return render_template('prism.html', result=result)


@app.route('/quader', methods=['post', 'get'])
def quder():
    height = 0
    length =0
    width=0
    aim=0
    if request.method == 'POST':
        height = float(request.form.get('height'))
        length = float(request.form.get('length'))
        width = float(request.form.get('width'))
        aim = int(request.form.get('aim'))
    result = abs(round(length * height * width, aim))
    return render_template('quder.html', result=result)


@app.errorhandler(ValueError)
def eror_value(error):
    return render_template('error.html')