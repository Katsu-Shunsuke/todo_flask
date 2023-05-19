from flask import Flask, request, render_template, redirect

app = Flask(__name__)
data = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=data)
    

@app.route('/append', methods=['GET', 'POST'])
def append():
    if request.method == 'POST':
        new = request.form['message']
        if new in data:
            print('既に存在しています')
        else:
            data.append(new)
        return render_template('index.html', todo_list=data)
        
@app.route('/delete', methods=['POST'])
def delete_item():
    item = request.form['item']
    if item in data:
        data.remove(item)
    return redirect('/')

if __name__ == '__main__':
    app.run(port=8080, debug=True)