from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/登録')
def review():
    return render_template('review.html')

@app.route('/output', methods=['POST'])
def output():
    data1 = request.form['data1']
    data2 = request.form['data2']
    data3 = request.form['data3']
    data4 = request.form['data4']
    data5 = request.form['data5']
    data6 = request.form['data6']
    data7 = request.form['data7']
    return  data1+':'+data2+':'+data3+':'+data4+':'+data5+':'+data6+':'+data7

if __name__=="__main__":
    app.run(debug=True)
