# Steganography
Here is a complete code implementation for steganography that allows the user to input both text and image, encode the text into the image, and then decode it to verify the hidden message. This code uses the Pillow library for image processing


Explanation:

1. encode_image(image_path, output_path, message):

      Uses the load() method to access the image pixels directly.
      Iterates through each pixel and modifies the least significant bits based on the binary message.
      This approach avoids creating a large list of all pixel data, making it more memory-efficient.
      Adjusted to handle both RGB and RGBA images by using r, g, b, *rest to unpack the pixel values.
      If there are additional values (like alpha), they are stored in rest and included back in the modified pixel data.
2.decode_image(image_path):

      Uses the load() method to access the image pixels directly.
      Iterates through each pixel to extract the least significant bits and reconstructs the binary message.
      Similarly adjusted to handle both RGB and RGBA images by using r, g, b, *rest to unpack the pixel values.


Instructions to run the code:
1. Save the code in a Python file, e.g., "steganography.py".
2. Ensure you have the Pillow library installed:
             pip install pillow
3. Run the script:
             python steganography.py
4. Follow the prompts to input the image path, output image path, and the message you want to hide.
5. The script will save the image with the hidden message and decode it to verify.


Example Output:
1. User input:
         Enter the path to the image file: input_image.png
         Enter the output image file path: output_image.png
         Enter the message to hide: Hello, World!
2. Output:
         Message encoded and saved to output_image.png
         Decoded message: Hello, World!

   
Notes:
        The script uses the least significant bit (LSB) method to hide the message in the RGB channels of the image.
        Ensure the image has enough pixels to store the entire binary message.
        The end of message delimiter (1111111111111110) is used to mark the end of the hidden message.
