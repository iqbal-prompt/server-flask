from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Halo dari Flask di Render!'

if __name__=="__main__":
    app.run(debug=True)
    