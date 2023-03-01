from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    with open('benefits.txt', 'r') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
