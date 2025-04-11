# 💼 Gross → Net Salary Calculator

This app helps calculate **Net Salary** based on **Gross Salary** and the **Number of Dependents** using a FastAPI backend and a Streamlit frontend. It supports single inputs and batch processing via uploaded files.

---

## 📁 Project Structure

```
Gross-2-Salary/
│
├── packages/
│   └── dev_ui/
│       └── src/
│           └── dev_ui/
│               └── ui/
│                   ├── pages/
│                   │   ├── Homepage.py
│                   │   ├── GrossNetPage.py
│                   │   └── UploadFilesPage.py
│                   └── __init__.py
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── salary.py
│   ├── core/
│   │   └── logic/
│   │       └── salary.py
│   └── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/gross-net-calculator.git
cd Gross-2-Salary
```

---

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, here’s a basic one:

```txt
fastapi
uvicorn
streamlit
requests
pandas
openpyxl
python-multipart
```

---

### 4. Run the FastAPI Backend

```bash
PYTHONPATH=src uvicorn cat.api.main:app --reload
```

This will start the backend at:

```
http://localhost:8000
```



---

### 5. Run the Streamlit Frontend

```bash
# Make sure to set PYTHONPATH so the UI can resolve internal modules
PYTHONPATH=packages/dev_ui/src streamlit run packages/dev_ui/src/dev_ui/ui/pages/Homepage.py
```

This will launch the web UI in your browser at:

```
http://localhost:8501
```

---

## 🧠 Features

- ✅ Calculate net salary from single gross input
- 📁 Upload CSV or Excel to process bulk salary data
- 📥 Download result with net salaries included
- 🚀 FastAPI + Streamlit + Modular folder structure

---

## ⚙️ Fix Import Errors

Ensure these files exist to fix any import issues with Python modules:

```bash
touch packages/dev_ui/src/__init__.py
touch packages/dev_ui/src/dev_ui/__init__.py
touch packages/dev_ui/src/dev_ui/ui/__init__.py
touch packages/dev_ui/src/dev_ui/ui/pages/__init__.py
```

---

## 👨‍💻 Developed by

**Benjamin Dao** – A passionate DevOps engineer from Vietnam 🇻🇳  
📧 daominhphuc05@gmail.com  
🏓 Loves Linux and table tennis!

---
