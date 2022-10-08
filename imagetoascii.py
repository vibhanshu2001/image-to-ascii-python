import sys
from PIL import Image

# pass the image path below
image_path = 'myimage.jpg'
img = Image.open(image_path)

# resizing the image
width,height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio *new_width*0.55
img = img.resize((new_width,int(new_height)))
# new size of image can be printed using following command
print(img.size)

# now converting image to grayscale format
img = img.convert('L')
# getting the pixel by pixel information of image
pixels = img.getdata()
# now replacing each pixel with a character from the array defined as
chars = ["B","S","#","&","@","$","%","*","!",":",",","."]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# ?splitting string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index+new_width] for index in range(0,new_pixels_count,new_width)]
ascii_image = "\n".join(ascii_image)

# printing ascii_image
print(ascii_image)

# also writing the image to text file
with open("ascii_image.txt","w") as f:
    f.write(ascii_image)

# we are done with the code part. Let's hope we have not made any muistakes in code.abs
# Lets run it.
# eneabling the virtual environment - pipenv shell (for mac users)


# thank youfor the
# I will put the code in description box
# do like and comment if you need more videos like this: https
# Thanks :)