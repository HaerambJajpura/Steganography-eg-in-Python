from PIL import Image
import random

def decode_message_from_image(image_path, key):

    img = Image.open(image_path)
    img = img.convert("RGB") 


    pixels = list(img.getdata())


    random.seed(key)
    pixel_indices = list(range(len(pixels)))
    random.shuffle(pixel_indices)


    binary_message = ''
    for pixel_index in pixel_indices:
        r, g, b = pixels[pixel_index]
        binary_message += str(r & 1)

    message = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])


    message = message.split("####")[0]

    print("Decoded message:", message)


encoded_image_path = 'encoded_image.png'
key = 14980

decode_message_from_image(encoded_image_path, key)
input("Press Enter to continue...")