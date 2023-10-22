from flask import Flask

app=Flask(__name__)

@app.route('/')

def hello_world():
    return 'This is tableau dashboard'

if __name__ == '__main__':
    app.run(debug=False)