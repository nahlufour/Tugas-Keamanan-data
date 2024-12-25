import tkinter as tk
from tkinter import messagebox

# Fungsi Enkripsi
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        # Huruf besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Karakter selain huruf tetap
            cipher_text += char
    return cipher_text

# Fungsi Dekripsi
def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        # Huruf besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Karakter selain huruf tetap
            plain_text += char
    return plain_text

# Fungsi GUI untuk Enkripsi
def handle_enkripsi():
    plain_text = entry_plaintext.get()
    try:
        shift = int(entry_shift.get())
        if 1 <= shift <= 25:
            cipher_text = enkripsi(plain_text, shift)
            result_var.set(f"Hasil Enkripsi: {cipher_text}")
        else:
            messagebox.showerror("Error", "Pergeseran harus antara 1 dan 25!")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid!")

# Fungsi GUI untuk Dekripsi
def handle_dekripsi():
    cipher_text = entry_ciphertext.get()
    try:
        shift = int(entry_shift.get())
        if 1 <= shift <= 25:
            plain_text = dekripsi(cipher_text, shift)
            result_var.set(f"Hasil Dekripsi: {plain_text}")
        else:
            messagebox.showerror("Error", "Pergeseran harus antara 1 dan 25!")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid!")

# Membuat Antarmuka GUI
root = tk.Tk()
root.title("Program Enkripsi dan Dekripsi Teks")
root.geometry("400x300")

# Input Teks Asli
tk.Label(root, text="Teks Asli (Plaintext):").pack(pady=5)
entry_plaintext = tk.Entry(root, width=40)
entry_plaintext.pack()

# Input Teks Terenkripsi
tk.Label(root, text="Teks Terenkripsi:").pack(pady=5)
entry_ciphertext = tk.Entry(root, width=40)
entry_ciphertext.pack()

# Input Pergeseran
tk.Label(root, text="Nilai Pergeseran (1-25):").pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

# Tombol Enkripsi
btn_encrypt = tk.Button(root, text="Enkripsi", command=handle_enkripsi, bg="lightblue")
btn_encrypt.pack(pady=5)

# Tombol Dekripsi
btn_decrypt = tk.Button(root, text="Dekripsi", command=handle_dekripsi, bg="lightgreen")
btn_decrypt.pack(pady=5)

# Output Hasil
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").pack(pady=10)

# Jalankan GUI
root.mainloop()