# 🎬 Netflix-Style Movie Recommender Web App

A fully functional Netflix-inspired movie recommendation system built with **Flask** and **Python**.  
This project demonstrates how machine learning and data science can be applied to create an engaging, production-like web application.

---

## ✨ Features
- 🔐 **User Authentication**: Login & logout with personalized greeting
- 🎥 **Movie Recommendation**: Select a movie, get similar movies recommended instantly
- 🧠 **Content-Based Filtering**: Recommendations powered by machine learning similarity algorithms
- 💻 **Clean UI**: Dark-themed, Netflix-inspired, responsive design
- 🛠 **Easy to Extend**: Add collaborative filtering, user history, or deployment to cloud

---

## 🛠 Tech Stack
| Layer       | Technology                          |
| ----------  | -----------------------------------  |
| Frontend    | HTML, CSS     |
| Backend     | Python, Flask                       |
| ML / Recsys | Content-based filtering (cosine similarity) |
| Database    | SQLite or CSV (movie metadata, users data) |
| Deployment  | Local server (Flask) - easily deployable to Heroku, Render, etc. |

---

## 📂 Project Structure

```
Netflix-App/
│
├── static/
│   └── style.css
│   └── bg.jpg
│
├── templates/
│   └── home.html
│   └── login.html
│   └── signup.html
│
├── app.py
├── train.py
├── netflixdb.py
├── movies_dataset.csv
├── movies.pkl
├── similarity.pkl
└── users.db
```
---
## 📊 How it Works
- The app uses a **content-based recommendation algorithm**:
  - Extracts movie features (e.g., genre, keywords, cast)
  - Computes **cosine similarity** between movies
  - Recommends movies most similar to the user’s selection
- Built to demonstrate:
  - Feature engineering & vectorization
  - Similarity search & ranking
  - Integration of ML into real applications

---
## 🚀 How to Run Locally
- Go to the **Netflix Project Folder** in your PC, and open **Command Prompt** in that folder.

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
- Prepare the database :
  ```
  python netflixdb.py
  ```
  - **`users.db`** will be created.
  - In this database, we can store the Users' **email ids** and **passwords** for login.
  - **`users.db`** can be opened using **SQLiteStudio**.

- Train the Model :
  ```
  python train.py
  ```
  - **`movies.pkl`** & **`similarity.pkl`** will be created.

- Run the app :
  ```
  python app.py
  ```
- Go to this link in browser :
  ```
  http://127.0.0.1:5000
  ```
---
## Preview Images (screenshots) of the App
- Homepage :

![Netflix_App_Screenshot](https://github.com/user-attachments/assets/90ce9fcc-50d4-4f55-8f81-b6e0541f2d67)

- Login Page :

![Netflix_Login_Screenshot](https://github.com/user-attachments/assets/e12db505-b721-430d-9e92-45f5251cd6ec)

---
