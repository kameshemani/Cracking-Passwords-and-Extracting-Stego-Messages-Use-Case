from PIL import Image
import binascii

#opening image
imgg=Image.open("watermark.png")
#converting image to rgb format
imgg = imgg.convert("RGB")
k =""
width,height = imgg.size
green_binary_lsb = ""
#lsb bit detection
for x in range(height):
    for y in range(width):

        (r,g,b) = imgg.getpixel((y, x));

        green_binary_list = list(bin(g))

        green_binary_lsb = green_binary_lsb + green_binary_list[-1]
#converting binary to ascii
n = int(green_binary_lsb, 2)
k = binascii.unhexlify('%x' % n)
#opening a file and storing watermark
watermark= open('watermark.txt', 'w+')
watermark.write(k)





