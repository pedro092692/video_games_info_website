from flask import Flask, render_template, url_for
from video_game_info import VideoGame
from turbo_flask import Turbo


# setup app
app = Flask(__name__)
video_games = VideoGame()
# turbo
turbo = Turbo(app)

@app.route('/', methods=['GET'])
def home():
    popular_games = video_games.popular_games(limit=4)
    # popular_games = []
    return render_template('index.html', popular_games=popular_games)



# run app
if __name__ == "__main__":
    app.run(debug=True)