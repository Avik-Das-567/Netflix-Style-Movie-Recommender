# 🎬 Netflix-Style Movie Recommender Web App

A fully functional Netflix-inspired movie recommendation system built with **Flask** and **Python**. This project demonstrates how Machine Learning and NLP can power real-world recommendation systems — wrapped in a clean, production-style web app.

---

## ✨ Features
- 🔐 **User Authentication**: Login & logout with personalized greeting
- 🎥 **Movie Recommendation**: Select a movie, get similar movies recommended instantly
- 🧠 **Content-Based Filtering**: Recommendations powered by machine learning similarity algorithms
- 💻 **Clean UI**: Dark-themed, Netflix-inspired, responsive design
- 🛠 **Easy to Extend**: Add collaborative filtering, user history, or deployment to cloud

---
## 🛠 Tech Stack
| Layer         | Technology / Details                                                                 |
|-------------- | ------------------------------------------------------------------------------------ |
| Frontend      | HTML, CSS – Netflix-inspired UI                                                      |
| Backend       | Python, Flask – lightweight web server, routing, authentication                      |
| ML / Recsys   | Content-based filtering (CountVectorizer + cosine similarity) – trained on `movies_dataset.csv` |
| Data Storage  | SQLite (`users.db`) – stores user login data dynamically                             |
| Training Data | CSV file (`movies_dataset.csv`) containing movie metadata (title, tags)              |
| Deployment    | Local Flask server – easily deployable to cloud (e.g., Render, Heroku)                |

---

## 📂 Project Structure

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
## 📊 How it Works
- The app uses a **content-based recommendation algorithm** :
  - Extracts movie features from text tags (e.g., genre, keywords, themes)
  - Converts these tags into numerical vectors using **CountVectorizer**
  - Computes **cosine similarity** between movies
  - Recommends the top N movies most similar to the user's selected movie

- Built to demonstrate :
  - **Feature engineering & vectorization** – transforming text metadata into embeddings
  - **Similarity search & ranking** – finding closest matches based on cosine similarity
  - **Integration of ML into production** – connecting model outputs into a real Flask web app

---
## ✅ Requirements
- Python
- Flask
- pandas
- scikit-learn
- matplotlib
- (Optional) SQLiteStudio – to view `users.db` visually

---
## 🚀 How to Run Locally
- Go to the **Netflix-App Folder** in your PC, and open **Command Prompt** in that folder.

- In the CMD, type :
  ```
  python -m venv venv  
  ```
  This creates a **virtual environment** named `venv`.

- Activate the **Virtual Environment** :
  ```
  venv\Scripts\activate
  ```
- Install the dependencies : **flask**, **pandas** and **scikit-learn**.
  ```
  pip install flask pandas scikit-learn
  ```
- Create the database :
  ```
  python netflixdb.py
  ```
  - This will create **`users.db`** to store the users' **email IDs** and **passwords**.
  - You can open and inspect **`users.db`** using tools like **SQLiteStudio**.

- Train the Model :
  ```
  python train.py
  ```
  - **`movies.pkl`** & **`similarity.pkl`** will be created.

- Run the app :
  ```
  python app.py
  ```
- Open in your browser :
  ```
  http://127.0.0.1:5000
  ```
---
## 📸 Preview Images of the App
- Homepage :

![Netflix_App_Screenshot](https://github.com/user-attachments/assets/90ce9fcc-50d4-4f55-8f81-b6e0541f2d67)

- Login Page :

![Netflix_Login_Screenshot](https://github.com/user-attachments/assets/e12db505-b721-430d-9e92-45f5251cd6ec)

- Sign-Up Page :

![Signup Page](https://github.com/user-attachments/assets/27e8d941-f844-4356-803f-404acc495d50)

---
