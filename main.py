# main.py
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="AI Urdu Shayari Generator", layout="centered")
st.title("📝 AI Urdu Shayari Generator (Offline)")

st.markdown("""
Type any topic or word, and get a beautiful Urdu shayari related to that topic. This works 100% offline using a local shayari dataset.
""")

# Load Dataset
@st.cache_data
def load_shayari():
    df = pd.read_csv("shayari.csv")
    return df

df = load_shayari()

# Search Form
user_input = st.text_input("💬 Enter a topic or word (e.g., محبت, تنہائی, دوست)")

if st.button("🔍 Generate Shayari"):
    if user_input:
        filtered = df[df['topic'].str.contains(user_input, case=False, na=False)]
        if not filtered.empty:
            shayari = filtered.sample(1).iloc[0]['text']
            st.success("Here's a beautiful shayari:")
            st.markdown(f"""<div style='font-size:18px; line-height:1.8;'>{shayari}</div>""", unsafe_allow_html=True)
        else:
            st.warning("😔 No shayari found for this topic. Try another word.")
    else:
        st.error("Please enter a topic to search.")
