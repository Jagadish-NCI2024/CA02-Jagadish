from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3' # Connect us our app. file to the database
# db = SQLAlchemy(app) #create database instance
# app.app_context().push()
# #db.init_app(app)
# app.config ['SECRET_KEY'] = 'thisisasecretkey'
def create_table():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment TEXT
    )
    ''')
    conn.commit()
    conn.close()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False,unique=True)
#     password = db.Column(db.String(80), nullable=False)

#     def __init__(self,name,password):
#         self.name = name
#         self.password = password
        

    
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')



# Run the flask App
if __name__ == '__main__':
   
    app.run(debug=True)

















