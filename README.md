# 🎬 Entertainment Recommendation System

Welcome to the **Entertainment Recommendation System** — a personalized content discovery tool that suggests **Anime**, **Movies**, and **Web Series** based on your preferences. Built with **Streamlit**, **Sentence-BERT**, and **FAISS**, this system provides fast and accurate recommendations through a clean and intuitive UI.

---

## 🚀 Features

- 🔍 **Content-based Recommendations** for anime, movies, and web series.
- ⚡ **Real-time Suggestions** with semantic search using Sentence-BERT.
- 🧠 Efficient similarity search via **FAISS**.
- 🎨 **Custom tab bar UI** with category-specific background and icons.
- 🧾 Error logging and clean modular codebase for easy debugging and scaling.

---

## 📂 Project Structure

```
Entertainment-Recommendation-System/
│
├── app.py                      # Main Streamlit app
├── Dockerfile                  # Docker build configuration
├── requirements.txt            # Python dependencies
├── .env                        # (Optional) Environment variables
│
├── data/
│   ├── raw_data/
│   │   ├── anime/
│   │   ├── movie/
│   │   └── web_series/
│   └── processed_data/
│       ├── anime/
│       ├── movie/
│       └── web_series/
│
├── artifacts/
│   ├── anime/
│   ├── movie/
│   └── web_series/
│
├── icon/                       # Icons for tab bar
├── image/                      # Background images
├── notebook/
│   └── *.ipynb                 # Preprocessing notebooks
│
└── src/
    ├── recommender/
    │   └── base.py             # Recommendation logic
    ├── config/
    │   └── global_paths.py     # Global path management
    └── utils/
        └── logger.py           # Logging utility
```

---

## 📥 Datasets Used

- **Anime & Web Series**: Collected from Kaggle public datasets.
- **Movie**: [MovieLens 32M Dataset](https://grouplens.org/datasets/movielens/)

Organized into `raw_data/` and processed into `processed_data/` for each content type.

---

## 🧪 Preprocessing

To prepare your data and generate the model artifacts:

1. Use your own script or notebook to clean and combine metadata into a `tags` column.
2. Generate Sentence-BERT embeddings and FAISS index.
3. Save the following files in each `artifacts/{content_type}` folder:
   - `data.pkl`
   - `sbert_model.pkl`
   - `faiss_index.index`

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shakti-sarada/Entertainment-Recommendation-System.git
cd Entertainment-Recommendation-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## 🐳 Docker Support

You can also run this project inside a Docker container:

```bash
docker build -t recommender-app .
docker run -p 8501:8501 recommender-app
```

---

## 📒 Logging

All user actions, errors, and recommendations are logged in the `logs/recommender.log` file for monitoring and debugging purposes.

---

## ❗ Troubleshooting

- Ensure all `.pkl` and `.index` files are placed correctly inside the `artifacts` folder.
- Python ≥ 3.8 is recommended.
- Check that `streamlit` and `sentence-transformers` are installed properly.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- **Kaggle Datasets** for anime and web series metadata.
- **GroupLens** for the MovieLens 32M dataset.
- **Streamlit**, **FAISS**, and **SentenceTransformers** libraries.
