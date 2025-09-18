# 📑 PDF Merger – Flask Web App

A simple Flask web application that lets users **upload multiple PDF files** and merge them into a single PDF that can be downloaded instantly.

---

## 🚀 Features
- Upload **multiple PDF files** at once.
- Merge them into a single PDF with one click.
- Clean, responsive UI (Bootstrap/CSS ready).
- Files are processed on the server and returned immediately.

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask** (web framework)
- **PyPDF2** (PDF merging)

---

## 📂 Project Structure
project/
│ app.py # Flask backend
│ requirements.txt # Dependencies
│ README.md
├─ templates/
│ └─ index.html # Frontend page
├─ static/
│ └─ style.css # Optional custom styling
└─ uploads/ # Temporary PDF storage (ignored in Git)

yaml
Copy code

---

## ⚡ Setup & Run Locally

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/pdf-merger.git
cd pdf-merger
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the App
bash
Copy code
python app.py
Open your browser and go to:
➡️ http://127.0.0.1:5000

📝 Requirements
Contents of requirements.txt:

nginx
Copy code
Flask
PyPDF2
💡 Future Improvements
Drag & drop file upload

Merge order customization

Progress indicator during merging

yaml
Copy code

---

### ✅ Next Step to Push
After saving this new README:


git add README.md
git commit -m "Update README with better formatting and instructions"
git push