import openai
import os 

# Initialize OpenAI API key 
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set a default context for the chatGPT 
CONTEXT = "You are a yoda AI assistant." 

class Yoda():
    """
    A chatbot object that impersonates Yoda using OpenAI's GPT model.
    """

    def __init__(self, context = CONTEXT):
        """
        Initialize the Yoda bot with a context and a list to keep track of the conversation.
        
        Args:
            context (str): The initial context setting for the chatbot.
        """
        # Setting the context
        self.context = CONTEXT

        # A list to store the conversation history
        self.convo = [{"role": "system", "content": self.context }]

        # Model to use for OpenAI API
        self.model = "gpt-3.5-turbo"

    def ask_yoda(self, question): 
        """
        Simulate asking Yoda a question.
        
        Args:
            question (str): The question to ask Yoda.
            
        Returns:
            str: Yoda's answer.
        """
        # Add the user's question to the conversation history
        self.convo.append({"role":"user", "content":question})

        # Send the conversation history to the OpenAI API
        chat = openai.ChatCompletion.create(
            model=self.model,
            messages=self.convo
        )

        # Extract Yoda's response
        output = chat["choices"][0]["message"]["content"]

        # Add Yoda's response to the conversation history 
        self.convo.append({"role":"system", "content":output})

        return output
