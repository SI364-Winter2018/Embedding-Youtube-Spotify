# https://developers.google.com/youtube/v3/docs/search/list

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/youtube')
def youtube():
    with open('youtube-data.json') as f:
        response_json = f.read()
        data = json.loads(response_json)

    items_to_embed = []
    for item in data['items']:
        if 'playlistId' in item['id']:
            item['url'] = 'http://www.youtube.com/embed/?listType=playlist&list={0}'.format(item['id']['playlistId'])
            items_to_embed.append(item)
        elif 'videoId' in item['id']:
            item['url'] = "http://www.youtube.com/embed/{0}".format(item['id']['videoId'])
            items_to_embed.append(item)

    return render_template('youtube.html', items_to_embed=items_to_embed, search_term="vox videos")


@app.route('/spotify')
def spotify():
    with open('spotify-data.json') as f:
        response_json = f.read()
        data = json.loads(response_json)

    items_to_embed = data["tracks"]["items"]
    for item in items_to_embed:
        item['url'] = 'https://open.spotify.com/embed?uri={0}'.format(item['uri'])

    return render_template('spotify.html', items_to_embed=items_to_embed, search_term="tania bowra")


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
