import streamlit as st
import speech_recognition as sr
import google.generativeai as genai

# 🔑 Configure Gemini API key
genai.configure(api_key="Your API key")  #Gemini API key

# 🔍 Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-001")

# 🧠 Ask Gemini model your agriculture question
def ask_gemini(question):
    prompt = f"एक किसान की भाषा में, हिंदी में उत्तर दो:\n{question}"
    response = model.generate_content(prompt)
    return response.text.strip()

# 🎙️ Convert Hindi speech to text
def listen_hindi():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.info("🎤 कृपया बोलना शुरू करें...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='hi-IN')
            return text
        except sr.UnknownValueError:
            return "❌ आवाज़ समझ नहीं आई"
        except sr.RequestError:
            return "❌ स्पीच सर्विस उपलब्ध नहीं है"

import streamlit as st

# 🌾 Streamlit App Config
st.set_page_config(page_title="AgriBot (सारथी बॉट)", page_icon="🌾")

# ✨ Clean White Theme CSS
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
        }
        .big-title {
            font-size: 36px;
            font-weight: 700;
            color: #F5E8C7;
            margin-top: 10px;
        }
        .subheading {
            font-size: 24px;
            font-weight: 500;
            color: #555555;
            margin-bottom: 20px;
        }
        .question {
            font-size: 20px;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #f2f4f5;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            border-left: 4px solid #3498db;
        }
        .answer {
            font-size: 20px;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #f2f4f5;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            border-left: 4px solid #3498db;
        }
         .stButton>button {
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            padding: 14px 30px;
            font-size: 24px;
            font-weight: 900;
            border: none;
        }
        .stButton>button:hover {
            background-color: #3498db;
        }
        
    </style>
""", unsafe_allow_html=True)

# 🌿 App Title and Description
st.markdown('<div class="big-title">🌾 सारथी-AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading">🎤 माइक से हिंदी में सवाल पूछें और टेक्स्ट में उत्तर पाएं</div>', unsafe_allow_html=True)

# 🎙️ Speech Input Button
if st.button("🎙️ सवाल पूछें"):
    user_question = listen_hindi()
    st.markdown(f'<div class="question">❓सवाल: {user_question}</div>', unsafe_allow_html=True)

    if "❌" not in user_question:
        with st.spinner("🤖 विशेषज्ञ से उत्तर लिया जा रहा है..."):
            answer = ask_gemini(user_question)
            st.write("")
            st.write("")
            st.success("✅ उत्तर:")
            st.write("")
            st.markdown(f'<div class="answer">💬 {answer}</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ कृपया फिर से कोशिश करें।")
