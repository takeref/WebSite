from flask import Flask

app = Flask(__name__)

app.route('/')
def home():
    return 'Hola Tk'

app.route('/about')
def about():
    return 'Acerk de'

if __name__ == '__main__':
    app.run()
