import openai
import requests 
import os 

#get api key 
openai.api_key = os.getenv("OPENAI_API_KEY")

class Yoda():
    def __init__(self):
        #tell chatbot what to do 
        self.context = "You are a yoda AI assistant" 

        #keep track of convo
        self.convo = [{"role": "system", "content": self.context }]

        #what llm to use 
        self.model="gpt-3.5-turbo"

    def ask_yoda(self, question): 
        #append input to messages
        self.convo.append({"role":"user", "content":question})

        chat = openai.ChatCompletion.create(
            model=self.model,
            messages=self.convo
            )

        output = chat["choices"][0]["message"]["content"]

        #append output to history 
        self.convo.append({"role":"system", "content":output})

        return output

    


