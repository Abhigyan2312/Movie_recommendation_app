import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "15c9be74"

movies = pd.read_csv(r"D:\User\Downloads\FireShot\AIML\movies.csv")

features = ['genres', 'keywords', 'overview']
for f in features:
    movies[f] = movies[f].fillna('')

movies["combined"] = movies['genres'] + " " + movies['keywords'] + " " + movies['overview']

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(movies["combined"])
similarity = cosine_similarity(matrix)

movies['title_lower'] = movies['title'].str.lower()

def get_movie_data(name):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={name}"
    res = requests.get(url).json()
    if res['Response'] == 'True':
        return res
    return None

def show_result():
    name = combo.get().lower()

    if name not in movies['title_lower'].values:
        messagebox.showerror("Error", "Movie not found")
        return

    idx = movies[movies['title_lower'] == name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "Recommended Movies:\n\n")

    for i in scores:
        result_box.insert(tk.END, "• " + movies.iloc[i[0]].title + "\n")

    data = get_movie_data(combo.get())

    if data:
        if data.get("Poster") and data["Poster"] != "N/A":
            img_data = requests.get(data["Poster"]).content
            img = Image.open(BytesIO(img_data)).resize((150, 220))
            photo = ImageTk.PhotoImage(img)
            poster_label.config(image=photo)
            poster_label.image = photo
        else:
            poster_label.config(image='')

        info = f"""
Year: {data.get('Year')}
Director: {data.get('Director')}
Actors: {data.get('Actors')}
IMDb Rating: {data.get('imdbRating')}
"""
        info_box.delete(1.0, tk.END)
        info_box.insert(tk.END, info)

root = tk.Tk()
root.title("Movie Recommender")
root.geometry("700x650")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Movie Recommender", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=15)

label = tk.Label(root, text="Select Movie:", font=("Arial", 12), bg="#1e1e2f", fg="white")
label.pack()

combo = ttk.Combobox(root, width=50)
combo['values'] = list(movies['title'].head(200))
combo.pack(pady=10)

btn = tk.Button(root, text="Recommend", command=show_result, bg="#ff4b5c", fg="white")
btn.pack(pady=10)

poster_label = tk.Label(root, bg="#1e1e2f")
poster_label.pack(pady=10)

result_box = tk.Text(root, height=10, width=80, bg="#2b2b3c", fg="white")
result_box.pack(pady=10)

info_box = tk.Text(root, height=8, width=80, bg="#1e1e2f", fg="lightgreen")
info_box.pack(pady=10)

root.mainloop()
