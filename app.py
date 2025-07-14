# app.py
import streamlit as st
import os
from main import extract_username
from scraper import scrape_comments_from_user_page
from persona import build_prompt, call_groq, clean_persona_output
from persona_img import generate_persona_image
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
st.title("PersonaGen: Reddit Persona Generator")

url = st.text_input("Enter Reddit user comments URL:")

if st.button("Generate Persona"):
    if not url:
        st.warning("Please enter a Reddit user comments URL.")
    else:
        username = extract_username(url)
        st.info(f"Scraping comments for {username}...")
        comments = scrape_comments_from_user_page(url)
        prompt = build_prompt(username, comments)
        st.info("Generating persona...")
        persona = call_groq(prompt)
        if persona is None:
            st.error("Failed to generate persona. Please check your API key, internet connection, or try again later.")
        else:
            persona_clean = clean_persona_output(persona)

            # Save persona text
            os.makedirs("output", exist_ok=True)
            text_path = f"output/{username}_persona.txt"
            with open(text_path, "w") as f:
                f.write(persona_clean)

            st.success("Persona generated!")
            st.text_area("Persona", persona_clean, height=400)

            # Download persona text
            with open(text_path, "rb") as f:
                st.download_button("Download Persona Text", f, file_name=f"{username}_persona.txt")

            # Generate and show persona image
            image_path = f"output/{username}_persona.png"
            generate_persona_image(persona_clean, image_path)
            st.image(image_path, caption="Persona Image", use_column_width=True)

            # Download persona image
            with open(image_path, "rb") as img_file:
                st.download_button("Download Persona Image", img_file, file_name=f"{username}_persona.png")