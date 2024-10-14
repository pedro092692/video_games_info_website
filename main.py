from flask import Flask, render_template, url_for
from video_game_info import VideoGame


# setup app
app = Flask(__name__)
video_games = VideoGame()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')



# run app
if __name__ == "__main__":
    app.run(debug=True)