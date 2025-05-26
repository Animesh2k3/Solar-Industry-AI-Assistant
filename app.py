import streamlit as st
from utils.image_analysis import analyze_image_with_openrouter
from PIL import Image
import os


# Make sure the data directory exists
os.makedirs("data", exist_ok=True)

# Streamlit app settings
st.set_page_config(page_title="🔆 Solar Industry AI Assistant")

# UI Title
st.title("🔆 Solar Industry AI Assistant")
st.write("Upload a rooftop image to analyze its solar installation potential using AI.")

# File uploader
uploaded_file = st.file_uploader("Upload a rooftop image", type=["jpg", "jpeg", "png"])

# When a file is uploaded
if uploaded_file:
    # Save file to disk
    image_path = os.path.join("data", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display image
    st.image(Image.open(image_path), caption="Uploaded Rooftop", use_container_width=True)

    # Analyze button
    if st.button("Analyze Rooftop"):
        with st.spinner("Analyzing rooftop image with AI..."):
            try:
                result = analyze_image_with_openrouter(image_path)
                st.subheader("📊 Analysis Result")
                st.json(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
