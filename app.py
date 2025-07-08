from flask import Flask, render_template, request, redirect, session
import sqlite3
import pickle

app = Flask(__name__)
app.secret_key = 'secret123'

# Load ML model files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# SQLite DB connection
def get_db():
    return sqlite3.connect('users.db')

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/', methods=['POST'])
def do_login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cur.fetchone()
    conn.close()

    if user:
        session['user'] = email
        return redirect('/home')
    else:
        return render_template("login.html", error="Invalid Credentials")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        if cur.fetchone():
            return render_template("signup.html", error="User already exists")
       
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return redirect('/')
   
    return render_template("signup.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect('/')
   
    recommendations = []
    if request.method == 'POST':
        movie = request.form['movie']
        if movie in movies['title'].values:
            index = movies[movies['title'] == movie].index[0]
            distances = list(enumerate(similarity[index]))
            movie_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
            recommendations = [movies.iloc[i[0]].title for i in movie_list]

    return render_template("home.html", username=session['user'], movie_list=movies['title'].values, recommended=recommendations)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)