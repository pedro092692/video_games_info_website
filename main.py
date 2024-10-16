from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

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

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('search')
    if query != '':
        results = video_games.search_game(query=query, limit=5)
        if turbo.can_stream():
            return turbo.stream([
                turbo.update(render_template('/includes/results.html', content=results),
                             target="results")
            ])

    return redirect(url_for('home'))


@app.route('/game/<game_id>', methods=['GET'])
def game(game_id):
    game_info = video_games.get_game_info(game_id=game_id)
    return render_template('game.html', game_info=game_info[0])


# run app
if __name__ == "__main__":
    app.run(debug=True)