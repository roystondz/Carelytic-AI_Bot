# 🩺 Carelytic

**Carelytic** is an AI-powered healthcare assistant built in Python that leverages Large Language Models (LLMs) on the Groq platform. It accepts both visual (image) and textual input, processes them intelligently, and provides output in both text and spoken audio format.

## ✨ Features

- 🧠 **LLM on Groq** — Ultra-fast inference for medical-related text generation.
- 🖼️ **Image Input** — Accepts medical images (e.g., X-rays, prescriptions).
- 💬 **Text Input** — Accepts natural language queries and clinical notes.
- 🔊 **Text-to-Speech** — Converts AI responses into natural-sounding speech using ElevenLabs or other TTS engines.
- 🛠️ Modular and customizable for various healthcare applications.

## 📸 Demo

![Carelytic Demo](demo/demo.gif) <!-- Replace with actual media or image path -->

## 🏗️ Tech Stack

- **Python**
- **Groq API** – For high-speed LLM inference
- **ElevenLabs / pyttsx3 / gTTS** – For text-to-speech output
- **PIL / OpenCV** – For image handling
- **Gradio / Streamlit (optional)** – For the frontend interface

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/carelytic.git
cd carelytic
```

## Activate virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

- Create a .env file with the following content:

```bash
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key (Eleven Labs is commented  !! if required uncomment it)
```
### 4. Run the app
```bash
python gradio_app.py
```


---
Title: Ai-doctor
app_file: gradio_app.py
sdk: gradio
sdk_version: 5.32.0
---
