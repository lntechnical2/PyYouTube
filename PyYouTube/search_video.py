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
from pyyoutube import Data


class Search:
	
	def __init__(self,keywords:str , limit=10):
		
		search_keyword=keywords.replace(" ", "+")
		html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
		self.limit= limit
		self.source = html.read().decode()
		video_ids = re.findall(r"watch\?v=(\S{11})", self.source)[:self.limit]
		self.video_link = []
		for i in video_ids:
			id = 'https://youtu.be/'+i
			video_link.append(id)
		
	def videos(self):
		data = []
		video_ids = re.findall(r"watch\?v=(\S{11})", self.source)[:self.limit]
		link = self.video_link
		for i in video_ids:
			id = 'https://youtu.be/'+i
			link.append(id)		
		for i in link:
			_data = Data(i).data()
			data.append(_data)
		return data		
