from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    encrypted = img_array ^ key
    result = Image.fromarray(encrypted.astype(np.uint8))
    result.save("encrypted.png")
    print("Encrypted! Saved as encrypted.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    decrypted = img_array ^ key
    result = Image.fromarray(decrypted.astype(np.uint8))
    result.save("decrypted.png")
    print("Decrypted! Saved as decrypted.png")

print("================================")
print("  Image Encryption Tool")
print("================================")
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter choice (1 or 2): ")
path   = input("Enter image filename: ")
key    = int(input("Enter secret key (0-255): "))

if choice == "1":
    encrypt_image(path, key)
elif choice == "2":
    decrypt_image(path, key)
else:
    print("Invalid choice!")
