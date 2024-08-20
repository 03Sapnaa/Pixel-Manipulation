from PIL import Image
import numpy as np

# Encryption and Decryption Key
KEY = 123  # Simple integer key for XOR encryption

def encrypt_image(image_path, output_path, key):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encrypt the image
    encrypted_array = img_array ^ key

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_image_path, output_path, key):
    # Load the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)

    # Decrypt the image
    decrypted_array = encrypted_array ^ key

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    action = input("Enter 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").strip().lower()

    if action == 'encrypt':
        input_image = input("Enter the path of the image to encrypt: ").strip()
        output_image = input("Enter the path to save the encrypted image: ").strip()
        encrypt_image(input_image, output_image, KEY)
    elif action == 'decrypt':
        input_image = input("Enter the path of the encrypted image: ").strip()
        output_image = input("Enter the path to save the decrypted image: ").strip()
        decrypt_image(input_image, output_image, KEY)
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")
