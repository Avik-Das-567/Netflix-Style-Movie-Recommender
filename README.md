# 🎥 Netflix-Style Movie Recommender

A content-based movie recommender system built with **Flask**, combining machine learning and interactive visualizations.  
Inspired by Netflix, this web app offers personalized recommendations, trending titles, and direct trailer links — all in a simple, clean interface.

---

## ✨ Features at a Glance

- 🔐 **User Authentication**: Sign up, log in, manage sessions securely.
- 🎯 **Personalized Recommendations**: Suggests similar movies using NLP-based content filtering.
- 📈 **Trending Section**: Highlights top-rated movies (rating > 9).
- 📊 **Visualizations**: Language distribution & genre-wise average rating charts.
- 🎬 **Watch Trailers**: One-click trailer links from YouTube.
- 🛒 **Subscription Plans**: Simulated subscription page with confirmation screen.

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
│   ├── css/
│   │   ├── login.css
│   │   ├── signup.css
│   │   ├── style.css
│   │   ├── subscription.css
│   │   └── watch.css
│   │
│   └── img/
│
├── templates/
│   ├── admin.html
│   ├── home.html
│   ├── login.html
│   ├── payment_success.html
│   ├── signup.html
│   ├── subscription.html
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
| **`clean_data.py`**      | Cleans raw data, standardizes text, removes duplicates, handles missing values |
| **`train.py`**           | Generates vectors & similarity matrix using CountVectorizer & Cosine Similarity   |
| **`netflixdb.py`**       | Creates SQLite database for user login                                  |
| **`app.py`**             | Flask app: handles routing, sessions, recommendations, visualizations   |

---

## 📊 **Extra Features & Visualizations**

- **Visualizations (`/visualize` route)**
  - **Pie Chart :** Shows distribution of movies by language
  - **Bar Chart :** Displays genres where the average rating exceeds 8
  - Generated dynamically with **`matplotlib`** and embedded into the webpage

- **Watch trailers (`/watch/<movie>` route)**
  - Opens the trailer/watch link using pre-collected YouTube URLs stored in **`movie_links.csv`**

- **Subscription & Payment**
  - **`/subscriptions` :** Displays sample subscription plans.
  - **`/payment_success` :** Confirms selected plan after form submission.

- **Admin View (`/admin`)**
  - Opens the login page. If logged in as **admin**, redirects to the homepage like a regular user.

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
- **pickle**: Used to save and load preprocessed data (movie metadata & similarity matrix)

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

![Homepage_1](https://github.com/user-attachments/assets/d3ce49a2-3c90-4a54-a87d-61cb2c2f1417)

- Recommendations Page :

![Homepage_2](https://github.com/user-attachments/assets/74227a48-5393-48a4-b1a1-a5116ff4abcf)

- Visualizations Page :

![Visualization_Page](https://github.com/user-attachments/assets/fb7dfa00-d2cc-4c12-b227-3052693eb67b)

- Sign-up Page :

![Signup_Page](https://github.com/user-attachments/assets/8be5b7c4-3123-45bb-b869-f7f1ae68e78b)

- Sign-in Page :

![Login_Page](https://github.com/user-attachments/assets/bfb927d5-f840-481f-9066-255cc2957b67)

- "Watch Now" Page :

![Watch_on_youtube](https://github.com/user-attachments/assets/e14321bf-9c5e-49ab-b6e1-2a2597ba0b32)

- Subscriptions Page :

![Subscriptions_Page](https://github.com/user-attachments/assets/0bd906f7-6311-4619-b8b9-fbe18f1ea88c)

- "Payment Success" Page :

![Payment_Page](https://github.com/user-attachments/assets/f97b02f0-b28f-42ce-9bdc-825e964f4be9)


---

## 🚀 **Possible Future Improvements**

- Replace plain-text password storage with secure hashing

- Allow users to rate movies and track favorites or watchlists

- Add search auto-suggestions with fuzzy matching for better UX

- Integrate interactive visualizations using Plotly or Chart.js

- Enable basic subscription logic (e.g., restrict features based on plan)

- Improve UI with animations and responsive layouts

- Add movie filtering by genre, language, or rating

---

## 👤 **Author**

Built by **Avik** — For learning, experimenting, and exploring Machine Learning with real-world web apps.

---

## 📄 **License**

This is an open-source portfolio project. Feel free to use, modify, or extend it!

---
