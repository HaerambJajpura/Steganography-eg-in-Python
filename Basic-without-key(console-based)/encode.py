from PIL import Image
import stepic

def encode_message_in_image(image_path, message, output_image_path):

    img = Image.open(image_path)
    

    encoded_image = stepic.encode(img, message.encode())

   
    encoded_image.save(output_image_path, 'PNG')
    print(f"Message encoded and saved in {output_image_path}")


image_path = 'input_image.jpg'
output_image_path = 'encoded_image.png'
message = "this is my secret message."

encode_message_in_image(image_path, message, output_image_path)
