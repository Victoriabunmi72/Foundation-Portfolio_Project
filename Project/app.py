from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check login credentials and perform authentication
        # You can add your login authentication logic here
        return 'Login Successful'  # Redirect to a success page or perform further actions

    # Render the login form template for GET request
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
