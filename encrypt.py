from PIL import Image
import numpy as np


def encrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    img_array = np.array(img)

    # 1️⃣ XOR pixel values with key
    encrypted_array = img_array ^ key

    # 2️⃣ Swap rows (simple reversible shuffle)
    encrypted_array = encrypted_array[::-1]

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)

    print("✅ Image encrypted successfully!")


def decrypt_image(input_path, output_path, key):
    # Open encrypted image
    img = Image.open(input_path)
    img_array = np.array(img)

    # 1️⃣ Reverse row swap
    decrypted_array = img_array[::-1]

    # 2️⃣ XOR again with same key (XOR is reversible)
    decrypted_array = decrypted_array ^ key

    # Save decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)

    print("✅ Image decrypted successfully!")


def main():
    print("=== Simple Image Encryption Tool ===")

    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter numeric key (0-255): "))

    if choice == "encrypt":
        encrypt_image(input_path, output_path, key)
    elif choice == "decrypt":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
