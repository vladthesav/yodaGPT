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


if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Greetings, young one. How may I be of assistance to you today?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Greetings master yoda"]


#input_container = st.container()
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
yoda = Yoda()
def generate_response(prompt):
    response = yoda.ask_yoda(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))