"""
(C) @mrlokaman 
All rights reserved by LN Technical

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
		  	else:
		  		url_ =  'This tag not avilable'
		  		url.append(url_)
		  if url[0] == 'This tag not avilable' :
		  	raise Error(url[0])
		  else:
		  	return url[0]				  			 	  	 						 	  	 				
