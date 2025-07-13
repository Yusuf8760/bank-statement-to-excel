from flask import Flask, render_template, request, send_file
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf_file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Dummy Excel Output
            data = {
                'Date': ['01-01-2025', '02-01-2025'],
                'Description': ['Salary Credit', 'ATM Withdrawal'],
                'Credit': [25000, ''],
                'Debit': ['', 5000],
            }
            df = pd.DataFrame(data)
            excel_path = os.path.join(OUTPUT_FOLDER, 'converted.xlsx')
            df.to_excel(excel_path, index=False)

            return send_file(excel_path, as_attachment=True)

    return render_template('index.html')
