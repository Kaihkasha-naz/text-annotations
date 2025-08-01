# 📝 Text Annotation Tool (Tkinter + Python)

A simple GUI-based text annotation tool built with Python and Tkinter.  
Use it to assign custom labels (like sentiment, categories, tags, etc.) to each line of text in a file.

---

## 📌 Features

- Easy-to-use text labeling interface
- Assign custom labels (e.g., positive/negative, spam/ham, etc.)
- Output saved to `annotations.csv`
- Warning message if no label is entered
- Built with Python and Tkinter

---

## 🚀 Demo

![screenshot](assets/demo.png)  <!-- Optional: Add a screenshot of the GUI -->

---

## 🗃️ Project Structure

text-annotations/
│
├── data.txt # Input text file (one line = one sentence)
├── annotations.csv # Output CSV file (auto-generated after annotation)
├── annotate.py # Main Python script
└── README.md # This file
How to Use
Prepare your text file
Create a data.txt file with one sentence per line.

txt
Copy
Edit
I love this product.
It didn’t meet my expectations.
Excellent service.
Worst experience ever.
Run the tool

bash
Copy
Edit
python annotate.py
Annotate each line

Type a label (like positive, negative, etc.)

Click “Next”

Repeat for all lines

Output will be saved to annotations.csv

📤 Sample Output (annotations.csv)
csv
Copy
Edit
text,label
I love this product.,positive
It didn’t meet my expectations.,negative
Excellent service.,positive
Worst experience ever.,negative

🧠 Use Cases
Sentiment analysis datasets

Text classification

Spam detection

Chatbot training data

⚠️ Notes
You must enter a label for every sentence — blank entries will not be accepted.

data.txt should not be empty. The app will exit if no text is found.

📌 To-Do (Future Improvements)
 Add dropdown for label selection

 Add "Back" button to edit previous annotation

 Export to JSON format

 Keyboard shortcuts (e.g., Enter to proceed)

📜 License
This project is open-source and free to use under the MIT License.


### ✅ To Use:

Commit and push to GitHub:

bash
Copy
Edit
git add README.md
git commit -m "Add project README"
git push
