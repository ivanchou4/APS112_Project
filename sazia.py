from colorthief import ColorThief 
import matplotlib.pyplot as plt
from PIL import Image

#Open image using Image module
img = Image.open("Fall tree background.jpg")
img.show()
#Show actual Image

color_thief = ColorThief("Fall tree background.jpg")
dominant_color = color_thief.get_color(quality=1)
plt.imshow([[dominant_color]])
plt.show()

palette = color_thief.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()
