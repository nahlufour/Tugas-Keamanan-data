from stegano import lsb
import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")

        # Frame for hiding message
        Label(root, text="Sembunyikan Pesan", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
        Button(root, text="Pilih Gambar", command=self.select_image_hide).grid(row=1, column=0, pady=5, padx=5)
        self.image_path_entry_hide = Entry(root, width=50)
        self.image_path_entry_hide.grid(row=1, column=1, pady=5)

        Label(root, text="Pesan: ").grid(row=2, column=0, pady=5, padx=5)
        self.message_entry = Entry(root, width=50)
        self.message_entry.grid(row=2, column=1, pady=5)

        Button(root, text="Pilih Lokasi Simpan", command=self.select_save_path).grid(row=3, column=0, pady=5, padx=5)
        self.save_path_entry = Entry(root, width=50)
        self.save_path_entry.grid(row=3, column=1, pady=5)

        Button(root, text="Sembunyikan Pesan", command=self.hide_message).grid(row=4, column=0, columnspan=2, pady=10)

        # Frame for revealing message
        Label(root, text="Tampilkan Pesan", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)
        Button(root, text="Pilih Gambar", command=self.select_image_reveal).grid(row=6, column=0, pady=5, padx=5)
        self.image_path_entry_reveal = Entry(root, width=50)
        self.image_path_entry_reveal.grid(row=6, column=1, pady=5)

        Button(root, text="Tampilkan Pesan", command=self.show_message).grid(row=7, column=0, columnspan=2, pady=10)

    def select_image_hide(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if image_path:
            self.image_path_entry_hide.delete(0, "end")
            self.image_path_entry_hide.insert(0, image_path)

    def select_save_path(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            self.save_path_entry.delete(0, "end")
            self.save_path_entry.insert(0, save_path)

    def select_image_reveal(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if image_path:
            self.image_path_entry_reveal.delete(0, "end")
            self.image_path_entry_reveal.insert(0, image_path)

    def hide_message(self):
        image_path = self.image_path_entry_hide.get()
        message = self.message_entry.get()
        save_path = self.save_path_entry.get()

        if not os.path.exists(image_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong.")
            return

        if not save_path:
            messagebox.showerror("Error", "Path penyimpanan tidak boleh kosong.")
            return

        try:
            secret = lsb.hide(image_path, message)
            secret.save(save_path)
            messagebox.showinfo("Berhasil", f"Pesan berhasil disematkan di {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    def show_message(self):
        img_path = self.image_path_entry_reveal.get()

        if not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan", f"Pesan yang disematkan: {clear_message}")
            else:
                messagebox.showinfo("Info", "Pesan tidak ditemukan dalam gambar.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mendapatkan pesan: {e}")


if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
