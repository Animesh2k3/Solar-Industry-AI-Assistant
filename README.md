# 🔆 Solar Industry AI Assistant

An AI-powered Streamlit tool that analyzes rooftop images using OpenRouter Vision AI to estimate solar installation potential.

## Features

- AI-based rooftop image analysis
- Solar potential, recommended panel type, estimated ROI
- Simple web UI using Streamlit

## Technologies

- OpenRouter API (Qwen Vision Model)
- Python, Streamlit

 Implementation Documentation
## 🛠️ Setup Guide  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/yourusername/solar-ai-assistant.git
   
Install dependencies:
bash
pip install -r requirements.txt  

Add your OpenRouter API key to .env:
env
OPENROUTER_API_KEY=your_key_here  

Run the app:
bash
streamlit run app.py  

📖 Implementation Details
AI Model: Uses OpenRouter’s Qwen Vision model for rooftop analysis.

Output: Returns solar potential, panel recommendations, and ROI estimates in JSON format.

Error Handling: Catches API/upload errors with user-friendly messages.
