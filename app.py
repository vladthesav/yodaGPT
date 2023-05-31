import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

from chat import *


st.set_page_config(page_title="yodaGPT - A chatGPT-powered yoda bot")


with st.sidebar:
    st.title('yodaGPT')
    st.markdown('''
    ## About
    This app is an chatGPT-powered yoda chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [OpenAI](<https://platform.openai.com/docs/introduction/overview>)
    
    💡 Note: OpenAI API key required
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [vladthesav](<https://github.com/vladthesav>)')

#init Yoda object to track convo and make API requests
if 'yoda' not in st.session_state: st.session_state['yoda'] = Yoda()


colored_header(label='', description='', color_name='blue-30')
response_container = st.container()
input_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

## Applying the user input box
with input_container: user_input = get_text()


# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    response = st.session_state['yoda'].ask_yoda(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:  

        #ask the wise one
        response = generate_response(user_input)

        if not st.session_state["yoda"]: pass

        convo = st.session_state["yoda"].convo
        for i, m in enumerate(convo): 

            #first item in convo is context for bot - ignore it
            if i==0: continue 

            is_user = m["role"]=="user"
            message(m["content"], key=str(i), is_user=is_user)
        