from PIL import Image

def encode_image(image_path, output_path, message):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Convert message to binary
    binary_message = ''.join([format(ord(i), "08b") for i in message])
    binary_message += '1111111111111110'  # End of message delimiter

    # Create an iterator for the pixels
    pixels = encoded.load()
    
    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b, *rest = pixels[col, row]
                r = (r & ~1) | int(binary_message[index])
                index += 1
                if index < len(binary_message):
                    g = (g & ~1) | int(binary_message[index])
                    index += 1
                if index < len(binary_message):
                    b = (b & ~1) | int(binary_message[index])
                    index += 1
                
                # Handle alpha channel if present
                if rest:
                    pixels[col, row] = (r, g, b, *rest)
                else:
                    pixels[col, row] = (r, g, b)
            else:
                break

    encoded.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ''
    pixels = img.load()
    width, height = img.size
    
    for row in range(height):
        for col in range(width):
            r, g, b, *rest = pixels[col, row]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Split by 8-bits
    all_bytes = [binary_message[i: i + 8] for i in range(0, len(binary_message), 8)]
    
    # Convert from bits to characters
    decoded_message = ''
    for byte in all_bytes:
        if byte == '11111110':  # End of message delimiter
            break
        decoded_message += chr(int(byte, 2))
    
    return decoded_message

# User input
image_path = input("Enter the path to the image file: ")
output_path = input("Enter the output image file path: ")
message = input("Enter the message to hide: ")

# Encode the message
encode_image(image_path, output_path, message)

# Decode the message to verify
decoded_message = decode_image(output_path)
print(f"Decoded message: {decoded_message}")
