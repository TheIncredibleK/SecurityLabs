from PIL import Image
from numpy import ndenumerate as iterate_
from stegano import lsb

image_file = "gray.png"
result_file = "gray_with_result.png"
image_pixels_file = "image_pixels.txt"
new_image = "new_image_file.png"

"""
Question 1:
Print image to new file
"""
grayscale = Image.open(image_file).convert('L')
internals = grayscale.load()

with open(image_pixels_file, "w") as f:
    for (x,y), pixel in iterate_(grayscale):
        f.write(str(x) + "," + str(y) + " : " + str(pixel) + "\n" )

with open(new_image, "wb") as f2:
    with open(image_file, "rb") as f3:
        f2.write(f3.read())



"""
Question 2:
Hide message within file
"""
plaintext = 'keith kenny c13443362'
cipher_image = lsb.hide(image_file, plaintext)
cipher_image.save(result_file)
decrypted_plaintext = lsb.reveal(result_file)
print decrypted_plaintext