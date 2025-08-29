
``` 🎓 Student Buddy – ML Chatbot

📖 Project Overview
Student Buddy – ML Chatbot is a machine learning–powered chatbot designed to help students practice and learn Data Structures & Algorithms (DSA) effectively.  
It uses Natural Language Processing (NLP) and a K-Nearest Neighbors (KNN) model trained on DSA problems to provide step-by-step guidance rather than just direct solutions.  

The project includes both a backend (Flask + ML model) and a frontend (HTML, CSS, JS), making it a complete web-based chatbot application.  


🗂️ Repository Structure
```

STUDENT\_BUDDY\_ML\_CHATBOT/
│
├── backend/                   # Backend files
│   ├── app.py                 # Flask backend (API endpoints)
│   ├── chatbot.py             # Chatbot logic & model integration
│   ├── train\_model.py         # Script for training the ML model
│   ├── requirements.txt       # Python dependencies
│   ├── pycache/           # Auto-generated Python cache files
│
├── model/                     # Saved ML models
│   ├── knn\_model.pkl          # Trained KNN model
│   └── vectorizer.pld         # Text vectorizer for NLP
│
├── dataset/                   # Data sources
│   ├── database (2).csv
│   ├── problems.csv
│   ├── leetcode\_dataset.csv
│   ├── leetcode\_dataset - Ic.csv
│
├── frontend/                  # Web interface
│   ├── index.html             # Chatbot UI
│   ├── script.js              # Frontend logic
│   ├── style.css              # Styling
│   └── Logo.jpg               # Logo for branding
│
└── README.md                  # Project documentation

````


⚙️ Features
- 🤖 AI-Powered Chatbot – Answers DSA-related questions.  
- 📚 Dataset-Driven – Uses curated CSV datasets (LeetCode & problem sets).  
- 🧠 Machine Learning Model – KNN with text vectorization for response matching.  
- 🌍 Web-based Interface – User-friendly frontend with HTML, CSS, and JS.  
- 🔗 Flask REST API – Connects frontend with backend model.  


🛠️ Technology Stack
- Backend: Flask, Scikit-learn, Pandas, Numpy  
- Frontend: HTML, CSS, JavaScript  
- Model: K-Nearest Neighbors (KNN), Vectorizer  
- Other Tools: Pickle (for saving models), Flask-CORS  


🚀 How to Run the Project

1️⃣ Clone the Repository
```
git clone https://github.com/username/STUDENT_BUDDY_ML_CHATBOT.git
cd STUDENT_BUDDY_ML_CHATBOT/backend
````

2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

3️⃣ Train the Model (if needed)

```
python train_model.py
```

4️⃣ Start the Backend (Flask API)

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

5️⃣ Open the Frontend

Go to the `frontend/` folder and open index.html in your browser.
You can now chat with Student Buddy 🎉


📊 Dataset

* `leetcode_dataset.csv` – Contains DSA problem statements.
* `problems.csv` – Additional curated problem set.
* `database (2).csv` – Training & test dataset.


📌 Future Improvements

* 💬 Add NLP deep learning models (e.g., Transformers) for better accuracy.
* 🎯 Implement student progress tracking.
* 🌐 Deploy chatbot as a live web app (Heroku / AWS / Render).
* 🎮 Add gamification features (leaderboards, quizzes).



