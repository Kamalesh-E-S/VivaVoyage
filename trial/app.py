from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage (replace this with a database)
users = []
wishlist = []

# Home page
@app.route('/')
def home():
   
    return render_template('home.html')

# # Signup page
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         # Add user to the database (not implemented here)
#         users.append({'name': name, 'email': email, 'password': password})
#         return redirect(url_for('login'))  # Redirect to login page after signup
#     return render_template('signup.html')

# # Login page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         # Check if email and password match (not implemented here)
#         # If match, set session or cookie to indicate logged-in user
#         return redirect(url_for('explore'))  # Redirect to explore page after login
#     return render_template('login.html')

# Explore page (placeholder)
# @app.route('/explore')
# def explore():
#     return render_template('explore.html')

# # Review page (placeholder)
# @app.route('/review')
# def review():
#     return render_template('review.html')

# # Wishlist page (placeholder)
# @app.route('/wishlist')
# def wishlist():
#     return render_template('wishlist.html')

if __name__ == '__main__':
    app.run(debug=True)
