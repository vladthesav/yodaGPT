from threading import Thread
from yoda import *

import random
import string 
import time


def random_string(n=12):
    #create random string to use as session id
    return ''.join(random.choices(string.ascii_lowercase +string.digits, k=n))

class SessionManager():
    """very crude session manager"""
    def __init__(self, timeout=3000):

        #keep track of sessions
        self.sessions = {}

        #ger rid of stale sessions
        self.timeout = timeout

        self.stopped=False

    def start(self):
        Thread(target=self.cleanup, args=()).start()
        return self

    def cleanup(self):
        #get rid of sessions that timed out
        while not self.stopped:
            
            #look at every session and see when the user last interacted with it
            current_time = time.time()

            for chat_id in list(self.sessions.keys()): 

                #see when they last interacted with it
                last_heard_from = current_time - self.sessions[chat_id]["last_interacted_with"]

                if last_heard_from < self.timeout: continue 

                #remove stale sessions 
                self.end_session(chat_id)


    def start_session(self):
        #start a chat session 

        #create a unique key for session
        key = random_string()

        #if this key is already in use, find another one that isn't 
        while key in self.sessions: key = random_string()

        #create new session
        self.sessions[key] = {"chat":Yoda(), "last_interacted_with": time.time()}
        
        #return session id 
        return key


    def chat(self, chat_id, prompt):
        #send API request to chatgpt
        if chat_id not in self.sessions: 
            print("error: session {} not found".format(chat_id))
            return ""

        #get chat session
        session = self.sessions[chat_id]
        print(session)
        #ask the wise one
        response = session["chat"].ask_yoda( prompt)

        #update last time user did anything
        session["last_interacted_with"]=time.time()

        return response


    def end_session(self, chat_id):
        #kill session 

        #if session doesn't exist, stop here
        if chat_id not in self.sessions: return

        #delete session data from table 
        del self.sessions[chat_id]

        return


    def stop(self):
        self.stopped = True