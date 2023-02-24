# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import os
# Flask constructor takes the name of
# current module (_name_) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
            return '<h1>HELLO WORLD! Version 1</h1>'
# main driver function
if __name__ == '__main__':

  flask_port = os.getenv('FLASK_PORT')
# run() method of Flask class runs the application
# on the local development server.
  app.run(host='0.0.0.0', port=flask_port)
