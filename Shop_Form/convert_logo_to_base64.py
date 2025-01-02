import base64

# Open the image file in binary mode
with open("shop_logo.jpg", "rb") as image_file:
    # Convert the image file to Base64
    base64_encoded = base64.b64encode(image_file.read()).decode("utf-8")

# Save the Base64 string to a file
with open("shop_logo_base64.txt", "w") as output_file:
    output_file.write(base64_encoded)

print("Base64 string saved to shop_logo_base64.txt")
