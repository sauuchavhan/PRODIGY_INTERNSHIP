from PIL import Image


def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save("encrypted_image.png")
    print("Image Encrypted Successfully!")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save("decrypted_image.png")
    print("Image Decrypted Successfully!")


image_path = input("Enter image path: ")
key = int(input("Enter encryption key: "))

encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)