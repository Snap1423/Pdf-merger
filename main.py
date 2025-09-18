from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfWriter
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merge", methods=["POST"])
def merge():
    if "pdfs" not in request.files:
        return "No files uploaded!", 400

    files = request.files.getlist("pdfs")
    if not files or files[0].filename == "":
        return "No files selected!", 400

    merger = PdfWriter()

    for file in files:
        single_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(single_path)
        print("Merging:", single_path)  # debug
        merger.append(single_path)

    output_path = os.path.join(UPLOAD_FOLDER, "merged.pdf")
    merger.write(output_path)
    merger.close()

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)