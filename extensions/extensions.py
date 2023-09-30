# gets user input, remove whitespace, lowercase
filename = input("Filename: ")
filename = filename.strip().lower()

# get extension and store in first element of list
namestring = filename.split(".")
namestring.reverse()

# check for extension and output appropriate MIME
if filename.endswith(".gif") or filename.endswith(".jpeg") or filename.endswith(".png"):
    print("image/" + namestring[0])
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".pdf") or filename.endswith(".zip"):
    print("application/" + namestring[0])
elif filename.endswith(".jpg"):
    print("image/jpeg")
else:
    print("application/octet-stream")