from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('squarenumber'))

@app.route('/square',methods=['GET'])
def squarenumber():
    if request.method=='GET': 
        if request.args.get('num') is None:
            return render_template('index.html')
        elif request.args.get('num') =='':
            return"<html><body><h1> No Integer Input</h1></body></html>"
        else:
            number = request.args.get('num')
            # 4% ,R
            try:
                sq=int(number)*int(number)
            except ValueError:
                return"<html><body><h1>Invalid Input</h1></body></html>"
            return render_template('answer.html',squarenum=sq,num=number)
                
if __name__ == '__main__':
    app.run(debug=True)

