import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up Streamlit page configuration
st.set_page_config(page_title='Ayush Chatbot', layout='wide')

st.markdown("<h1 style='display: flex; align-items: center;'>Mr.AYUSH</h1>", unsafe_allow_html=True)

# Define the function to get a response from Gemini
def get_gemini_response(user_input):
    model = genai.GenerativeModel('gemini-pro')
    prompt = input_prompt + "\n\n" + user_input  # Combine input prompt with user input
    response = model.generate_content(prompt)
    response_text = response.candidates[0].content.parts[0].text
    
    # Check if the user is asking about how to apply for an Ayush license
    if "apply for ayush license" in user_input.lower():
        response_text += "\n\nYou can apply for an Ayush license here: [e-Aushadhi](https://e-aushadhi.gov.in/login)"
    
    return response_text

# Define the input prompt for the chatbot
input_prompt = """Hello, welcome to the world of AYUSH!
The Ayush Department Chatbot is an interactive AI-driven assistant designed to provide accurate, real-time information about Ayurveda, homeopathy, and other natural medical sciences. Built using Django and powered by the Gemini API, this chatbot is tailored to support startups and professionals within the Ayush sector by answering questions, offering guidance on traditional practices, and providing insights into natural medicine.


Key features include:
- Use emojis when interacting with users. Don't provide useless information.
- Intelligent Responses: The chatbot leverages advanced AI to understand and respond to user queries related to various aspects of natural medicine.
- User-Friendly Interface: A simple, intuitive web interface that allows users to engage with the chatbot effortlessly.
- Real-Time Interaction: Instantaneous feedback and responses, making the chatbot a reliable resource for quick information.
- Secure and Scalable: Deployed on a robust server environment, ensuring security and scalability to handle multiple users simultaneously.

Don't include this in intro 
IF  anyone asks how to apply for an Ayush license, provide them with the link to [e-Aushadhi](https://e-aushadhi.gov.in/login) as a clickable hyperlink along with the Gemini response.
"""

# Initialize a list to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input from the user
question = st.chat_input("Ask your question:")

# Display the response in chat format
if question:
    # Get the response from the Gemini API
    response = get_gemini_response(question)
    
    # Add the user's question and the bot's response to the chat history
    st.session_state.chat_history.append({"user": question, "bot": response})
    
    # Display the chat history in a chat-like format with styled containers
    for chat in st.session_state.chat_history:
        with st.container():
            st.markdown(f"<div style='background-color: #1e1e1e; color: #ffffff; padding: 10px; border-radius: 5px;'><b>User:</b> {chat['user']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #2e2e2e; color: #ffffff; padding: 10px; border-radius: 5px; margin-top: 5px;'><b>Bot:</b> {chat['bot']}</div>", unsafe_allow_html=True)
