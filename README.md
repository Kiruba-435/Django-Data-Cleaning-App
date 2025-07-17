# 🧼 SmartClean — Django Data Cleaning App

SmartClean is a web-based data cleaning tool built with Django and pandas. It allows users to securely upload CSV files, toggle preprocessing options, preview cleaned data, and download the result—all through a modern, user-friendly interface.

---

## 🧼 App Link

**🔗 Live App**: https://django-data-cleaning-app.onrender.com **

SmartClean is a web-based data cleaning tool built with Django and pandas...


## 🚀 Features

- 🔐 User authentication (register/login/logout)
- 📁 CSV upload with file validation
- ⚙️ Toggle-based cleaning options:
  - ✨ Handle missing values
  - 🚀 Remove outliers (IQR)
  - 🔤 Label encode categoricals
  - 🗑️ Drop duplicates
- 📊 Cleaning summary report
- 🧪 Preview of cleaned data (first 5 rows)
- 📥 Download cleaned dataset
- 🎨 Light-themed UI with emoji-enhanced toggles

---

## 🛠 Tech Stack

- **Backend**: Django, pandas, scikit-learn
- **Frontend**: HTML, CSS (custom light theme)
- **Deployment**: Render 
- **Extras**: WhiteNoise for static files, Gunicorn for production

---

## 🧪 Local Setup

## Install dependencies
pip install -r requirements.txt

## Run migrations
python manage.py migrate

## Collect static files
python manage.py collectstatic

## Start the server
python manage.py runserver


