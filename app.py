from app import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'