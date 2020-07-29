from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello There!</h1>'
@app.route('/home',methods=['GET','POST'])
def home():
    links = ['https://www.youtube.com','https://www.bing.com',
            'https://www.python.org','https://www.ruk-com.in.th']
    return render_template('example.html',links=links)
if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port=80)