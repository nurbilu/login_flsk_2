from flask import Flask, render_template, request , flash  , redirect , url_for
import os 

app = Flask(__name__)

app.secret_key = os.urandom(16) 


user_credentials = [
    {'username': 'user1', 'password': '123456789'},
    {'username': 'user2', 'password': '098765432'},
    {'username': 'user3', 'password': '111222333'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if any(user['username'] == username and user['password'] == password for user in user_credentials):
            # Authentication successful
            return render_template('success.html')
        else:
            # Authentication failed
            flash('Invalid username or password')
            return render_template('login.html')

    # Render the login form for GET requests
    return render_template('login.html')

@app.route('/sign_up', methods=['GET', 'POST'])  
def sign_up():
    if request.method == 'POST':
        # Get sign up data  
        username = request.form['username']
        password = request.form['password'] 
        confirm_password = request.form['confirm_password']
        
        # Validate form data
        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('sign_up.html') 

        if username in [user['username'] for user in user_credentials]:
            flash('Username already exists')
            return render_template('sign_up.html')
        
        # Add new user
        user_credentials.append({
            'username': username,
            'password': password
        })
        
        flash('User created successfully')
        return redirect(url_for('index'))

    return render_template('sign_up.html')

@app.route('/profile')
def profile():
    return render_template('profile.html') 

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=9600)
