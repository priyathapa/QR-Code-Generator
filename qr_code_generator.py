import qrcode
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Ask user for URL
url = input("Enter the URL: ")

# Generate QR code
img = qrcode.make(url)
img.save("qrcode.png")

# Create window
root = Tk()
root.title("img")
root.configure(bg="white")

# Load and display image
qr_image = Image.open("qrcode.png")
qr_photo = ImageTk.PhotoImage(qr_image)

label = Label(root, image=qr_photo, bg="white")
label.pack(padx=20, pady=20)

root.mainloop()
