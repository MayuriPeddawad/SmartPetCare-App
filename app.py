from flask import Flask, render_template, request, redirect, url_for
import os
from utils.image_preprocessing import preprocess_image
from utils.prediction import load_model, predict_health

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

model = load_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            image = preprocess_image(filepath)
            result = predict_health(model, image)
            return render_template('results.html', result=result, filepath=filepath)
    return render_template('index.html')

if _name_ == "_main_":
    app.run(debug=True)