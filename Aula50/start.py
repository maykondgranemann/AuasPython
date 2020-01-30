from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Starting Flask App'

app.run(debug=True)