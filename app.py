from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Sample roast statements
roasts = [
    "Bro really said fashion and chose violence 💀",
    "This outfit looks like WiFi signal — weak 📶",
    "Are you dressing or experimenting? 🤔",
    "Even Google can't find this style 🔍",
    "This outfit needs a software update ⚠️",
    "Fashion police called, they're coming 🚓",
    "Did a toddler pick this out? 👶",
    "Your outfit has a 404 error ⚠️",
    "Bold choice… but why tho? 😳",
    "Did you try to roast yourself with clothes? 🔥"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roast', methods=['POST'])
def roast():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))
    
    # Save file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Pick random roast
    roast_statement = random.choice(roasts)

    return render_template('result.html', image_path=filepath, roast=roast_statement)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)