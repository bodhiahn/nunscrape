import ctypes
import praw
import os
from PIL import Image
import requests
from io import BytesIO

image_path = "C:\\Users\\"+os.getlogin()+"\\Pictures\\nuns"

reddit = praw.Reddit(
    client_id="NV_EoxLhN9vNuuWvOOo9xA",
    client_secret="LhJ3tG7n_nDNLdLr0efPtvPvGW4lRw",
    user_agent="nunscrape",
)
user = reddit.redditor('LittleNunsBot')
submission = user.submissions.new(limit=1)
for s in submission:
    response = requests.get(s.url)
    img = Image.open(BytesIO(response.content))
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    image = img.save(f"{image_path}/nun.jpg")

ctypes.windll.user32.SystemParametersInfoW(20, 0, "%userprofile%\\pictures\\nuns\\nun.jpg" , 3)