# Movie Recommendation System

A simple AI-based Movie Recommendation System built using **Python** and **Content-Based Filtering**. This project recommends similar movies to users based on the selected movie using **CountVectorizer** and **Cosine Similarity**.

---

## Features

- Recommend movies based on genre similarity
- Uses Content-Based Filtering
- Calculates similarity using Cosine Similarity
- User-friendly command-line interface
- Handles invalid movie names gracefully
- Lightweight and easy to run

---

## Technologies Used

- Python 3
- Pandas
- NumPy
- Scikit-learn

---

## How It Works

1. Load the movie dataset.
2. Convert movie genres into numerical vectors using **CountVectorizer**.
3. Calculate similarity between movies using **Cosine Similarity**.
4. Ask the user to enter a movie name.
5. Recommend the top 5 most similar movies.

---

## Algorithm Used

### Content-Based Filtering

The recommendation system suggests movies that have similar genres to the movie selected by the user.

### Cosine Similarity

Cosine Similarity measures the similarity between two movies based on their genre vectors.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YourajSingh123/CODSOFT_TASKNO_4__RecommendationSystem-Movie-.git
```

### 2. Navigate to the project folder

```bash
cd CODSOFT_TASKNO_4__RecommendationSystem-Movie-
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## Future Enhancements

- Movie posters using TMDb API
- Search autocomplete
- Web application using Flask
- GUI using Tkinter
- Collaborative Filtering
- Hybrid Recommendation System
- Larger movie dataset

---

## Concepts Covered

- Artificial Intelligence
- Recommendation Systems
- Content-Based Filtering
- Natural Language Processing (Basic)
- Machine Learning Concepts
- Cosine Similarity
- Feature Extraction
- Data Processing with Pandas

---
