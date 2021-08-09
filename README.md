# PyYouTube 

<p align="center">
  <a href="https://www.python.org">
    <img src="https://tg-link.herokuapp.com/dl/0/AgADkawxG1bbiVQ.jpg">

  </a>


Get Video Data from YouTube link 

## Installation 
```bash
pip install PyYouTube
```

## How to use it ?
#### Get Videos Data 

```python
from pyyoutube import Data
yt = Data("https://youtu.be/HhHzCfrqsoE")
print(yt.data)
```

#### Search Videos
> Get videos link 
```python 
from pyyoutube import Search
yt = Search("ln technical")
print(yt.videos)
```
> Get Video Data 
```python 
from pyyoutube import Search ,Data 
yt = Search("ln technical").videos
results = []
for vid in yt:
     res = Data(vid).data
     results.append(res)
print(results)
```

## License 
Copyright (c) 2021 Lntechnical

This repository is licensed under the MIT license.
