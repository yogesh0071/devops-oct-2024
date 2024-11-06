import os
from flask import Flask

app = Flask(__name__)

# take value of env variable
who_to_greet = os.environ.get("who_to_greet_env_var")

@app.get("/")
def get_greetings():
    greet_message = f"Hi {who_to_greet} , This is coming from container, Welcome to container world, again"
    return greet_message, 200

