from flask import render_template
from app import app
from flask import render_template

@app.route('/')
@app.route('/cv')
def cv():
    return render_template('cv.html', title='cv_html')