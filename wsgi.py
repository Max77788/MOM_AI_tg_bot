from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the Pyrogram bot server running!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
