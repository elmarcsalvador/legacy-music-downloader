from flask import Flask
from youtube_search import YoutubeSearch
import json
import yt_dlp

baseyturl = (f"https://youtube.com/watch?v=")

app = Flask(__name__)

@app.route("/")
def home():
    return "ahh $hit, here we go again!"

@app.route("/<query>")
def unknown(query):
    name = query.replace("%20", " ")
    res = YoutubeSearch(name, max_results=10).to_json()
    results = json.loads(res)

    titlelist = []
    urllist = []
    durationlist = []

    videos = results["videos"]

    for i in range(10):
        vid = videos[i]
        title = vid["title"]
        duration = vid["duration"]
        id = vid["id"]
        url = baseyturl + id
        titlelist.append(title)
        durationlist.append(duration)
        urllist.append(url)
    return f"{titlelist} \n{urllist} \n{durationlist}"

    #video0 = videos[0]
    #ID0 = video0["id"]
    #title0 = video0["title"]
    #duration0 = video0["duration"]
    #yturl0 = baseyturl + ID0
    #return name


if __name__ == "__main__":
    app.run(debug=True)
