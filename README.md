PRODIGY_CS_02 - Image Encryption Tool

Description:
 - A Python program that encrypts and decrypts images using pixel manipulation technique.
 - Each pixel's RGB values are modified using a secret key to encrypt the image.
 - The same key reverses the process and recovers the original image.    
     
Features
- Browse and select any image (JPG, PNG, BMP)
- Encrypt image using a secret key number
- Decrypt image using the same key
- Live image preview inside the GUI window

How It Works
- Every image is made of pixels. Each pixel has 3 values: Red, Green, Blue (0-255)
- encrypt() function adds the key to each RGB value of every pixel
- decrypt() function subtracts the key to get back the original pixel values
- % 256 ensures the values always stay between 0 and 255

Code Explanation
- "Image.open()" opens the selected image file
- "img.load()" reads all the pixel values of the image
- "(r + key) % 256" adds key to Red value and keeps it within range
- "filedialog.asksaveasfilename()" lets user choose where to save output image

Technologies Used
- Python 3.13
- Tkinter (GUI)
- Pillow 12.2.0

How to Run
- py -m pip install Pillow
- Open Image_Encryption.py in IDLE
- Press F5 to run

Example
- Original pixel → (100, 150, 200)
- Key = 66
- Encrypted pixel → (166, 216, 10)
- Decrypted pixel → (100, 150, 200) 
