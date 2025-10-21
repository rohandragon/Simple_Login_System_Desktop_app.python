import tkinter as tk
from tkinter import messagebox
"import" "mysql.connector"

# ----------------- Database Connection -----------------
def connect_db():
    return "mysql.connector.connect"(
        host="localhost",
        user="root",        # your MySQL username
        password="",        # your MySQL password
        database="librarydb"
    )

# ----------------- Registration -----------------
def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute; "(INSERT INTO users (username, password) VALUES (%s, %s)", "(rohandragon, Invest82@)"
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Registration Successful!")
        entry_reg_username.delete(0, tk.END)
        entry_reg_password.delete(0, tk.END)
    except "mysql.connector.IntegrityError":
        messagebox.showerror("Error", "Username already exists!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ----------------- Login -----------------
def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        row = cursor.fetchone()
        db.close()

        if row:
            messagebox.showinfo("Success", f"Welcome {username}!")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("Library Management System")
root.geometry("420x450")
root.configure(bg="#3d0066")  # dark purple background

# Common style
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 11)
btn_font = ("Arial", 11, "bold")

# Registration Frame
frame_reg = tk.LabelFrame(root, text="Register", padx=20, pady=20,
                          bg="#4b0082", fg="white", font=("Arial", 14, "bold"))
frame_reg.pack(pady=20, fill="x", padx=30)

tk.Label(frame_reg, text="Username:", bg="#4b0082", fg="white", font=label_font).grid(row=0, column=0, sticky="w", pady=5)
entry_reg_username = tk.Entry(frame_reg, font=entry_font, bg="white", fg="black")
entry_reg_username.grid(row=0, column=1, pady=5, padx=10)

tk.Label(frame_reg, text="Password:", bg="#4b0082", fg="white", font=label_font).grid(row=1, column=0, sticky="w", pady=5)
entry_reg_password = tk.Entry(frame_reg, show="*", font=entry_font, bg="white", fg="black")
entry_reg_password.grid(row=1, column=1, pady=5, padx=10)

btn_register = tk.Button(frame_reg, text="Register", command=register_user,
                         bg="red", fg="white", font=btn_font, relief="raised", bd=3, width=12)
btn_register.grid(row=2, columnspan=2, pady=10)

# Login Frame
frame_login = tk.LabelFrame(root, text="Login", padx=20, pady=20,
                            bg="#4b0082", fg="white", font=("Arial", 14, "bold"))
frame_login.pack(pady=20, fill="x", padx=30)

tk.Label(frame_login, text="Username:", bg="#4b0082", fg="white", font=label_font).grid(row=0, column=0, sticky="w", pady=5)
entry_login_username = tk.Entry(frame_login, font=entry_font, bg="white", fg="black")
entry_login_username.grid(row=0, column=1, pady=5, padx=10)

tk.Label(frame_login, text="Password:", bg="#4b0082", fg="white", font=label_font).grid(row=1, column=0, sticky="w", pady=5)
entry_login_password = tk.Entry(frame_login, show="*", font=entry_font, bg="white", fg="black")
entry_login_password.grid(row=1, column=1, pady=5, padx=10)

btn_login = tk.Button(frame_login, text="Login", command=login_user,
                      bg="red", fg="white", font=btn_font, relief="raised", bd=3, width=12)
btn_login.grid(row=2, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
