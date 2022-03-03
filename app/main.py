from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/cv')
def index():
    return render_template('cv.html', title='cv_html')

if __name__ == "__main__":
    app.run()

