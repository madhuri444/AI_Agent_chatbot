import streamlit as st 
import requests
st.set_page_config(page_title="Langgraph agent UI",layout="centered")

API_URL = "http://127.0.0.1:8000/chat"

st.title("AI AGENT")
st.write("Interact with langgraph based AI agents")

MODEL_NAMES= [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
    ]

input_prompt =  st.text_area("Define your AI agent",height=150,placeholder="Type your system prompt here")
selected_model = st.selectbox("Select models", MODEL_NAMES)
user_input=  st.text_area("Define your AI agent",height=150,placeholder="Type your query here")

if st.button("Send Query"):
    if user_input.strip():
        try:
            payload = {
                "model_name":selected_model, "system_prompt":input_prompt,"messages":[user_input]
            }
            response = requests.post(API_URL,json=payload)
            
            if response.status_code == 200:
                response_data=response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    ai_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]
                    
                    if ai_responses:
                        st.subheader("Agent Response:")
                        st.markdown(f"**Final Response:** {ai_responses[-1]}")
                    else:
                        st.warning("No AI response found in the agent output.")
            else:
                st.error(f"Request failed with status code {response.status_code}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking 'Send Query'.")   
                
                
                
    