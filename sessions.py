from threading import Thread
from yoda import *

import random
import string 
import time


def random_string(n=12):
    """
    Generate a random string of a given length.

    Args:
        n (int): The desired length of the string.

    Returns:
        str: A random alphanumeric string.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))


class SessionManager():
    """
    A class to manage multiple chat sessions with the Yoda chatbot.
    """
    def __init__(self, timeout=3000):
        """
        Initialize the SessionManager.

        Args:
            timeout (int): The time in seconds after which a session is considered stale and removed.
        """
        self.sessions = {}  # A dict to store all active sessions
        self.timeout = timeout  # The timeout to consider a session as stale
        self.stopped = False  # A flag to indicate whether the session manager should stop

    def start(self):
        """
        Start the session manager.
        """
        Thread(target=self.cleanup).start()
        return self

    def cleanup(self):
        """
        Periodically remove sessions that are stale (i.e., haven't been interacted with in a while).
        """
        while not self.stopped:
            current_time = time.time()

            # Check all sessions for staleness
            for chat_id in list(self.sessions.keys()): 
                last_interacted_with = current_time - self.sessions[chat_id]["last_interacted_with"]

                # If the session is stale, remove it
                if last_interacted_with > self.timeout:
                    self.end_session(chat_id)

    def start_session(self):
        """
        Start a new chat session with Yoda.

        Returns:
            str: The ID of the new session.
        """
        key = random_string()

        # Ensure the session ID is unique
        while key in self.sessions:
            key = random_string()

        # Create the new session
        self.sessions[key] = {"chat": Yoda(), "last_interacted_with": time.time()}

        return key

    def chat(self, chat_id, prompt):
        """
        Ask a question to Yoda in a particular chat session.

        Args:
            chat_id (str): The ID of the chat session.
            prompt (str): The question to ask Yoda.

        Returns:
            str: Yoda's answer, or an empty string if the session ID was not found.
        """
        if chat_id not in self.sessions: 
            print(f"Error: session {chat_id} not found.")
            return ""

        #get chat session
        session = self.sessions[chat_id]

        #get API response
        response = session["chat"].ask_yoda(prompt)

        # Update the session to reflect that it's just been interacted with
        session["last_interacted_with"] = time.time()

        return response

    def end_session(self, chat_id):
        """
        End a specific chat session.

        Args:
            chat_id (str): The ID of the session to end.
        """
        # Ignore invalid session IDs
        if chat_id not in self.sessions: return

        #delete session
        del self.sessions[chat_id]

    def stop(self):
        """
        Stop the session manager.
        """
        self.stopped = True