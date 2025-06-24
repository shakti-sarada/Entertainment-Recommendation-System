import streamlit as st
from src.recommender.base import BaseRecommender
from src.utils.logger import logger
import base64
import os

st.set_page_config(page_title="Recommendation System", layout="wide")

# === Backgrounds & Icons ===
bg_images = {
    "Anime": "image/anime.jpg",
    "Movie": "image/movie.jpg",
    "Web Series": "image/web_series.jpg"
}

icons = {
    "Anime": "icon/anime.png",
    "Movie": "icon/movie.png",
    "Web Series": "icon/web_series.png"
}

@st.cache_data(show_spinner=False)
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# === CSS for custom horizontal tab bar ===
def inject_css(tab):
    b64_img = get_base64_image(bg_images[tab])
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }}
        .tab-container {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 1rem;
            flex-wrap: nowrap;
        }}
        .tab {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 6px 10px;
            border-radius: 10px;
            background-color: rgba(255,255,255,0.15);
            border: 2px solid transparent;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            min-width: 90px;
        }}
        .tab.selected {{
            border: 2px solid white;
            background-color: rgba(255,255,255,0.3);
        }}
        .tab img {{
            width: 24px;
            height: 24px;
            margin-bottom: 2px;
        }}
        .tab span {{
            font-size: 13px;
            font-weight: 600;
            color: white;
        }}
        input[type="text"]::placeholder {{
            color: rgba(255,255,255,0.6);
        }}
        </style>
    """, unsafe_allow_html=True)

# === Handle initial selection ===
if "selected_tab" not in st.session_state:
    st.session_state["selected_tab"] = "Anime"

# === Handle tab switching ===
query_params = st.query_params
tab_from_url = query_params.get("tab", st.session_state["selected_tab"])
st.session_state["selected_tab"] = tab_from_url
inject_css(tab_from_url)
logger.info(f"Selected tab: {tab_from_url}")

# === Horizontal tab bar ===
tab_list = ["Anime", "Movie", "Web Series"]
tab_icons_b64 = {tab: get_base64_image(icons[tab]) for tab in tab_list}

st.markdown('<div class="tab-container">', unsafe_allow_html=True)
for tab in tab_list:
    selected = "selected" if tab == st.session_state["selected_tab"] else ""
    tab_html = f"""
        <form action="" method="get">
            <input type="hidden" name="tab" value="{tab}" />
            <button type="submit" style="all: unset;">
                <div class="tab {selected}">
                    <img src="data:image/png;base64,{tab_icons_b64[tab]}" />
                    <span>{tab}</span>
                </div>
            </button>
        </form>
    """
    st.markdown(tab_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# === App Title ===
category = st.session_state["selected_tab"]
st.title(f"{category} Recommendation System")

# === Load Models if Not Loaded ===
if "recommenders" not in st.session_state:
    st.session_state["recommenders"] = {}
if "models_loaded" not in st.session_state:
    with st.spinner("⚙️ Warming up recommendation models..."):
        logger.info("Warming up recommendation models...")
        for key in ["anime", "movie", "web_series"]:
            st.session_state["recommenders"][key] = BaseRecommender(content_type=key)
        st.session_state["models_loaded"] = True

# === Input Box ===
placeholder_text = f"Enter a {category} Title"
title_input = st.text_input("", placeholder=placeholder_text, label_visibility="collapsed")

# === Recommendation Output ===
if title_input:
    logger.info(f"User entered title: '{title_input}' in category: {category}")
    try:
        content_key = category.lower().replace(" ", "_")
        recommender = st.session_state["recommenders"][content_key]
        with st.spinner("🔍 Fetching recommendations..."):
            results = recommender.recommend(title_input)

        if isinstance(results, str):
            logger.warning(f"Recommendation issue: {results}")
            st.warning(results)
        else:
            logger.info(f"Recommendations generated for: {title_input}")
            st.dataframe(results.reset_index(drop=True), use_container_width=True)

    except Exception as e:
        logger.error(f"Error during recommendation: {e}")
        st.error("❌ An error occurred while generating recommendations.")
