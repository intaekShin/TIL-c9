import os, csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님!'
    
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result) #flask는 문자형식으로 return해주어야 한다.
    
@app.route('/html_file') #여기서 부터 rander_template 모듈(?)을 끌어온다.
def html_file():
    return render_template('html_file.html')
    
@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)
    
@app.route('/fruits')
def fruits():
    fruits = ['apple', 'banana', 'mango', 'melon']
    return render_template('fruits.html', fruits=fruits)
    
@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    # request.args
    # {'who': 'junwoo', 'message' : 'hello'}
    whoRU = request.args.get('who')
    message = request.args.get('message')
    
    with open('guestbook.csv', 'a', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['who', 'message'])
        writer.writerow({
            'who': whoRU,
            'message': message
        })
    return render_template('receive.html', naming=whoRU, message=message)

@app.route('/guestbook')
def guestbook():
    messages = []
    with open('guestbook.csv', 'r', encoding='utf8', newline='') as f:
        reader =csv.DictReader(f)
        for row in reader:
            messages.append(row)
    
    return render_template('guestbook.html', messages = messages)
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) #실제 서버를 실행시키는 줄이기 때문에 항상 마지막에 입력해야 한다!