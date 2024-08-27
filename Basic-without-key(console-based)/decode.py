from PIL import Image
import stepic

def decode_message_from_image(image_path):
    img = Image.open(image_path)
    
    message = stepic.decode(img)
    print("Decoded message:", message)

encoded_image_path = 'encoded_image.png'
decode_message_from_image(encoded_image_path)
