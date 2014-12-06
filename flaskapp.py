from flask import Flask
app = Flask("first app")

@app.route('/')

def index():
     return "flask app"

if __name__ == "__main__":
     app.run()
