# 🎬 Netflix-Style Movie Recommender Web App

- A fully functional Netflix-inspired movie recommendation system built with **Flask** and **Python**.  
- This project demonstrates how Machine Learning and NLP can power real-world recommendation systems — wrapped in a clean, production-style web app.

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
| ML / Recsys   | Content-based filtering using cosine similarity – Model trained on static `movies_dataset.csv` |
| Data Storage  | SQLite (`users.db`) – stores user login data dynamically                             |
| Training Data | CSV file (`movies_dataset.csv`) containing movie metadata (title, tags)              |
| Deployment    | Local Flask server – easily deployable to cloud (e.g., Render, Heroku)                |

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
- (Optional) SQLiteStudio – to view `users.db` visually

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
- Open in your browser :
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
