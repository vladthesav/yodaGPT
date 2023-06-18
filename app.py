from flask import Flask, request, render_template, abort
from sessions import SessionManager 
import os

# Initialize SessionManager and start cleanup thread
sessions = SessionManager().start()

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template("index.html")

@app.route('/respond')
def respond():
    """
    Handle a GET request to respond to a user message.

    Request should contain "session_id" and "message" as query parameters.
    """
    # Ensure the request contains necessary data
    session_id = request.args.get('session_id')
    message = request.args.get('message')

    if session_id is None: abort(400, description="Missing parameter: 'session_id'")
    if message is None: abort(400, description="Missing parameter: 'message'")

    # Get a response from Yoda and return it
    response = sessions.chat(session_id, message)

    return response

@app.route("/make_session")
def make_session():
    """
    Handle a GET request to create a new chat session.

    Returns the ID of the new session.
    """
    session_id = sessions.start_session() 

    return session_id

if __name__ == '__main__':

    #get configs from environment vars 
    env_vars = os.environ 

    #don't run in debug mode if running in container - we set this env variable when building it
    debug = False if "container" in env_vars else True
    print("debug mode = ",debug)

    app.run(debug=debug, port=2000,host='0.0.0.0')