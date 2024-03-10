from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ABcde#1234'

users = {
    'user1' : {'name':'User One', 'email':'cpbagul150@gmail.com', 'password':'123#456'},
    'user2' : {'name':'User Two', 'email':'vaishalishardul@gmail.com', 'password':'789#654'}, 
}

@app.route("/")
def index():
    if 'username' in session:
        user = users[session['username']]
        return render_template('index.html', user = user)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and password == users[username]['password']:
            session['username'] = username
            session['password'] = password
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)