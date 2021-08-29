"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""
# This Modules Helps To Get Youtube Video Data 

"""
example :

from  pyyoutube import Data

yt = Data("Youtube Video link")

print(yt.data)

OUTPUT :
	{ 
      	             "id": id,
      	             "title": title,
      	             "thumbnails": thumb,
      	             "views": views,
      	             "likes": likes,
      	             "dislikes":dislikes,
      	             "publishdate": publish_date,
      	             "category": category,
      	             "channel_name": channelName,
      	             "subscriber":sub,
                     "tags":tags
	}
"""

import re
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import html5lib


class Data:
      
      """
      	Get YouTube Video Data 
      	
      """
      def __init__(self,link:str):
      
      	try:
      		html = urllib.request.urlopen(link)
      	except Exception as e :
      		self.data = e
      		self.id = e
      		self.title = e
      		self.thumbnails = e
      		self.views = e
      		self.likes = e
      		self.dislikes = e
      		self.publishdate =  e
      		self.category = e
      		self.channel_name = e
      		self.subscriber = e
                self.tags = e
      		return
      	source = html.read().decode()
      	try:
      		# Get Video Details 
      		videodetails=re.findall("\"videoDetails\":\{(.+?),\"isOwnerViewing", source)[0]
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
      		thumb= re.findall("\"thumbnails\":\[\{\"url\":\"(.+?)\",\"width",source )[0]
      	except:
      		thumb = None
      	try:
      		# Get Video Publish Date 
      		publish_date = re.findall("\"publishDate\":\"(\d{4}-\d{2}-\d{2})", source)[0]
      	except:
      		publish_date = None
      	try:
      		# Get Views Of the Video 
      		views = re.findall("\"viewCount\":\"(\d+)",source)[0]
      	except:
      		views = None
      	try:
      		# Get Category Of The Video 
      		category = re.findall("\"category\":\"(.+?)\",", source)[0]
      	except:
      		category = None       		
      	try:
      		# Get Channel Name 
      		channelName = re.findall("\"ownerChannelName\":\"(.+?)\",\"uploadDate",source)[0]
      	except:
      		try:
      			channelName = e.findall("\"channelName\":\"(.+?)\",", source)[0]
      		except:
      			channelName = None
      			
      	try:
      		#Get likes Of The Video 
      		likes = re.findall("accessibilityData\":{\"label\":\"(.+?) likes", source)[0]
      	except:
      		likes = None 
      	try:
      		#Get dislikes Of The Video 
      		dislikes = re.findall("accessibilityData\":{\"label\":\"(\S+) dislike", source)[0]
      	except:
      		dislikes = None 
      	try:
      		#Get Subscriber of The video 
      		sub = re.findall("\"subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"", source)[0]
      	except:
      		sub = None
        try:
                request = requests.get(link)
                soup = BeautifulSoup(request.content, 'html5lib') 
                tags = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
                text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
        except:
                tags = None

      	#Get all Data in JSON Format
      	self.data = { 
      	             "id": id,
      	             "title": title,
      	             "thumbnails": thumb,
      	             "views": views,
      	             "likes": likes,
      	             "dislikes":dislikes,
      	             "publishdate": publish_date,
      	             "category": category,
      	             "channel_name": channelName,
      	             "subscriber":sub,
                     "tags":tags
      	        }
      	        
      	#  Get Specific Value 
      	self.id = id
      	self.title = title 
      	self.thumbnails = thumb
      	self.views = views
      	self.likes = likes
      	self.dislikes = dislikes
      	self.publishdate =  publish_date
      	self.category = category
      	self.channel_name = channelName
      	self.subscriber = sub
        self.tags = tags

class Search:
	def __init__(self,keywords:str , limit: int=10):
		search_keyword=keywords.replace(" ", "+")
		try:
			html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
		except Exception as e :
			self.videos = e
			return
		source = html.read().decode()
		video_ids = re.findall(r"watch\?v=(\S{11})", source)[:limit]
		video_link = []
		for i in video_ids:
			id = 'https://youtu.be/'+i
			video_link.append(id)
		self.videos = video_link		   	
