from PIL import Image
import random

def encode_message_in_image(image_path, message, output_image_path, key):

    img = Image.open(image_path)
    img = img.convert("RGB")


    message += "####"
    binary_message = ''.join([format(ord(char), '08b') for char in message])


    pixels = list(img.getdata())
    

    random.seed(key)
    pixel_indices = list(range(len(pixels)))
    random.shuffle(pixel_indices)


    for i in range(len(binary_message)):
        pixel_index = pixel_indices[i]
        r, g, b = pixels[pixel_index]


        r = (r & ~1) | int(binary_message[i])

   
        pixels[pixel_index] = (r, g, b)


    img.putdata(pixels)
    img.save(output_image_path, 'PNG')
    print(f"Message encoded and saved in {output_image_path}")


image_path = 'input_image.jpg'
output_image_path = 'encoded_image.png'
message = input("Enter the ssecret message: ")
key = 14980 

encode_message_in_image(image_path, message, output_image_path, key)
input("Press Enter to continue...")
