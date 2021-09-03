"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""
# This Modules Helps To Get Youtube Video Data 


import re
import urllib.request
import json

class Data:
      
      """
      	Get YouTube Video Data 
      	
      """
      def __init__(self,link):
      		headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
      		res = urllib.request.Request(link, headers=headers)
      		html = urllib.request.urlopen(res)
      		self.source = html.read().decode()
      		     		
      		
      # Get Video id 
      def id(self):
      	try:
      		videodetails=re.findall("\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
      	except:
      		return None
      	try:
      		#Get id , title From videodetails variable
      		id = re.findall("\"videoId\":\"(\S{11})",videodetails)[0]
      		return id 
      	except:
      		return None
      		
      	
      			
      # Get Video Title 	
      def title(self):
      	try:
      		videodetails=re.findall("\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
      	except:
      		return None
      	try:
      		#Get id , title From videodetails variable
      		title = re.findall("\"title\":\"(.+?)\",",videodetails)[0]
      		return title 
      	except:
      		return None
    
      
      
      #Get Thumbnails Link From Youtube Video 
      def thumb(self):
      		try :
      			thumb= re.findall("\"thumbnails\":\[\{\"url\":\"(.+?)\",\"width",self.source )[0]
      			return thumb
      		except:
      			return None
      		
      		
     # Get Video Publish Date 	
      def publish_date(self):
      	try:
      		publish_date = re.findall("\"publishDate\":\"(\d{4}-\d{2}-\d{2})", self.source)[0]
      		return publish_date
      	except:
      		return None
      
      def tag(self):
      	tag =re.findall("itag\":251,\"url\":\"(.+?)\",\"mimeType\"",self.source)
      	return tag
      	
      
      # Get Views Of the Video
      def views(self):
      	try:      		 
      		views = re.findall("\"viewCount\":\"(\d+)",self.source)[0]
      		return views
      	except:
      		return None
      
      
      # Get Category Of The Video 
      def category(self):
      	try:      		
      		category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
      		return category
      	except:
      		return None
      
      
      
      # Get Channel Name 
      def channel_name(self):
      		try:
      			channelName = e.findall("\"channelName\":\"(.+?)\",", self.source)[0]
      			return channelName
      		except:
      			try:
      				channelName = re.findall("\"ownerChannelName\":\"(.+?)\",\"uploadDate",self.source)[0]
      				return channelName
      			except:
      				return None
     
      				 				
      				
      #Get likes Of The Video 				
      def likes(self):
      		try:
      			likes = re.findall("accessibilityData\":{\"label\":\"(\S+) likes", self.source)[0]
      			return likes
      		except:
      			return None
      		
     
      		 		
      #Get dislikes Of The Video    		
      def dislikes(self): 
      	try:
      		dislikes = re.findall("accessibilityData\":{\"label\":\"(\S+) dislike", self.source)[0]
      		return dislikes
      	except:
      		return None
      		
      		
      #Get Subscriber of The video 		
      def subscriber(self):
      		try:
      			sub = re.findall("subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]  
      			return sub
      		except:
      			try:
      				sub = re.findall("accessibilityData\":{\"label\":\"(\S+) subscribers", self.source)[0]   				
      				return sub
      			except:
      				return None 
      			
      def data(self):
      	try:
      		# Get Video Details 
      		videodetails=re.findall("\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
      	except:
      		videodetails = None
      	try:
      		#Get id , title From videodetails variable
      		id = re.findall("\"videoId\":\"(\S{11})",videodetails)[0]
      		title = re.findall("\"title\":\"(.+?)\",",videodetails)[0]
      	except:
      		title = None
      		id = None
      	try :
      		#Get Thumbnails Link From Youtube Video 
      		thumb= re.findall("\"thumbnails\":\[\{\"url\":\"(.+?)\",\"width",self.source )[0]
      	except:
      		thumb = None
      	try:
      		# Get Video Publish Date 
      		publish_date = re.findall("\"publishDate\":\"(\d{4}-\d{2}-\d{2})", self.source)[0]
      	except:
      		publish_date = None
      	try:
      		# Get Views Of the Video 
      		views = re.findall("\"viewCount\":\"(\d+)",self.source)[0]
      	except:
      		views = None
      	try:
      		# Get Category Of The Video 
      		category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
      	except:
      		category = None       		
      	try:
      		# Get Channel Name 
      		channelName = e.findall("\"channelName\":\"(.+?)\",", self.source)[0]
      	except:
      		try:
      			channelName = re.findall("\"ownerChannelName\":\"(.+?)\",\"uploadDate",self.source)[0]
      		except:
      			channelName = None
      			
      	try:
      		#Get likes Of The Video 
      		likes = re.findall("accessibilityData\":{\"label\":\"(\S+) likes", self.source)[0]
      	except:
      		likes = None
      	try:
      		#Get dislikes Of The Video 
      		dislikes = re.findall("accessibilityData\":{\"label\":\"(\S+) dislike", self.source)[0]
      	except:
      		dislikes = None 
      	try:
      		#Get Subscriber of The video 
      		sub = re.findall("accessibilityData\":{\"label\":\"(\S+) subscribers", self.source)[0]
      	except:
      		try:
      			sub = re.findall("subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]  
      		except:
      			sub = None
      		
      	DATA = { 
      	             "id": id,
      	             "title": title,
      	             "thumbnails": thumb,
      	             "views": views,
      	             "likes": likes,
      	             "dislikes":dislikes,
      	             "publishdate": publish_date,
      	             "category": category,
      	             "channel_name": channelName,
      	             "subscriber":sub
      	        }
      	 
      	return json.dumps(DATA,indent = 2)
      	
     
      	

	
"""

Search Youtube Video 

Example:
	
from pyyoutube import Search

yt = Search("ln technical" , 1)

print(yt.videos)

OUTPUT :
	['https://youtu.be/{11}']
"""		
			
					
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
		     	
