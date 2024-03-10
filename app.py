from flask import Flask

# Creating a Flask app instance
app = Flask(__name__)

# Defining a route for the home page
@app.route('/')
def home():
    return 'Welcome to my DevOpsWebServer!'

# Running the app
if __name__ =='__main__':
    app.run(debug=True)
