from flask import Flask, jsonify,request, render_template
from sessions import SessionManager 

import openai
import os

#keep track of chat sessions
sessions = SessionManager().start()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/respond')
def respond():
    # get response from ChatGPT

    #get session ID
    if "session_id" not in request.args: return "error: no session id found"
    session_id = request.args.get("session_id")
    #print("session_id= ",session_id)

    #get message 
    if "message" not in request.args: return "error: no message found"
    message = request.args.get("message")

    #ask yoda
    response = sessions.chat(session_id, message)

    return  response

@app.route("/make_session")
def make_session():
    #create chat session and return session id to keep track of it
    session_id = sessions.start_session() 

    return session_id

if __name__ == '__main__':

    #get configs from environment vars 
    env_vars = os.environ 

    #don't run in debug mode if running in container - we set this env variable when building it
    debug = False if "container" in env_vars else True
    print("debug mode = ",debug)

    app.run(debug=debug, port=2000,host='0.0.0.0')