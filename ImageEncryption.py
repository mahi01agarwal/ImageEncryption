# Encrypt an image file using the Caesar cipher
def encrypt_image(image_file, shift):
  # Open the image file in binary mode
  with open(image_file, 'rb') as file:
    # Read the file content into a bytes object
    image_bytes = file.read()
  
  # Create an empty list to store the encrypted bytes
  encrypted_bytes = []
  
  # Iterate over each byte in the image
  for b in image_bytes:
    # Encrypt the byte by shifting it to the right
    encrypted_byte = (b + shift)%256
    # Append the encrypted byte to the list
    encrypted_bytes.append(encrypted_byte)
  
  # Convert the encrypted bytes back into a bytes object
  encrypted_image = bytes(encrypted_bytes)
  
  # Write the encrypted bytes back to a new file
  with open('encrypted_image.bin', 'wb') as file:
    file.write(encrypted_image)

# Test the encryption function
encrypt_image('rickroll.jpeg', 3)



# Decrypt an image file using the Caesar cipher
def decrypt_image(image_file, shift):
  # Open the image file in binary mode
  with open(image_file, 'rb') as file:
    # Read the file content into a bytes object
    encrypted_bytes = file.read()
  
  # Create an empty list to store the decrypted bytes
  decrypted_bytes = []
  
  # Iterate over each byte in the encrypted image
  for b in encrypted_bytes:
    # Decrypt the byte by shifting it to the left
    decrypted_byte = (b - shift)%256
    # Append the decrypted byte to the list
    decrypted_bytes.append(decrypted_byte)
  
  # Convert the decrypted bytes back into a bytes object
  decrypted_image = bytes(decrypted_bytes)
  
  # Write the decrypted bytes back to a new file
  with open('decrypted_image.jpg', 'wb') as file:
    file.write(decrypted_image)
    
decrypt_image('encrypted_image.bin', 3)   



