from PIL import Image

# Open the JPG image
jpg_image = Image.open("car/car2/texture_dae/Specchio1.png.001.png")

# Convert and save as PNG
jpg_image.save("car/car1/texture_stl/texture_0.png", "PNG")

# Open the JPG image
# jpg_image = Image.open("rounddoor/rounddoor3/texture_dae/material_24.jpg")
#
# # Convert and save as PNG
# jpg_image.save("rounddoor/rounddoor3/texture_stl/texture_1.png", "PNG")