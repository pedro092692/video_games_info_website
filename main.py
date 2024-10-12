from flask import Flask, render_template, url_for


# setup app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello world'



# run app
if __name__ == "__main__":
    app.run(debug=True)