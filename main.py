#Importing Required Modules
from youtube_search import YoutubeSearch
import json
import os
import yt_dlp

#Song/Music Search Function
name = str(input("enter song name -> "))
res = YoutubeSearch(name, max_results=10).to_json()
results = json.loads(res)

#Base Youtube URL For Making Complete URL's
baseyturl = (f"https://youtube.com/watch?v=")

#Spacer/Designer
print("---------------------------------------------------------")
print("-------------------------Results-------------------------")
print("---------------------------------------------------------")

#Video - 0 | Results
videos = results["videos"]
video0 = videos[0]
ID0 = video0["id"]
title0 = video0["title"]
duration0 = video0["duration"]
yturl0 = baseyturl + ID0
print(f"[0]: {title0} \n{yturl0} \n{duration0}")

#Spacer
print("---------------------------------------------------------")

#Video - 1 | Results
videos = results["videos"]
video1 = videos[1]
ID1 = video1["id"]
title1 = video1["title"]
duration1 = video1["duration"]
yturl1 = baseyturl + ID1
print(f"[1]: {title1} \n{yturl1} \n{duration1}")

#Spacer
print("---------------------------------------------------------")

#Video - 2 | Results
videos = results["videos"]
video2 = videos[2]
ID2 = video2["id"]
title2 = video2["title"]
duration2 = video2["duration"]
yturl2 = baseyturl + ID2
print(f"[2]: {title2} \n{yturl2} \n{duration2}")

#Spacer
print("---------------------------------------------------------")

#Video - 3 | Results
videos = results["videos"]
video3 = videos[3]
ID3 = video3["id"]
title3 = video3["title"]
duration3 = video3["duration"]
yturl3 = baseyturl + ID3
print(f"[3]: {title3} \n{yturl3} \n{duration3}")

#Spacer
print("---------------------------------------------------------")

#Video - 4 | Results
videos = results["videos"]
video4 = videos[4]
ID4 = video4["id"]
title4 = video4["title"]
duration4 = video4["duration"]
yturl4 = baseyturl + ID4
print(f"[4]: {title4} \n{yturl4} \n{duration4}")

#Spacer
print("---------------------------------------------------------")

#Video - 5 | Results
videos = results["videos"]
video5 = videos[5]
ID5 = video5["id"]
title5 = video5["title"]
duration5 = video5["duration"]
yturl5 = baseyturl + ID5
print(f"[5]: {title5} \n{yturl5} \n{duration5}")

#Spacer
print("---------------------------------------------------------")

#Video - 6 | Results
videos = results["videos"]
video6 = videos[6]
ID6 = video6["id"]
title6 = video6["title"]
duration6 = video6["duration"]
yturl6 = baseyturl + ID6
print(f"[6]: {title6} \n{yturl6} \n{duration6}")

#Spacer
print("---------------------------------------------------------")

#Video - 7 | Results
videos = results["videos"]
video7 = videos[7]
ID7 = video7["id"]
title7 = video7["title"]
duration7 = video7["duration"]
yturl7 = baseyturl + ID7
print(f"[7]: {title7} \n{yturl7} \n{duration7}")

#Spacer
print("---------------------------------------------------------")

#Video - 8 | Results
videos = results["videos"]
video8 = videos[8]
ID8 = video8["id"]
title8 = video8["title"]
duration8 = video8["duration"]
yturl8 = baseyturl + ID8
print(f"[8]: {title8} \n{yturl8} \n{duration8}")

#Spacer
print("---------------------------------------------------------")

#Video - 9 | Results
videos = results["videos"]
video9 = videos[9]
ID9 = video9["id"]
title9 = video9["title"]
duration9 = video9["duration"]
yturl9 = baseyturl + ID9
print(f"[9]: {title9} \n{yturl9} \n{duration9}")

#Spacer
print("---------------------------------------------------------")

#Function For Selecting Song/Music
print("\n\n\n---------------- \nSelect The Song \n----------------")
sel = str(input("-> "))
if "0" in sel:
    url = yturl0
elif "1" in sel:
    url = yturl1
elif "2" in sel:
    url = yturl2
elif "3" in sel:
    url = yturl3
elif "4" in sel:
    url = yturl4
elif "5" in sel:
    url = yturl5
elif "6" in sel:
    url = yturl6
elif "7" in sel:
    url = yturl7
elif "8" in sel:
    url = yturl8
elif "9" in sel:
    url = yturl9
else:
    print("Invaild Number Chosen!")
    print("----------------------")
    print("Please Try Again  [:(]")
    
ytdl_opts = {'format': 'bestaudio'}
with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
    info =  ydl.extract_info(url, download=False)

    print(info["url"])
