# PyYouTube 


Get Video Data from YouTube link 

## Installation 
```bash
pip install py-youtube
```

## How to use it ?
#### Get Videos Data 

```python
from py_youtube import Data
data = Data("https://youtu.be/HhHzCfrqsoE").data()
print(data)
```
<details>
  <summary><b>Example Results</summary>
<br/>

```json
{
  'id': 'HhHzCfrqsoE',
   'title': 'How To Create MongoDB Database  Url', 
   'thumbnails': 'https://i.ytimg.com/vi/HhHzCfrqsoE/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==\\u0026rs=AOn4CLBOkJZAdEpYxQOVdaUxFHdbThH_DQ',  
   'views': '709', 
   'likes': '27', 
   'dislikes': '1', 
   'publishdate': '2021-08-04', 
   'category': 'Howto \\u0026 Style', 
   'channel_name': 'Ln Technical', 
   'subscriber': '1.67K', 
   'keywords': 'video, sharing, camera phone, video phone, free, upload'
}
```

</details>

 
## Search Videos
 Search video Data
```python 
from py_youtube import Search
videos = Search("ln technical").videos()
print(videos)
```
<details>
  <summary><b>Example Results</summary>
<br/>

```json
[
  {
    "id": "7BX0paTfllI",
    "title": "How To Create Advance Google Translater Telegram Bot",
    "thumb": [
      "https://i.ytimg.com/vi/7BX0paTfllI/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLCxWsEz6p7P9KVh72YQ-qK_m1bWKg",
      "https://i.ytimg.com/vi/7BX0paTfllI/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDgD8dPi-IO2WZ9RXbdRMV7eS-Afg"
    ],
    "simple_data": "How To Create Advance Google Translater Telegram Bot by Ln Technical 2 weeks ago 9 minutes, 34 seconds 311 views"
  },
  {
    "id": "MzAuQ7DBJtw",
    "title": "python India flag \ud83c\uddee\ud83c\uddf3",
    "thumb": [
      "https://i.ytimg.com/vi/MzAuQ7DBJtw/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLAltEKI5zBWmhxJwk0egXWp0iN9fQ",
      "https://i.ytimg.com/vi/MzAuQ7DBJtw/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBjbeyE6dgtTd5wrfs9PSD7t2Tt8g"
    ],
    "simple_data": "python India flag \ud83c\uddee\ud83c\uddf3 by Ln Technical 2 weeks ago 30 seconds 80 views"
  },
  {
    "id": "vmnRD2XMRs8",
    "title": "How to create your own telgram  welcome message bot",
    "thumb": [
      "https://i.ytimg.com/vi/vmnRD2XMRs8/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLD3u4JNQFxHXYiSqZRPO823XsLjfw",
      "https://i.ytimg.com/vi/vmnRD2XMRs8/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBI67RS_CC0yNO28MdZmP8H_dkBhg"
    ],
    "simple_data": "How to create your own telgram  welcome message bot by Ln Technical 4 months ago 6 minutes, 58 seconds 699 views"
  },
  {
    "id": "HQhVmxcW0zk",
    "title": "How to translate one language to another language in telegram",
    "thumb": [
      "https://i.ytimg.com/vi/HQhVmxcW0zk/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLB5SSaS9Szv5zVOpAENYAeesr8PjQ",
      "https://i.ytimg.com/vi/HQhVmxcW0zk/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBYi_pd4jy7ZlDbIAwCpkpviuWBfA"
    ],
    "simple_data": "How to translate one language to another language in telegram by Ln Technical 1 year ago 1 minute, 52 seconds 4,315 views"
  },
  {
    "id": "3GdY1fgpkZw",
    "title": "How to create movie app in 10minutes",
    "thumb": [
      "https://i.ytimg.com/vi/3GdY1fgpkZw/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLCyNx5lMXzIhIqhVzdieKSGi07ZcA",
      "https://i.ytimg.com/vi/3GdY1fgpkZw/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLAspgwRstQ0dfyaAq5OtTHIhsx6Ig"
    ],
    "simple_data": "How to create movie app in 10minutes by Ln Technical 1 year ago 10 minutes, 20 seconds 3,932 views"
  },
  {
    "id": "nTvXhzyfjUA",
    "title": "How to upload movie on telegram",
    "thumb": [
      "https://i.ytimg.com/vi/nTvXhzyfjUA/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLA3RbLNoAjtSIXtdF3yhUwPMxHo9A",
      "https://i.ytimg.com/vi/nTvXhzyfjUA/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLARfj5VghkZOPgQZWKvQaRzATC2pg"
    ],
    "simple_data": "How to upload movie on telegram by Ln Technical 1 year ago 6 minutes, 9 seconds 2,145 views"
  },
  {
    "id": "62AD0LXy8Cg",
    "title": "LNMIIT Jaipur\ud83d\udd25| 60 LAKH CSE PACKAGE\ud83d\ude0d| Best Coders in India?| Cutoff |College Review[2020]\ud83d\ude31",
    "thumb": [
      "https://i.ytimg.com/vi/62AD0LXy8Cg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLDkxWB3u8NHZPb1S2mGAHS09SmrRQ",
      "https://i.ytimg.com/vi/62AD0LXy8Cg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBmt1DuV0s2yZ-jT9x5fmH6utpxRA"
    ],
    "simple_data": "LNMIIT Jaipur\ud83d\udd25| 60 LAKH CSE PACKAGE\ud83d\ude0d| Best Coders in India?| Cutoff |College Review[2020]\ud83d\ude31 by Yash Garg 1 year ago 13 minutes, 25 seconds 151,422 views"
  },
  {
    "id": "gAB2S65nuTE",
    "title": "Home Made OREO Cake | \u0d13\u0d35\u0d7b \u0d07\u0d32\u0d4d\u0d32\u0d3e\u0d24\u0d46 \u0d05\u0d1f\u0d3f\u0d2a\u0d4a\u0d33\u0d3f \u0d13\u0d31\u0d3f\u0d2f\u0d4b  \u0d15\u0d47\u0d15\u0d4d\u0d15\u0d4d | M4 Tech |",
    "thumb": [
      "https://i.ytimg.com/vi/gAB2S65nuTE/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLClVZHg9Z3ew2pVGp5a_TfKHoWpCQ",
      "https://i.ytimg.com/vi/gAB2S65nuTE/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBNqsV3CmjOPD5g9IqXP5An-SxoKw"
    ],
    "simple_data": "Home Made OREO Cake | \u0d13\u0d35\u0d7b \u0d07\u0d32\u0d4d\u0d32\u0d3e\u0d24\u0d46 \u0d05\u0d1f\u0d3f\u0d2a\u0d4a\u0d33\u0d3f \u0d13\u0d31\u0d3f\u0d2f\u0d4b  \u0d15\u0d47\u0d15\u0d4d\u0d15\u0d4d | M4 Tech | by M4 Tech 2 years ago 17 minutes 22,631,646 views"
  },
  {
    "id": "DPCN3abXmsc",
    "title": "Reduce ERP complexity and gain operational agility with Infor LN",
    "thumb": [
      "https://i.ytimg.com/vi/DPCN3abXmsc/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLAAATsQHYFf7tWkurzhkXvWn4hZSg",
      "https://i.ytimg.com/vi/DPCN3abXmsc/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDhgdw9ErkUKxhpNAMcqywHTxusiw"
    ],
    "simple_data": "Reduce ERP complexity and gain operational agility with Infor LN by Infor 9 months ago 1 minute, 56 seconds 2,307 views"
  },
  {
    "id": "LxfBzrs6kWk",
    "title": "Post Chemotherapy Robot Assisted Bilateral Radical Inguinal L. N. D: Technical Feasibility",
    "thumb": [
      "https://i.ytimg.com/vi/LxfBzrs6kWk/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLARUWxQ1Brgqz4I6AB5nyR90u8-ag",
      "https://i.ytimg.com/vi/LxfBzrs6kWk/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLAgofts4C7f53tTJWliVzTfG91XKA"
    ],
    "simple_data": "Post Chemotherapy Robot Assisted Bilateral Radical Inguinal L. N. D: Technical Feasibility by Vattikuti Foundation 7 months ago 7 minutes, 59 seconds 89 views"
  },
  {
    "id": "jEnlga0hYyY",
    "title": "Tutorial 1 - History of Infor ERP LN",
    "thumb": [
      "https://i.ytimg.com/vi/jEnlga0hYyY/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLBJreaRpSHpnuy9SJEcraXO711Nmw",
      "https://i.ytimg.com/vi/jEnlga0hYyY/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDMNZr_IMmpqPASvjDNaeJm3P0zxQ"
    ],
    "simple_data": "Tutorial 1 - History of Infor ERP LN by Infor LN Technical Trainer 3 years ago 2 minutes, 6 seconds 10,192 views"
  },
  {
    "id": "Yw3JZkP84cs",
    "title": "Is the stock market in a bubble right now - Valuation Guru Aswath Damodaran interview | Viral reacts",
    "thumb": [
      "https://i.ytimg.com/vi/Yw3JZkP84cs/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLBD5vMqQCO84TcNxEwpnrcW6k0s0g",
      "https://i.ytimg.com/vi/Yw3JZkP84cs/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLCDVQ_Y1bFKUivVoDCwLRhhkI_ayQ"
    ],
    "simple_data": "Is the stock market in a bubble right now - Valuation Guru Aswath Damodaran interview | Viral reacts by Groww 1 week ago 14 minutes, 50 seconds 120,029 views"
  },
  {
    "id": "h4C3BQ-JyHM",
    "title": "We Made Spiderman Shoes Using 12 Volt Battery",
    "thumb": [
      "https://i.ytimg.com/vi/h4C3BQ-JyHM/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLDmbvQkCVXKUrLRemJElZ8pU-k8jw",
      "https://i.ytimg.com/vi/h4C3BQ-JyHM/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBbpg9UYc3A7BAGxy7QPNSjngwr7w"
    ],
    "simple_data": "We Made Spiderman Shoes Using 12 Volt Battery by MR. INDIAN HACKER 4 months ago 10 minutes, 49 seconds 3,938,188 views"
  },
  {
    "id": "or9WCwvKgK4",
    "title": "Top 5 Reasons Why People Lose Money Trading Options | \u0932\u094b\u0917 Options  Trading \u092e\u0947\u0902 \u092a\u0948\u0938\u093e \u0915\u094d\u092f\u094b\u0902 \u0917\u0935\u093e\u0924\u0947 \u0939\u0948?",
    "thumb": [
      "https://i.ytimg.com/vi/or9WCwvKgK4/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLBB86Hexbh1-uD3zjlNQGwbcJx8XQ",
      "https://i.ytimg.com/vi/or9WCwvKgK4/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLAdF4mrAKZDtDZE9U0Iquae2alTpw"
    ],
    "simple_data": "Top 5 Reasons Why People Lose Money Trading Options | \u0932\u094b\u0917 Options  Trading \u092e\u0947\u0902 \u092a\u0948\u0938\u093e \u0915\u094d\u092f\u094b\u0902 \u0917\u0935\u093e\u0924\u0947 \u0939\u0948? by Kundan Kishore 1 week ago 15 minutes 13,971 views"
  },
  {
    "id": "XM3E4rv5pQM",
    "title": "BIG FISH FRY WITH BANANA LEAF - \u0d35\u0d32\u0d3f\u0d2f \u0d2e\u0d40\u0d7b \u0d35\u0d3e\u0d34\u0d2f\u0d3f\u0d32\u0d2f\u0d3f\u0d7d \u0d1a\u0d41\u0d1f\u0d4d\u0d1f\u0d24\u0d4d | Cooking Skill Village Food Channel",
    "thumb": [
      "https://i.ytimg.com/vi/XM3E4rv5pQM/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLDiczjhVetMrgEgAnTmnBidlrY9sA",
      "https://i.ytimg.com/vi/XM3E4rv5pQM/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLAFlrDtd9nIsi8URXQDQLBSVQXNHQ"
    ],
    "simple_data": "BIG FISH FRY WITH BANANA LEAF - \u0d35\u0d32\u0d3f\u0d2f \u0d2e\u0d40\u0d7b \u0d35\u0d3e\u0d34\u0d2f\u0d3f\u0d32\u0d2f\u0d3f\u0d7d \u0d1a\u0d41\u0d1f\u0d4d\u0d1f\u0d24\u0d4d | Cooking Skill Village Food Channel by Village Food Channel 2 years ago 11 minutes, 56 seconds 4,966,385 views"
  }
]
```

</details>

## Search Limits Video 
```python 
from py_youtube import Search ,Data 
videos = Search("ln technical", limit = 3).videos()
print(videos)
```
<details>
  <summary>Example Results</summary>
<br/>
  
``` json
[
  {
    "id": "7BX0paTfllI",
    "title": "How To Create Advance Google Translater Telegram Bot",
    "thumb": [
      "https://i.ytimg.com/vi/7BX0paTfllI/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLCxWsEz6p7P9KVh72YQ-qK_m1bWKg",
      "https://i.ytimg.com/vi/7BX0paTfllI/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDgD8dPi-IO2WZ9RXbdRMV7eS-Afg"
    ],
    "simple_data": "How To Create Advance Google Translater Telegram Bot by Ln Technical 2 weeks ago 9 minutes, 34 seconds 311 views"
  },
  {
    "id": "MzAuQ7DBJtw",
    "title": "python India flag \ud83c\uddee\ud83c\uddf3",
    "thumb": [
      "https://i.ytimg.com/vi/MzAuQ7DBJtw/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLAltEKI5zBWmhxJwk0egXWp0iN9fQ",
      "https://i.ytimg.com/vi/MzAuQ7DBJtw/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLBjbeyE6dgtTd5wrfs9PSD7t2Tt8g"
    ],
    "simple_data": "python India flag \ud83c\uddee\ud83c\uddf3 by Ln Technical 2 weeks ago 30 seconds 80 views"
  }
]
```
</details>

## License 
Copyright (c) 2021 Lntechnical

This repository is licensed under the MIT license.
