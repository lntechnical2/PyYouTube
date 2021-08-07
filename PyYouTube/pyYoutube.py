"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""
# This Modules Helps To Get Youtube Video Data 

"""
example 

from  pyYoutube import Data

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
                    "subscriber":sub
 }
"""

import re
import urllib.request


class Data:
      
      """
       Get YouTube Video Data 
       
      """
      def init(self,link):
       
       try:
        html = urllib.request.urlopen(link)
       except Exception as e :
        print(e)
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
        channelName = e.findall("\"channelName\":\"(.+?)\",", source)[0]
       except:
        try:
         channelName = re.findall("\"ownerChannelName\":\"(.+?)\",\"uploadDate",source)[0]
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
       #Get all Data in JSON Format 
       data = { 
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
       
