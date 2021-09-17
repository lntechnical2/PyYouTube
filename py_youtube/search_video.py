"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""

"""
MIT License

Copyright (c) 2021 Lntechnical

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


# This Modules Helps To Get Youtube Video Data 


import re
import urllib.request
import json



class Search:
	
	def __init__(self,keywords:str , limit=15):
		
		search_keyword=keywords.replace(" ", "+")
		html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
		self.limit= limit
		self.source = html.read().decode('utf8')
		
		
	def videos(self):
		"""
		[
  {
    "id": "P1uHDPpe_04",
    "title": "Build language translator with 3 lines of python code",
    "thumb": [
      "https://i.ytimg.com/vi/P1uHDPpe_04/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLBffClhp28J0iQB2e8jtV_am6TO4g",
      "https://i.ytimg.com/vi/P1uHDPpe_04/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLAld_3eDi_itf1WQJ9rF7TmXLCJmA"
    ],
    "simple_data": "Build language translator with 3 lines of python code by codebasics 8 months ago 4 minutes, 58 seconds 21,386 views"
  },
  {
    "id": "mwq5-01z1U0",
    "title": "Create a Simple Language Translator Bot using Bot Builder SDK and Google Translation API",
    "thumb": [
      "https://i.ytimg.com/vi/mwq5-01z1U0/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLA6jeEFU7aMQqQNdwxoPf-IutXx8g",
      "https://i.ytimg.com/vi/mwq5-01z1U0/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDZoi0Vy4wS5peNhwfL2Idqkuptqg"
    ],
    "simple_data": "Create a Simple Language Translator Bot using Bot Builder SDK and Google Translation API by JD Bots 1 year ago 12 minutes, 55 seconds 594 views"
  },
  {
    "id": "PTAkiukJK7E",
    "title": "Creating a Telegram Bot in Python 3.9 Tutorial (Fast \\u0026 Easy)",
    "thumb": [
      "https://i.ytimg.com/vi/PTAkiukJK7E/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLB9N4Z0WpfElA6UVVk2A7ye54ZveQ",
      "https://i.ytimg.com/vi/PTAkiukJK7E/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLDOwR6QmwLlNIuvJSb4sRHQuH7L6Q"
    ],
    "simple_data": "Creating a Telegram Bot in Python 3.9 Tutorial (Fast \\u0026 Easy) by Code Palace 7 months ago 13 minutes, 7 seconds 64,519 views"
  },
  {
    "id": "I5iux1KXswk",
    "title": "how to translate any language on telegram app with translator bot on telegram - how to use telegram",
    "thumb": [
      "https://i.ytimg.com/vi/I5iux1KXswk/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLAWge1QJjpIuvKcVRBIlxgMU-1jig",
      "https://i.ytimg.com/vi/I5iux1KXswk/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLALlQl3kEP4oVN7JxnZH4D5JGualw"
    ],
    "simple_data": "how to translate any language on telegram app with translator bot on telegram - how to use telegram by TS Tech Talk 3 months ago 7 minutes, 24 seconds 7,771 views"
  },
  {
    "id": "CTwlDu6ik3s",
    "title": "Google Translate Telegram Bot | Nodejs \\u0026 Telegraf",
    "thumb": [
      "https://i.ytimg.com/vi/CTwlDu6ik3s/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\\u0026rs=AOn4CLDBuCSuLnUQfGwp5tA91JDcHrh3vg",
      "https://i.ytimg.com/vi/CTwlDu6ik3s/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=\\u0026rs=AOn4CLC5Uu46b8qQ8-t-i9XSJyH11SF3Eg"
    ],
    "simple_data": "Google Translate Telegram Bot | Nodejs \\u0026 Telegraf by modos coding 1 week ago 3 minutes, 50 seconds 17 views"
  }
]
		
		"""		
		limit = self.limit
		source = self.source
		data  = re.findall('{\"videoRenderer\":{\"videoId\":\"(\S{11})\",\"thumbnail\":{\"thumbnails\":\[{\"url\":\"(\S+)\",\"width\":360,\"height\":202},{\"url\":\"(\S+)\",\"width\":720,\"height\":404}\]},\"title\":{\"runs\":\[{\"text\":\"(.+?)\"}\],\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}},\"longBylineText\"',source)[:limit]
		data_ = []
		for i in data:
				js_data = {"id":"",
		            "title":"", 
		             "thumb" : "" ,
		              "simple_data":""}
				js_data['id'] = i[0]
				js_data['title'] = i[3]
				js_data['thumb'] = i[1],i[2]
				js_data['simple_data'] = i[4]
				data_.append(js_data)
		value =  json.dumps(data_ )
		return json.loads(value)
						
