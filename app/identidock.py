from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello  kkk !\n'

@app.route('/test')
def hello_test():
    return 'Hello kkk2!\n'

@app.route('/test/')
def hello_test2():
    return 'Hello kkk5!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


