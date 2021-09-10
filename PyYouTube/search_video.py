


class Search:
	
	def __init__(self,keywords:str , limit=15):
		
		search_keyword=keywords.replace(" ", "+")
		html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
		self.limit= limit
		self.source = html.read().decode()
	
	def videos(self):
		video_ids = re.findall(r"watch\?v=(\S{11})", self.source)[:self.limit]
		video_link = []
		for i in video_ids:
			id = 'https://youtu.be/'+i
			video_link.append(id)
		return video_link
		     	
