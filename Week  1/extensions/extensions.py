shef = input("File name: ")

if shef.endswith("gif"):
    print("image/gif")

elif shef.endswith("jpg") or shef.endswith("jpeg"):
    print("image/jpeg")

elif shef.endswith("png"):
    print("image/png")

elif shef.endswith("pdf"):
    print("application/pdf")

elif shef.endswith("txt"):
    print("text/plain")

elif shef.endswith("zip"):
    print("application/zip")

else:
    print("application/octet-stream")