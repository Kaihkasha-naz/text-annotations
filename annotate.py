import tkinter as tk
import pandas as pd

# === Load and Clean Text Data ===
with open('data.txt', 'r', encoding='utf-8') as file:
    text_data = [line.strip() for line in file if line.strip()]  # remove empty lines

# === Handle Empty File ===
if not text_data:
    print("❌ 'data.txt' is empty. Please add text lines to annotate.")
    exit()

annotations = []
index = 0

# === UI Setup ===
root = tk.Tk()
root.title("Text Annotation Tool")

text_box = tk.Text(root, height=10, width=80, font=("Arial", 12), wrap="word")
text_box.pack(pady=10)

label_entry = tk.Entry(root, font=("Arial", 12))
label_entry.pack(pady=5)

def next_text():
    global index
    label = label_entry.get().strip()

    if label:
        annotations.append({
            "text": text_data[index],
            "label": label
        })

    label_entry.delete(0, tk.END)
    index += 1

    if index < len(text_data):
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text_data[index])
    else:
        # ✅ NO Indentation Errors Here
        df = pd.DataFrame(annotations)
        print(f"Saving {len(annotations)} annotations to file...")
        df.to_csv("annotations.csv", index=False, encoding='utf-8')
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "✅ Annotation completed and saved to annotations.csv!")
        label_entry.destroy()
        next_button.destroy()

next_button = tk.Button(root, text="Next", command=next_text, font=("Arial", 12))
next_button.pack(pady=10)

# === Start with the first sentence ===
text_box.insert(tk.END, text_data[index])

root.mainloop()
