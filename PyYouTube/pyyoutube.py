"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""
import re
import urllib.request


class Youtube:
      def __init__(self, link):
      	"""
      	Get YouTube Video Data 
      	
      	"""
      	try:
      		html = urllib.request.urlopen(link)
      	except Exception as e :
      		print(e)
      		return 
      	source = html.read().decode()
      	try:
      		# Get Video Details 
      		videodetails=re.findall("\"videoDetails\":\{(.+?),\"isCrawlable", source)[0]
      	except:
      		videodetails = None
      	try:
      		#Get id , title , description From videodetails variable
      		id = re.findall("\"videoId\":\"(\S{11})",videodetails)[0]
      		title = re.findall("\"title\":\"(.+?)\",",videodetails)[0]
      		desc2 = re.findall("\"shortDescription\":\"(.+?)\"",videodetails)[0]
      	except:
      		title = None
      		id = None
      		desc2 = None
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
      		channelName = re.findall("\"channelName\":\"(.+?)\",",source)[0]
      	except:
      		channelName = None 
      	try:
      		#Get likes Of The Video 
      		likes = re.findall("accessibilityData\":{\"label\":\"(\d+) likes", source)[0]
      	except:
      		likes = None 
      	try:
      		#Get dislikes Of The Video 
      		dislikes = re.findall("accessibilityData\":{\"label\":\"(\S+) dislike", source)[0]
      	except:
      		dislikes = None 
      	try:
      		#Get Subscriber of The video 
      		sub = re.findall("accessibilityData\":{\"label\":\"(\S+) subscribers", source)[0]
      	except:
      		sub = None
      	try:
      		desc= re.findall("name=\"title\"/><meta content=\"(.+?)\" name=\"description\"/", source)[0]
      	except:
      		desc = desc2
      	#Get all Data in JSON Format 
      	self.data = { 
      	             "id": id,
      	             "title": title,
      	             "thumbnails": thumb,
      	             "views": views,
      	             "description":desc,
      	             "likes": likes,
      	             "dislikes":dislikes,
      	             "publishdate": publish_date,
      	             "category": category,
      	             "channel_name": channelName,
      	             "subscriber":sub
      	        }
      	 
      	# Get Specific Value 
      	self.id = id
      	self.title = title 
      	self.thumbnails = thumb
      	self.views = views
      	self.description = desc
      	self.likes = likes
      	self.dislikes = dislikes
      	self.publishdate =  publish_date
      	self.category = category
      	self.channel_name = channelName
      	self.subscriber = sub


