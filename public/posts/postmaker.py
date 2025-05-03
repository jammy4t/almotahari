import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import os

def get_next_filename():
    i = 1
    while os.path.exists(f"{i}.md"):
        i += 1
    return f"{i}.md"

def save_file():
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+03:00")
    data = {key: var.get() for key, var in entry_vars.items()}
    content = text_area.get("1.0", tk.END).strip()

    filename = get_next_filename()
    with open(filename, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'title: "{data["title"]}"\n')
        f.write(f"date: {now}\n")
        f.write(f'draft: {data["draft"]}\n')
        f.write(f'ShowToc: {data["ShowToc"]}\n')
        f.write("cover:\n")
        f.write(f'    image: {data["image"]}\n')
        f.write(f'    alt: {data["alt"]}\n')
        f.write(f'    caption: {data["caption"]}\n')
        f.write(f'    hidden: {data["hidden"]}\n')
        f.write(f'summary: {data["summary"]}\n')
        f.write(f'tags: {data["tags"]}\n')
        f.write(f'categories: {data["categories"]}\n')
        f.write(f'books: {data["books"]}\n')
        f.write("---\n\n")
        f.write(content)
    print(f"تم حفظ الملف باسم {filename}")

root = tk.Tk()
root.title("منشئ ملفات Markdown")
root.geometry("800x750")
root.configure(bg="#f4f4f4")

entry_vars = {
    "title": tk.StringVar(),
    "draft": tk.StringVar(value="false"),
    "ShowToc": tk.StringVar(value="false"),
    "image": tk.StringVar(value="img/01.jpg"),
    "alt": tk.StringVar(value="'صورة'"),
    "caption": tk.StringVar(value="''"),
    "hidden": tk.StringVar(value="false"),
    "summary": tk.StringVar(),
    "tags": tk.StringVar(value="[]"),
    "categories": tk.StringVar(value="[]"),
    "books": tk.StringVar(value='["كتابة بحوث"]')
}

labels = [
    ("---", None),
    ("title:", "title"),
    ("date:", None),
    ("draft:", "draft"),
    ("ShowToc:", "ShowToc"),
    ("cover:", None),
    ("image:", "image"),
    ("alt:", "alt"),
    ("caption:", "caption"),
    ("hidden:", "hidden"),
    ("summary:", "summary"),
    ("tags:", "tags"),
    ("categories:", "categories"),
    ("books:", "books"),
    ("---", None)
]

for i, (label_text, var_key) in enumerate(labels):
    tk.Label(root, text=label_text, anchor="w", bg="#f4f4f4").grid(row=i, column=0, sticky="w", padx=10, pady=2)
    if var_key:
        tk.Entry(root, textvariable=entry_vars[var_key], width=70).grid(row=i, column=1, padx=10, pady=2)
    elif label_text == "date:":
        date_value = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+03:00")
        tk.Label(root, text=date_value, anchor="w", bg="#f4f4f4").grid(row=i, column=1, sticky="w", padx=10, pady=2)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=95, height=10)
text_area.grid(row=len(labels), column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="تنفيذ", bg="#333", fg="white", command=save_file).grid(row=len(labels)+1, column=0, columnspan=2, pady=10)

root.mainloop()
