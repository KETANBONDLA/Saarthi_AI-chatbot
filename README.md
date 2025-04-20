# 🌾 AgriBot - सारथी बॉट

A simple and intuitive *Hindi voice-enabled AI chatbot for farmers, built using **Streamlit, **Speech Recognition, and **Google Gemini AI. The system listens to a farmer's question in **Hindi, processes it through **Gemini AI*, and responds in simple Hindi text.

---

## ✨ Features

- 🎙 Takes *speech input in Hindi* using microphone  
- 🤖 Uses *Gemini Pro AI* to generate expert answers  
- 💬 Returns response in *Hindi text* for easy understanding  
- 🧑‍🌾 Designed to be *farmer-friendly* with large fonts and clean UI  

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- SpeechRecognition  
- Google Generative AI (Gemini)  
- HTML & CSS (inline in Streamlit)

---

## ⚙ How It Works

1. User speaks their question in Hindi through the mic  
2. Audio is converted to text using Google's Speech Recognition API  
3. Text is sent as a prompt to the Gemini AI model  
4. Gemini responds with an answer in Hindi  
5. The response is displayed in a styled box on screen  

---

## ▶ Usage

Click the 🎙 सवाल बोलें button and ask your farming-related question in Hindi.

Example:  
*User Input (spoken):* "टमाटर की फसल में कौन सी खाद देनी चाहिए?"  
*AI Response (text):* "टमाटर की फसल के लिए नाइट्रोजन, फॉस्फोरस और पोटाश युक्त खाद फायदेमंद होती है।..."

---

## 📁 File Requirements

Make sure the main app file contains your actual Google Gemini API key:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
