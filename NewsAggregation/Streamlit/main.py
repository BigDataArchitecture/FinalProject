import streamlit as st
import requests
import json
import numpy as np
from PIL import Image


response = requests.get("https://images.7news.com.au/publication/C-6518754/4af20795e626f3ff42180ecfbd31e2958ffc5211-16x9-x0y54w1024h576.jpg")

file = open("NewsAggregation/Streamlit/sample_image.png", "wb")
file.write(response.content)
file.close()

st.sidebar.write("Welcome Admin")       
st.title("Hello")

image = Image.open("NewsAggregation/Streamlit/sample_image.png")
st.image(image, caption='Sunrise by the mountains')