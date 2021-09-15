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


# PyYouTube is optionally depends on youtube-dl 

import youtube_dl

class Error(Exception):
    pass

class ytdl:
	def __init__(self,link):
		" "
		ydl_opts = {
		                       'quiet': True  }
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			meta = ydl.extract_info(link,download=False)
			self.format = meta.get('formats' , [meta])
	
	def formats(self):
		 form_ = []
		 formats_ = self.format
		 for qu in formats_ :
		 	 formats = qu["format"]
		 	 form_.append(formats)		 	 
		 return form_
	
	def url(self, itag:str):
		  formats_ = self.format
		  url = []
		  data = []
		  for qu in formats_ :
		  	id_url =  qu['format_id'],qu['url'],qu['format']
		  	data.append(id_url)
		  for tag in data:
		  		if tag[0] == itag:
		  			url_ =  tag[1]
		  			url.append(url_)
		  if url:
		  	return url[0]
		  else:
		      raise Error('this tag not avilable')
		      
		      
	def besturl(self):
		formats_ = self.format
		for qu in formats_ :
			if qu['acodec'] != 'none' and qu['vcodec'] != 'none':
				url_ = qu['url']
		return url_			    	 						 	  	 				