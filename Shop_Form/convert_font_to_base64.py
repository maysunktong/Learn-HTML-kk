import base64

# Open the font file in binary mode
with open("Sarabun-Regular.ttf", "rb") as font_file:
    # Convert the font file to Base64
    base64_encoded = base64.b64encode(font_file.read()).decode("utf-8")

# Save the Base64 string to a file
with open("Sarabun-Regular-Base64.txt", "w") as output_file:
    output_file.write(base64_encoded)

print("Base64 string saved to Sarabun-Regular-Base64.txt")
