import tkinter as tk

def calculate_interest(event=None):
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_entry.get()) / 100 
        time = float(time_entry.get())

        interest = principal * interest_rate * time
        result_text.delete(0, tk.END)
        result_text.insert(tk.END, f"${interest:.2f}")
    except ValueError:
        pass


root = tk.Tk()
root.title("Tk")


tk.Label(root, text="Principal").grid(row=0, column=0)
tk.Label(root, text="Interest").grid(row=0, column=1)
tk.Label(root, text="Years").grid(row=0, column=2)
tk.Label(root, text="Amount").grid(row=3, column=0)



principal_entry = tk.Entry(root)
principal_entry.grid(row=1, column=0)
interest_entry = tk.Entry(root)
interest_entry.grid(row=1, column=1)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=2)
result_text = tk.Entry(root)
result_text.grid(row=3, column=1)

for entry in [principal_entry, interest_entry, time_entry]:
    entry.bind("<KeyRelease>", calculate_interest)

root.mainloop()
