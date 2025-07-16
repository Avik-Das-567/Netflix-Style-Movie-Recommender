# 🎥 Netflix-Style Movie Recommender

A content-based movie recommender system built with **Flask**, combining machine learning and interactive visualizations.  
Inspired by Netflix, this web app offers personalized recommendations, trending titles, and direct trailer links — all in a simple, clean interface.

---

## ✨ Features at a Glance

- 🔐 **User authentication**: Sign up, log in, and manage sessions.
- 🎯 **Personalized recommendations**: Suggests similar movies based on content (genre, tags, actors, language).
- 📈 **Trending movies**: Highlights top-rated movies (rating > 9).
- 📊 **Visualizations**: Interactive charts showing:
  - Language distribution across movies.
  - Genres with an average rating above 8.
- 🎬 **Watch trailers**: One-click trailer links from YouTube.

---

## 🧠 How It Works

This project uses a **content-based filtering** approach to recommend movies. Here’s an overview of the data flow and logic:

### 1️⃣ Data Collection & Cleaning

- Raw movie data is stored in **`dataset/movies_dataset.csv`**.

- **`clean_data.py`**:
  - Removes duplicates and incomplete records.
  - Standardizes text fields (lowercase, trims spaces).
  - Ensures all movies have valid ratings and image references.

- Clean data is saved to **`dataset/cleaned_movies.csv`**.

### 2️⃣ Feature Engineering & Model Training

- **`train.py`**:
  - Merges key metadata fields: tags, genre, actor, and language into a single text field.
  - Uses **CountVectorizer** (from scikit-learn) to create vector embeddings of each movie.
  - Computes **cosine similarity** between all movie vectors.

- Saves:
  - **`pkl/movies.pkl`**: DataFrame of cleaned movies with metadata.
  - **`pkl/similarity.pkl`**: Pre-computed similarity matrix.

### 3️⃣ Web Application (Flask)

- **`app.py`**:
  - Handles routing, user sessions, and rendering templates.
  - Supports login, signup, logout, recommendations, admin view, and data visualizations.

- Recommendations are served instantly using the pre-computed similarity matrix.

### 4️⃣ Database

- User accounts stored in **SQLite** (`database/users.db`).

- Created using **`netflixdb.py`** script with fields:
  - **`id`** (primary key)
  - **`email`** (unique)
  - **`password`** (plain text)

---

## 🏛 Project Structure

```
Netflix-App/
│
├── scripts/
│   ├── clean_data.py
│   ├── netflixdb.py
│   └── train.py
│
├── static/
│   ├── style.css
│   ├── watch.css
│   ├── bg.jpg
│   └── images
│
├── templates/
│   ├── admin.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── visualize.html
│   └── watch.html
│
├── dataset/
│   ├── movies_dataset.csv
│   ├── movie_links.csv
│   └── cleaned_movies.csv
│
├── pkl/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── database/
│   └── users.db
│
└── app.py
```
---

## ⚙️ Main Modules & Scripts

| Script                | Purpose                                                                |
| -------------------- | ----------------------------------------------------------------------- |
| **`clean_data.py`**      | Cleans raw data, standardizes text, removes duplicates, handles missing |
| **`train.py`**           | Generates vectors & similarity matrix using CountVectorizer & cosine    |
| **`netflixdb.py`**       | Creates SQLite database for user login                                  |
| **`app.py`**             | Flask app: handles routing, sessions, recommendations, visualizations   |

---

## 📊 **Extra Features & Visualizations**

- **Visualizations (`/visualize` route)**
  - **Pie Chart :** Shows distribution of movies by language
  - **Bar Chart :** Shows genres with average rating above 8
  - Generated dynamically with **`matplotlib`** and embedded into the page

- **Watch trailers (`/watch/<movie>` route)**
  - Opens the trailer or watch link using pre-collected YouTube URLs stored in **`movie_links.csv`**

- **Admin** Login button on homepage:
  - Takes you to the login page. If logged in as the admin user, takes you back to the app's homepage.

---

## 🎬 **Recommendation Logic**

When a user selects a movie:
- The app retrieves its index from the movies DataFrame.
- Fetches its row in the similarity matrix.
- Sorts other movies by descending similarity score.
- Recommends the top 5 most similar movies.

Recommendations include:
- Title
- Genre
- Language
- Rating
- Poster image (via `image_file` column)

---

## 🧪 **Technologies & Libraries Used**

- **Python** & **Flask**: Web framework & backend
- **SQLite**: Lightweight relational database
- **Pandas**: Data cleaning & processing
- **scikit-learn**: NLP vectorization & similarity calculation
- **Matplotlib**: Data visualization
- **HTML**: Templates
- **pickle**: Saving and loading trained models

---
## 🚀 How to Run Locally
- Navigate to your local **Netflix-App** folder, and open **Command Prompt** in that folder. Create a **virtual environment** :
  ```
  python -m venv venv  
  ```
- Activate the **virtual environment** :
  ```
  venv\Scripts\activate
  ```
- Install required dependencies : **flask**, **pandas**, **scikit-learn**, **matplotlib**.
  ```
  pip install flask pandas scikit-learn matplotlib
  ```
- Prepare the database :
  ```
  python scripts/netflixdb.py
  ```
  This creates **`users.db`** to store **usernames** and **passwords**.

- Clean the data :
  ```
  python scripts/clean_data.py
  ```
  This generates the **`cleaned_movies.csv`** dataset.

- Train the Recommendation Model :
  ```
  python scripts/train.py
  ```
  This generates **`movies.pkl`** & **`similarity.pkl`**.

- Run the app :
  ```
  python app.py
  ```
- Open your browser and go to :
  ```
  http://127.0.0.1:5000
  ```

---

## 📸 Preview Images (Screenshots of the App)
- Homepage :

![Homepage_1](https://github.com/user-attachments/assets/1acfa540-42ae-4ad6-82b0-e132d719baea)

- Recommendations page :

![Homepage_2](https://github.com/user-attachments/assets/1b9d4341-2113-4175-8117-974d13d0c172)

- Visualizations page :

![Visualization_Page](https://github.com/user-attachments/assets/0a753422-111b-4efe-971c-e0f7243824b4)

- Sign-up Page :

![Signup_Page](https://github.com/user-attachments/assets/a7af236f-7f29-4155-9ce4-52854106bbfb)

- Login Page :

![Login_Page](https://github.com/user-attachments/assets/846d0d33-70bb-404e-8e16-f55f6cab03cd)

- Watch page :

![Watch_on_youtube](https://github.com/user-attachments/assets/740462d8-2fcb-4f17-a406-2edb7e8c5d18)

---

## 🚀 **Possible Future Improvements**

✅ Use password hashing instead of plain text storage  
✅ Add user-specific favorite lists & history  
✅ Deploy the app to cloud (e.g., Heroku, Render)  
✅ Improve search with fuzzy matching  
✅ Add collaborative filtering for even richer recommendations  
✅ Replace static plots with interactive charts (e.g., Plotly)

---

## 👤 **Author**

Built by **Avik** — For learning, experimenting, and exploring Machine Learning with real-world web apps.

---

## 📄 **License**

This is an open-source portfolio project. Feel free to use, modify, or extend it!

---
