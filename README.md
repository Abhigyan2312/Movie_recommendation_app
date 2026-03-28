# 🎬 Movie Recommendation System (AI/ML Project)

## 📌 Overview

This project is a **Movie Recommendation System** built using **Machine Learning** and **Python**. It suggests movies based on user selection by analyzing similarities between movies using **content-based filtering**.

The system also fetches **real-time movie details and posters** using the OMDb API and displays them in an interactive **Tkinter GUI**.

---

## 🎯 Features

* 🎥 Movie recommendation based on similarity
* 🧠 Content-based filtering using ML
* 📊 Cosine similarity for accurate suggestions
* 🖥️ Interactive GUI using Tkinter
* 🌐 Real-time movie details via OMDb API
* 🖼️ Displays movie posters

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * Pandas
  * Scikit-learn
  * Requests
  * Tkinter
  * PIL (Pillow)
* **API:** OMDb API
* **Dataset:** movies.csv

---

## ⚙️ How It Works

1. The dataset is loaded and cleaned
2. Important features (genres, keywords, overview) are combined
3. Text data is converted into numerical form using CountVectorizer
4. Cosine similarity is calculated between movies
5. User selects a movie from the GUI
6. System recommends top 5 similar movies
7. Movie details and poster are fetched using API

---

## 📂 Project Structure

```
├── Movie Reccomandation.py
├── movies.csv
├── PROJECT REPORT AIML.docx
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Install dependencies

```
pip install pandas scikit-learn requests pillow
```

### 3️⃣ Add Dataset

* Place `movies.csv` in the project folder
* Update file path in code if required

### 4️⃣ Add API Key

* Get API key from: http://www.omdbapi.com/
* Replace in code:

```python
API_KEY = "YOUR_API_KEY"
```

### 5️⃣ Run the project

```
python "Movie Reccomandation.py"
```

---

## 🖥️ Output

* Select a movie from dropdown
* Click **Recommend**
* Get:

  * ✅ Top 5 recommended movies
  * 🎬 Movie poster
  * 📅 Year
  * 🎭 Actors
  * 🎬 Director
  * ⭐ IMDb rating

---

## 📊 Algorithm Used

* Content-Based Filtering
* Count Vectorization
* Cosine Similarity

---

## ✅ Advantages

* Simple and easy to use
* No user data required
* Fast recommendations
* Interactive GUI

---

## ⚠️ Limitations

* No personalized recommendations
* Depends on dataset quality
* Requires internet for API
* Limited diversity in results

---

## 🔮 Future Enhancements

* Add collaborative filtering
* Improve UI design
* Deploy as web app (Streamlit/Flask)
* Add user authentication
* Use deep learning models

---

## 🌍 Real-World Applications

* OTT platforms (Netflix, Prime Video)
* E-commerce recommendations
* Music streaming apps
* Content discovery systems

---

## 👨‍💻 Author

**Abhigyan Tiwari**
CSE (AI-ML)

---

## 📚 References

* Scikit-learn Documentation
* Pandas Documentation
* OMDb API
* Python Tkinter Documentation

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
