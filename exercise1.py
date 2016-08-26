from cp_ecb import encrypt_image_file, decrypt_image_file


# A key to use for the Caesar Cipher
KEY = 42


def caesar(image):
    output = []

    for value in image:
        output += [value]  # TODO change here (this does nothing)

    return output


encrypt_image_file("tux.png", caesar, "tux-caesar.png")
