from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def search_track(query):
    url = f"https://itunes.apple.com/search?term={query}&entity=song"
    response = requests.get(url)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        track = data["results"][0]
        return {
            "artist": track["artistName"],
            "track": track["trackName"],
            "album": track["collectionName"],
            "price": track["trackPrice"]
        }
    else:
        return {
            "artist": "N/A",
            "track": "N/A",
            "album": "N/A",
            "price": "N/A"
        }

@app.route('/', methods=['GET', 'POST'])
def index():
    track_info = None
    if request.method == 'POST':
        query = request.form['query']
        track_info = search_track(query)
    return render_template('index.html', track_info=track_info)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    track_info = search_track(query)
    return jsonify(track_info)

if __name__ == '__main__':
    app.run(debug=True)
