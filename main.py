
import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


def generate_qr():
    text = entry.get().strip()

    if not text:
        messagebox.showwarning(
            "Input Required",
            "Please enter text or a website URL!"
        )
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(text)
        qr.make(fit=True)

        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert("RGB")

        # Keep the QR image for saving
        global generated_image
        generated_image = qr_image

        # Resize the image for the window
        preview = qr_image.copy()
        preview.thumbnail((250, 250))

        global qr_photo
        qr_photo = ImageTk.PhotoImage(preview)

        qr_label.config(image=qr_photo, text="")
        status_label.config(
            text="QR code generated successfully!",
            fg="green"
        )

    except Exception as error:
        messagebox.showerror("Error", str(error))


def save_qr():
    if generated_image is None:
        messagebox.showwarning(
            "No QR Code",
            "Generate a QR code first!"
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save QR Code"
    )

    if file_path:
        generated_image.save(file_path)
        messagebox.showinfo(
            "Saved",
            "QR code saved successfully!"
        )


# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x560")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

generated_image = None
qr_photo = None

# Heading
heading = tk.Label(
    root,
    text="QR Code Generator",
    font=("Arial", 22, "bold"),
    bg="#f0f4f8",
    fg="#183153"
)
heading.pack(pady=(20, 10))

# Instructions
instructions = tk.Label(
    root,
    text="Enter text or a website URL below",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#444444"
)
instructions.pack(pady=5)

# Text input
entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=35,
    relief="solid",
    bd=1
)
entry.pack(pady=10, ipady=7)

# Generate button
generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
generate_button.pack(pady=10, ipadx=12, ipady=5)

# QR code preview
qr_label = tk.Label(
    root,
    text="Your QR code will appear here",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#666666"
)
qr_label.pack(pady=10)

# Save button
save_button = tk.Button(
    root,
    text="Save QR Code as PNG",
    command=save_qr,
    font=("Arial", 11),
    bg="#15803d",
    fg="white",
    activebackground="#166534",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
save_button.pack(pady=10, ipadx=8, ipady=5)

# Status message
status_label = tk.Label(
    root,
    text="Ready to generate a QR code",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#555555"
)
status_label.pack(pady=5)

root.mainloop()
