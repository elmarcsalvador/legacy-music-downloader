from flask import Flask, render_template, request
from youtube_search import YoutubeSearch
import json
import yt_dlp

app = Flask(__name__)

BASE_YT_URL = "https://youtube.com/watch?v="
BASE_IMG_URL = "https://i.ytimg.com/vi/"

def get_data(query, limit=5):
    name = query.replace("%20", " ")
    res = YoutubeSearch(name, max_results=limit).to_json()
    results = json.loads(res)["videos"]

    ytdl_opts = {"format": "bestaudio"}
    output = []

    # Prepare metadata
    meta = []
    for vid in results[:limit]:
        vid_id = vid["id"]
        url = BASE_YT_URL + vid_id
        img = BASE_IMG_URL + vid_id + "/default.jpg"
        meta.append({"title": vid["title"], "url": url, "img": img})

    # Reuse one YDL instance for all videos
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        for m in meta:
            try:
                info = ydl.extract_info(m["url"], download=False)
                m["stream"] = info.get("url")
            except Exception as e:
                print(f"yt-dlp error for {m['url']}: {e}")
                m["stream"] = None
            output.append(m)

    return output

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("sear")
        return search(query)
    return render_template("index.html")

def search(query):
    try:
        results = get_data(query)
        return render_template("results.html", search=query, results=results)
    except Exception as e:
        print("Error in search:", e)
        return "Internal Server Error!"

if __name__ == "__main__":
    app.run(debug=True)
