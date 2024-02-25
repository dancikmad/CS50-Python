prompt = input("File name: ")
prompt = prompt.lower()

if prompt.endswith("gif"):
    print("image/gif")
elif ".jpg" in prompt:
    print("image/jpeg")
elif ".jpeg" in prompt:
    print("image/jpeg")
elif ".png" in prompt:
    print("image/png")
elif ".pdf" in prompt:
    print("application/pdf")
elif ".txt" in prompt:
    print("text/plain")
elif ".zip" in prompt:
    print("application/zip")
else:
    print("application/octet-stream")


