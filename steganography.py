import cv2
import os

def generate_lookup_tables():
    encrypt_table = {chr(i): i for i in range(256)}
    decrypt_table = {i: chr(i) for i in range(256)}
    return encrypt_table, decrypt_table

def encrypt_image(img, message):
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

def decrypt_message(img):
    n, m, z = 0, 0, 0
    decrypted_message = ""
    for _ in range(len(msg)):
        decrypted_message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3
    return decrypted_message

# Load the image
img = cv2.imread("sukana.png")
if img is None:
    raise ValueError("Error loading the image.")

# Encrypt the image
msg = input("Enter secret message: ")
encrypt_password = input("Enter encryption passcode:")
encrypt_table, decrypt_table = generate_lookup_tables()
encrypt_image(img, msg)

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.startfile("encryptedImage.jpg")

# Decrypt the message
attempts = 3  # Set the maximum number of attempts
for _ in range(attempts):
    decrypt_password = input("Enter decryption passcode:")
    if decrypt_password == encrypt_password:
        decrypted_msg = decrypt_message(img)
        print("Decrypted message =", decrypted_msg)
        break
    else:
        print("Incorrect password. Please try again.")
else:
    print("Exceeded maximum attempts. Exiting.")
    exit()
