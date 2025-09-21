import re
import os
import random
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

def encryptfile(txtfile):
    """Read plaintext from txtfile, write numeric ciphertext to encrypted_file.txt and return seed."""
    if not os.path.exists(txtfile):
        raise FileNotFoundError(f"File not found: {txtfile}")
    seed = random.randint(1, 10**9)
    random.seed(seed)
    with open(txtfile, "r", encoding="utf-8") as f:
        message = f.read()
    parts = []
    for char in message:
        val = ord(char)
        val = val * random.randint(1, 99)
        val = val * random.randint(1, 99)
        parts.append(str(val))
    encrypted_path = "encrypted_file.txt"
    with open(encrypted_path, "w", encoding="utf-8") as f:
        f.write(" ".join(parts) + "\n")
        f.write(f"Seed: {seed}\n")
    return encrypted_path, seed

def decryptfile(txtfile, provided_seed=None):
    """Read numeric ciphertext from txtfile (or use provided_seed), write plaintext to decrypted_file.txt."""
    if not os.path.exists(txtfile):
        raise FileNotFoundError(f"File not found: {txtfile}")
    with open(txtfile, "r", encoding="utf-8") as f:
        content = f.read()
    # Try to extract seed from file if not provided
    seed = provided_seed
    if seed is None:
        m = re.search(r"Seed:\s*(\d+)", content)
        if m:
            seed = int(m.group(1))
            # remove the Seed line from the numeric string
            content = re.sub(r"Seed:\s*\d+", "", content)
    if seed is None:
        # caller should request seed from user
        raise ValueError("Seed not found in file")
    random.seed(int(seed))
    num_tokens = content.split()
    nums = []
    try:
        for tok in num_tokens:
            n = int(tok)
            n = n // random.randint(1, 99)
            n = n // random.randint(1, 99)
            nums.append(n)
        plaintext = "".join(chr(n) for n in nums)
    except Exception as e:
        raise ValueError("Decryption failed or invalid ciphertext") from e
    decrypted_path = "decrypted_file.txt"
    with open(decrypted_path, "w", encoding="utf-8") as f:
        f.write(plaintext)
    return decrypted_path, plaintext

def encrypt(msg):
    """Encrypt message by seeding RNG, then multiplying each char code by two random ints.
    Returns the space-separated numeric ciphertext and the seed used."""
    seed = random.randint(1, 10**9)
    random.seed(seed)
    parts = []
    for char in msg:
        val = ord(char)
        val = val * random.randint(1, 99)
        val = val * random.randint(1, 99)
        parts.append(str(val))
    encrypted = " ".join(parts)
    return encrypted, seed

def decrypt(encrypted_msg, seed):
    """Decrypt space-separated numeric ciphertext using the provided seed.
    Returns the plaintext or raises ValueError on invalid input."""
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        raise ValueError("Invalid seed")

    random.seed(seed)
    textlist = encrypted_msg.split()
    numbers_list = []
    for s in textlist:
        n = int(s)
        n = n // random.randint(1, 99)
        n = n // random.randint(1, 99)
        numbers_list.append(n)
    try:
        result_string = "".join(chr(num) for num in numbers_list)
    except Exception as e:
        raise ValueError("Decryption produced invalid character codes") from e
    return result_string

window = tk.Tk()
window.title('Encryption/Decryption Tool')
window.geometry('1280x960')

# top frame: filename entry
top_frame = ttk.Frame(window, padding=10)
top_frame.pack(fill="x")
ttk.Label(top_frame, text="File name (for file operations):").pack(side="left", padx=(0,6))
file_entry = ttk.Entry(top_frame, width=60)
file_entry.pack(side="left", fill="x", expand=True)

def ask_and_encrypt():
    msg = simpledialog.askstring("Encrypt", "Enter the message to encrypt:")
    if not msg:
        return
    # If input looks numeric (only digits and spaces), warn user
    if re.fullmatch(r'[\d\s]+', msg):
        messagebox.showwarning("Input looks numeric", "Input looks like numeric ciphertext — use 'Decrypt' instead.")
        return
    encrypted_msg, seed = encrypt(msg)
    # write numeric ciphertext + seed next to this script so location is predictable
    base_dir = os.path.dirname(os.path.abspath(__file__))
    encrypted_path = os.path.join(base_dir, "encrypted_message.txt")
    try:
        with open(encrypted_path, "w", encoding="utf-8") as f:
            f.write(encrypted_msg + "\n")
            f.write(f"Seed: {seed}\n")
    except Exception as e:
        messagebox.showerror("File write error", f"Failed to write encrypted file: {e}")
        return
    # copy seed to clipboard
    window.clipboard_clear()
    window.clipboard_append(str(seed))
    window.update()  # ensure clipboard updated on Windows
    # inform user with the full path
    messagebox.showinfo(
        "Encrypted",
        f"Encrypted message saved to:\n{encrypted_path}\n\nSeed has been copied to the clipboard."
    )

def ask_and_decrypt():
    encrypted_msg = simpledialog.askstring("Decrypt", "Enter the encrypted message (space-separated numbers):")
    if not encrypted_msg:
        return
    seed = simpledialog.askinteger("Seed", "Enter the seed (the number shown after encryption):")
    if seed is None:
        return
    try:
        decrypted = decrypt(encrypted_msg, seed)
        messagebox.showinfo("Decrypted", decrypted)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def encrypt_file_from_entry():
    txtfile = file_entry.get().strip()
    if not txtfile:
        messagebox.showwarning("No file", "Please enter a file name in the box above.")
        return
    try:
        encrypted_path, seed = encryptfile(txtfile)
        # copy seed to clipboard
        window.clipboard_clear()
        window.clipboard_append(str(seed))
        window.update()
        messagebox.showinfo("File Encrypted",
                            f"Encrypted file written to: {encrypted_path}\nSeed: {seed}\n(The seed was copied to clipboard.)")
    except FileNotFoundError as e:
        messagebox.showerror("File not found", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file_from_entry():
    txtfile = file_entry.get().strip()
    if not txtfile:
        messagebox.showwarning("No file", "Please enter a file name in the box above.")
        return
    # Try to decrypt using seed found in file; if not present, ask user
    try:
        try:
            decrypted_path, plaintext = decryptfile(txtfile, provided_seed=None)
        except ValueError:
            # seed not in file, ask user
            seed = simpledialog.askinteger("Seed required", "Seed not found in file. Enter the seed:")
            if seed is None:
                return
            decrypted_path, plaintext = decryptfile(txtfile, provided_seed=seed)
        messagebox.showinfo("File Decrypted", f"Decrypted file written to: {decrypted_path}")
    except FileNotFoundError as e:
        messagebox.showerror("File not found", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# buttons frame
btn_frame = ttk.Frame(window, padding=20)
btn_frame.pack()

button_encrypt = ttk.Button(
    master=btn_frame,
    text="Encrypt (message)",
    command=ask_and_encrypt
)
button_encrypt.grid(row=0, column=0, padx=8, pady=6)

button_decrypt = ttk.Button(
    master=btn_frame,
    text="Decrypt (message)",
    command=ask_and_decrypt
)
button_decrypt.grid(row=0, column=1, padx=8, pady=6)

button_encrypt_file = ttk.Button(
    master=btn_frame,
    text="Encrypt File",
    command=encrypt_file_from_entry
)
button_encrypt_file.grid(row=1, column=0, padx=8, pady=6)

button_decrypt_file = ttk.Button(
    master=btn_frame,
    text="Decrypt File",
    command=decrypt_file_from_entry
)
button_decrypt_file.grid(row=1, column=1, padx=8, pady=6)

window.mainloop()
