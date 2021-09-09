# PyYouTube 


Get Video Data from YouTube link 

## Installation 
```bash
pip install PyYouTube
```

## How to use it ?
#### Get Videos Data 

```python
from pyyoutube import Data
yt = Data("https://youtu.be/HhHzCfrqsoE")
print(yt.data())
```
<details>
  <summary><b>Example Results</summary>
<br/>

```json
{
  "id": "HhHzCfrqsoE",
  "title": "How To Create MongoDB Database  Url",
  "thumbnails": "https://i.ytimg.com/vi/HhHzCfrqsoE/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==\\u0026rs=AOn4CLBOkJZAdEpYxQOVdaUxFHdbThH_DQ",
  "views": "91",
  "likes": "11",
  "dislikes": "No",
  "publishdate": "2021-08-04",
  "category": "Howto \\u0026 Style",
  "channel_name": "Ln Technical",
  "subscriber": "1.15K subscribers"
}
```

</details>

#### Get Youtube Url
  Get video url
```python
from pyyoutube import ytdl
video = ytdl("https://youtu.be/7BX0paTfllI")
print(video.url(itag = '18'))
```
  Get formats 
```python
from pyyoutube import ytdl
video = ytdl("https://youtu.be/7BX0paTfllI")
print(video.formats())
```
<details>
  <summary>Example Results</summary>
<br/>
  
```bash
['139 - audio only (DASH audio)', '140 - audio only (tiny)', '251 - audio only (tiny)', '278 - 256x144 (DASH video)', '160 - 256x144 (DASH video)', '242 - 426x240 (DASH video)', '133 - 426x240 (DASH video)', '134 - 640x360 (360p)', '243 - 640x360 (DASH video)', '244 - 854x480 (DASH video)', '135 - 854x480 (DASH video)', '247 - 1280x720 (DASH video)', '136 - 1280x720 (DASH video)', '137 - 1920x1080 (1080p)', '248 - 1920x1080 (DASH video)', '18 - 640x360 (360p)', '22 - 1280x720 (720p)']
```
</details>
 
#### Search Videos
 Get videos link 
```python 
from pyyoutube import Search
yt = Search("ln technical")
print(yt.videos())
```
<details>
  <summary><b>Example Results</summary>
<br/>

```bash
['https://youtu.be/jEnlga0hYyY', 'https://youtu.be/jEnlga0hYyY', 'https://youtu.be/Fxj5ZpaNq24', 'https://youtu.be/bAyh6FU01ho', 'https://youtu.be/DPCN3abXmsc', 'https://youtu.be/ros6m2BBI84', 'https://youtu.be/jEnlga0hYyY', 'https://youtu.be/hbtfaAx4bBE', 'https://youtu.be/qvBt04Q60Mg', 'https://youtu.be/1T3rAZH4rmw']
```

</details>

 Get Video Data 
```python 
from pyyoutube import Search, Data 
yt = Search("ln technical" , limit = 2).videos()
for vid in yt:
  res = Data(vid)
  print(res.data())
```
<details>
  <summary>Example Results</summary>
<br/>

```json
[
  {
    "id": "jEnlga0hYyY",
    "title": "Tutorial 1 - History of Infor ERP LN",
    "thumbnails": "https://i.ytimg.com/vi/jEnlga0hYyY/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==\\u0026rs=AOn4CLC9vnXpG2XmDpNfwZHEBMdo8GVf-A",
    "views": "9957",
    "likes": "80",
    "dislikes": "1",
    "publishdate": "2017-11-07",
    "category": "Education",
    "channel_name": "Infor LN Technical Trainer",
    "subscriber": "935 subscribers"
  },
  {
    "id": "jEnlga0hYyY",
    "title": "Tutorial 1 - History of Infor ERP LN",
    "thumbnails": "https://i.ytimg.com/vi/jEnlga0hYyY/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==\\u0026rs=AOn4CLC9vnXpG2XmDpNfwZHEBMdo8GVf-A",
    "views": "9957",
    "likes": "80",
    "dislikes": "1",
    "publishdate": "2017-11-07",
    "category": "Education",
    "channel_name": "Infor LN Technical Trainer",
    "subscriber": "935 subscribers"
  }
]
```
</details>

#### Search Limits Video 
```python 
from pyyoutube import Search, Data 
yt = Search("ln technical", limit = 3)
print(yt.videos())
```
<details>
  <summary>Example Results</summary>
<br/>
  
```
['https://youtu.be/jEnlga0hYyY', 'https://youtu.be/jEnlga0hYyY', 'https://youtu.be/Fxj5ZpaNq24']
```
</details>

## License 
Copyright (c) 2021 Lntechnical

This repository is licensed under the MIT license.
