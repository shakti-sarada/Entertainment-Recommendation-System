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
├── config/
|       └── global_paths.py     # Global path management
|
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

## 🚀 Deployment on Hugging Face Spaces

You can deploy this Streamlit-based recommendation system on **[Hugging Face Spaces](https://huggingface.co/spaces)** using the following steps:

### 🛠 Prerequisites

- A [Hugging Face account](https://huggingface.co/join)
- Git installed on your system
- [Git LFS](https://git-lfs.com/) installed (for large files like `.pkl`, `.index`, `.jpg`)

---

### 🌐 Step-by-Step Guide

#### 1. Create a new Space
- Go to [https://huggingface.co/spaces](https://huggingface.co/spaces)
- Click **“Create new Space”**
- Fill the form:
  - **Name**: `Entertainment-Recommendation-System`
  - **SDK**: `Docker`
  - **Visibility**: `Public` or `Private`
- Click **“Create Space”**

#### 2. Clone the created Space
```bash
git clone https://huggingface.co/spaces/<your-username>/Entertainment-Recommendation-System
cd Entertainment-Recommendation-System
```

#### 3. Copy your project files (excluding `artifacts/`)
```bash
cp -r ../YourLocalProject/* .
cp -r ../YourLocalProject/.* . 2>/dev/null  # Optional: hidden files
rm -rf artifacts/  # Remove large models if not using LFS
```

#### 4. Track large files using Git LFS
```bash
git lfs install
git lfs track "*.pkl" "*.index" "*.jpg"
git add .gitattributes
```

#### 5. Push to Hugging Face
```bash
git add .
git commit -m "Initial push to Hugging Face Spaces"
git push
```

---

### ✅ Deployment

Once the build completes, your app will be accessible at:

```
https://huggingface.co/spaces/<your-username>/Entertainment-Recommendation-System
```

You can monitor the logs while it builds. The app should be live in a couple of minutes.


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
