from flask import Flask, render_template, request
from youtube_search import YoutubeSearch
import json
import yt_dlp

baseyturl = (f"https://youtube.com/watch?v=")
baseimgurl = (f"https://i.ytimg.com/vi/")

app = Flask(__name__)

def get_data(query):
    name = query.replace("%20", " ")
    res = YoutubeSearch(name, max_results=10).to_json()
    results = json.loads(res)

    videos = results["videos"]
    
    ytdl_opts = {'format': 'bestaudio'}

    vid0 = videos[0]
    con0 = vid0["title"]
    url0 = baseyturl+vid0["id"]
    img0 = baseimgurl+vid0["id"]+"/default.jpg"
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf0 =  ydl.extract_info(url0, download=False)
        hre0 = inf0["url"]
        
    vid1 = videos[1]
    con1 = vid1["title"]
    url1 = baseyturl+vid1["id"]
    img1 = baseimgurl+vid1["id"]+"/default.jpg"
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf1=  ydl.extract_info(url1, download=False)
        hre1 = inf1["url"]

    vid2 = videos[2]
    con2 = vid2["title"]
    url2 = baseyturl+vid2["id"]
    img2 = baseimgurl+vid2["id"]+"/default.jpg"
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf2 =  ydl.extract_info(url2, download=False)
        hre2 = inf2["url"]

    vid3 = videos[3]
    con3 = vid3["title"]
    url3 = baseyturl+vid3["id"]
    img3 = baseimgurl+vid3["id"]+"/default.jpg"
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf3 =  ydl.extract_info(url3, download=False)
        hre3 = inf3["url"]

    vid4 = videos[4]
    con4 = vid4["title"]
    url4 = baseyturl+vid4["id"]
    img4 = baseimgurl+vid4["id"]+"/default.jpg"
    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        inf4 =  ydl.extract_info(url4, download=False)
        hre4 = inf4["url"]

    return (con0,hre0,con1,hre1,con2,hre2,con3,hre3,con4,hre4,img0,img1,img2,img3,img4)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("sear")
        return search(query) 

    return render_template("index.html")

def search(query):
    try:
        s = get_data(query)
        con0 = s[0]
        con1 = s[2]
        con2 = s[4]
        con3 = s[6]
        con4 = s[8]
        hre0 = s[1]
        hre1 = s[2]
        hre2 = s[3]
        hre3 = s[4]
        hre4 = s[5]
        img0 = s[9]
        img1 = s[10]
        img2 = s[11]
        img3 = s[12]
        img4 = s[13]
        return render_template("results.html", search=query, c0=con0, h0=hre0, c1=con1, h1=hre1, c2=con2, h2=hre2, c3=con3, h3=hre3, c4=con4, h4=hre4, i0=img0, i1=img1, i2=img2, i3=img3, i4=img4)
    except:
        return "Internal Server Error!"    

if __name__ == "__main__":
    app.run(debug=True)
