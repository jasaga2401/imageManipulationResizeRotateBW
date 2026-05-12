
from PIL import Image

img = Image.open("football.jpg")

# Resize
small = img.resize((300, 200))

# Rotate
rotated = img.rotate(90)

# Convert to black and white
bw = img.convert("L")

# Save result
bw.save("photo_black_white.jpg")
