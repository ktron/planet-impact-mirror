
# planet_impact_mirror/streamlit_app.py
import streamlit as st
from agent import satire_bot

st.set_page_config(page_title="Planet Impact Mirror", page_icon="🌍")
st.title("Planet Impact Mirror 🌍🪞")
st.subheader("Who is killing the Earth today?")

query = st.text_area("Ask about a billionaire, industry, or activity. Ask about yourself, too!",)

if st.button("Analyze Planetary Harm"):
    if query:
        with st.spinner("Consulting the planetary reckoning engines..."):
            response = satire_bot(query)
            st.markdown(response)


