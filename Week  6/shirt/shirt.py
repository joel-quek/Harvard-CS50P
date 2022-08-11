import sys
import PIL
from PIL import Image
from PIL import ImageOps
#-------------------------------------------------------------------------------------
try :
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1].split(".")[1] not in ["jpg", "jpeg", "png"]):
        sys.exit("Invalid input")
    elif (sys.argv[2].split(".")[1] not in ["jpg", "jpeg", "png"]):
        sys.exit("Invalid output")
    elif (sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]):
        sys.exit("Input and output have different extensions")
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        muppet = Image.open(filename)

except FileNotFoundError:
        sys.exit("Input does not exist")
# -----------------------------------------------------------------------------------
# Import before pictures and open CS50 shirt and check shirt size
CS50_shirt = Image.open("shirt.png")
shirt_size = CS50_shirt.size

# resize muppet to fit CS50 shirt
muppet = ImageOps.fit(muppet, shirt_size)

# merge CS50 shirt with before image
muppet.paste(CS50_shirt, (0, 0), CS50_shirt)

# Export After pictures
muppet.save(sys.argv[2])