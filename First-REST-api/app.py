from flask import Flask

app = Flask(__name__) #__name__ provides a unique name to this Flask app object

@app.route('/') # the top-level endpoint
def home():
  return "Hello World!"

app.run(port=5000)