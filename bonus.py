from PIL import Image
import binascii

#opening image
imgg=Image.open("bonus.png")
#converting image to rgb format
imgg = imgg.convert("RGB")
k =""
width,height = imgg.size
red_binary_lsb = ""
#lsb bit detection and saving
for x in range(height):
    for y in range(width):

        (r,g,b) = imgg.getpixel((y, x));

        red_binary_list = list(bin(r))

        red_binary_lsb = red_binary_lsb + red_binary_list[-1]
#converting binary to ascii
n = int(red_binary_lsb, 2)
k = binascii.unhexlify('%x' % n)
#opening a file and storing watermark
watermark= open('bonus.txt', 'w+')
watermark.write(k)





