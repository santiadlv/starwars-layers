import os
import asyncio
import requests
from flask import Flask, request, jsonify

from .controller import sort_by_id, get_all_movie_character_names


port = int(os.environ['PORT'])
movie_url = os.environ['API_URL']

app = Flask(__name__)

@app.route("/", methods=['GET'])
def list_movies():
    response = requests.get(movie_url).json()
    movies = [{"id": movie['episode_id'], "name": movie['title']} for movie in response['results']]
    sort_by_id(movies)
    return jsonify(movies)

@app.route("/characters", methods=['GET'])
def list_movie_characters():
    movie_id = request.args.get('id', default=1)
    response = requests.get(f'{movie_url}{movie_id}').json()
    character_urls = response['characters']
    character_list = asyncio.run(get_all_movie_character_names(character_urls))
    return jsonify({ 'movie_id': movie_id, 'title': response['title'], 'characters': character_list })

if __name__ == "__main__":
    print(f'Application listening on port {port}')
    app.run(host="0.0.0.0", debug=True, port=port)
