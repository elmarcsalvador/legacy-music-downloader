from flask import Flask, render_template
from youtube_search import YoutubeSearch
import json
import yt_dlp

baseyturl = (f"https://youtube.com/watch?v=")

app = Flask(__name__)

maincont = "<title>Legacy-Music-Downloader</title><h1>Welcome To LMD!</h1><br><p>To Use:- /{song-name}</p><br><p>Made With Love By @elmarcsalvador</p>"

@app.route("/")
def home():
    return maincont

@app.route("/<query>")
def unknown(query):
    name = query.replace("%20", " ")
    res = YoutubeSearch(name, max_results=10).to_json()
    results = json.loads(res)

    videos = results["videos"]
    
    ytdl_opts = {'format': 'bestaudio'}

    vid0 = videos[0]
    con0 = vid0["title"]
    url0 = baseyturl+vid0["id"]
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf0 =  ydl.extract_info(url0, download=False)
        hre0 = inf0["url"]
        
    vid1 = videos[1]
    con1 = vid1["title"]
    url1 = baseyturl+vid1["id"]
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf1=  ydl.extract_info(url1, download=False)
        hre1 = inf1["url"]

    vid2 = videos[2]
    con2 = vid2["title"]
    url2 = baseyturl+vid2["id"]
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf2 =  ydl.extract_info(url2, download=False)
        hre2 = inf2["url"]

    vid3 = videos[3]
    con3 = vid3["title"]
    url3 = baseyturl+vid3["id"]
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf3 =  ydl.extract_info(url3, download=False)
        hre3 = inf3["url"]

    vid4 = videos[4]
    con4 = vid4["title"]
    url4 = baseyturl+vid4["id"]
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf4 =  ydl.extract_info(url4, download=False)
        hre4 = inf4["url"]

    return render_template("page.html", search=query, c0=con0, h0=hre0, c1=con1, h1=hre1, c2=con2, h2=hre2, c3=con3, h3=hre3, c4=con4, h4=hre4)


if __name__ == "__main__":
    app.run(debug=True)
