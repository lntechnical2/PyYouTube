""" (C) @mrlokaman All rights reserved by LN Technical

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
class Data:

    """
      Get YouTube Video Data

    """

    def __init__(self, link):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        res = urllib.request.Request(link, headers=headers)
        html = urllib.request.urlopen(res)
        self.source = html.read().decode('utf8')

    # Get Video id

    def id(self):
        try:
            videodetails = re.findall(
                "\"videoDetails\":\\{(.+?),\"isOwnerViewing",
                self.source)[0]
        except BaseException:
            return None
        try:
            # Get id , title From videodetails variable
            id = re.findall("\"videoId\":\"(\\S{11})", videodetails)[0]
            return id
        except BaseException:
            return None

    # Get Video Title

    def title(self):
        try:
            videodetails = re.findall(
                "\"videoDetails\":\\{(.+?),\"isOwnerViewing",
                self.source)[0]
        except BaseException:
            return None
        try:
            # Get id , title From videodetails variable
            title = re.findall("\"title\":\"(.+?)\",", videodetails)[0]
            return title
        except BaseException:
            return None

    def shortDescription(self):
        try:
            # Get id , title From videodetails variable
            shortDescription = re.findall("\"shortDescription\":\"(.+?)\",", self.source)[0]
            return shortDescription
        except BaseException:
            return None

    # Get Thumbnails Link From Youtube Video

    def thumb(self):
        try:
            thumb = re.findall(
                "\"thumbnails\":\\[\\{\"url\":\"(.+?)\",\"width",
                self.source)[0]
            return thumb
        except BaseException:
            return None

     # Get Video Publish Date

    def publish_date(self):
        try:
            publish_date = re.findall(
                "\"publishDate\":\"(\\d{4}-\\d{2}-\\d{2})",
                self.source)[0]
            return publish_date
        except BaseException:
            return None

    # Get Views Of the Video

    def views(self):
        try:
            views = re.findall("\"viewCount\":\"(\\d+)", self.source)[0]
            return views
        except BaseException:
            return None

    # Get Category Of The Video

    def category(self):
        try:
            category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
            return category
        except BaseException:
            return None

    # Get Channel Name

    def channel_name(self):
        try:
            channelName = e.findall(
                "\"channelName\":\"(.+?)\",", self.source)[0]
            return channelName
        except BaseException:
            try:
                channelName = re.findall(
                    "\"ownerChannelName\":\"(.+?)\",\"uploadDate", self.source)[0]
                return channelName
            except BaseException:
                return None

    # Get likes Of The Video

    def likes(self):
        try:
            likes = re.findall(
                "accessibilityData\":{\"label\":\"(\\S+) likes",
                self.source)[0]
            return likes
        except BaseException:
            return None

    # Get dislikes Of The Video

    def dislikes(self):
        try:
            dislikes = re.findall(
                "accessibilityData\":{\"label\":\"(\\S+) dislike",
                self.source)[0]
            return dislikes
        except BaseException:
            return None

    # Get YouTube Videos tag
    def tags(self):
        try:
            tags = re.findall(
                "\\<meta name=\"keywords\" content=\"(.+?)\">",
                self.source)[0]
            return tags
        except BaseException:
            return None

    # Get Subscriber of The video

    def subscriber(self):
        try:
            sub = re.findall(
                "subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}",
                self.source)[0]
            return sub
        except BaseException:
            try:
                sub = re.findall(
                    "accessibilityData\":{\"label\":\"(\\S+) subscribers",
                    self.source)[0]
                return sub
            except BaseException:
                return None

    def data(self):
        try:
            # Get Video Details
            videodetails = re.findall(
                "\"videoDetails\":\\{(.+?),\"isCrawlable",
                self.source)[0]
        except BaseException:
            videodetails = None
        try:
            # Get id , title From videodetails variable
            id = re.findall("\"videoId\":\"(\\S{11})", videodetails)[0]
            title = re.findall("\"title\":\"(.+?)\",", videodetails)[0]
        except BaseException:
            title = None
            id = None
        try:
            shortDescription = re.findall("\"shortDescription\":\"(.+?)\",", self.source)[0]
        except:
            shortDescription = None
        try:
            # Get Thumbnails Link From Youtube Video
            thumb = re.findall(
                "\"thumbnails\":\\[\\{\"url\":\"(.+?)\",\"width",
                self.source)[0]
        except BaseException:
            thumb = None
        try:
            # Get Video Publish Date
            publish_date = re.findall(
                "\"publishDate\":\"(\\d{4}-\\d{2}-\\d{2})",
                self.source)[0]
        except BaseException:
            publish_date = None
        try:
            # Get Views Of the Video
            views = re.findall("\"viewCount\":\"(\\d+)", self.source)[0]
        except BaseException:
            views = None
        try:
            # Get Category Of The Video
            category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
        except BaseException:
            category = None
        try:
            # Get Channel Name
            channelName = e.findall(
                "\"channelName\":\"(.+?)\",", self.source)[0]
        except BaseException:
            try:
                channelName = re.findall(
                    "\"ownerChannelName\":\"(.+?)\",\"uploadDate", self.source)[0]
            except BaseException:
                channelName = None

        try:
            # Get likes Of The Video
            likes = re.findall(
                "accessibilityData\":{\"label\":\"(\\S+) likes",
                self.source)[0]
        except BaseException:
            likes = None
        try:
            # Get dislikes Of The Video
            dislikes = re.findall(
                "accessibilityData\":{\"label\":\"(\\S+) dislike",
                self.source)[0]
        except BaseException:
            dislikes = None
        try:
            # Get Subscriber of The video
            sub = re.findall(
                "accessibilityData\":{\"label\":\"(\\S+) subscribers",
                self.source)[0]
        except BaseException:
            try:
                sub = re.findall(
                    "subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}",
                    self.source)[0]
            except BaseException:
                sub = None
            # kewords(tag)
        try:
            tags = re.findall(
                "\\<meta name=\"keywords\" content=\"(.+?)\">",
                self.source)[0]
        except BaseException:
            tags = None

        DATA = {
            "id": id,
            "title": title,
            "shortDescription": shortDescription,
            "thumbnails": thumb,
            "duration": None,
            "views": views,
            "likes": likes,
            "dislikes": dislikes,
            "publishdate": publish_date,
            "category": category,
            "channel_name": channelName,
            "subscriber": sub,
            "keywords": tags
        }

        return DATA
