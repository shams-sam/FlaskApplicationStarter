import sys
sys.path.append('/nlp')

from flask import Flask, render_template, \
    url_for, redirect, session, request
import re

from forms import Form
from config import Config

from feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/flask_status", methods=["GET"])
def flask_status():
    return "Flask server is running..."

@app.route("/nlp", methods=["GET", "POST"])
def index():
    form = Form()
    data = {
        'text': '',
        'result': {},
    }

    if form.validate_on_submit():
        text = request.form['text']
        text = re.sub('\s+', ' ', text)
        data['text'] = text
        print(extractor.rules)
        data['result'] = extractor.label(text)

    return render_template('index.html', form=form, data=data, page="index")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
