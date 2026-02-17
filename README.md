# AI Formal Document Generator

A Django-based application for generating formal documents (Circulars, Office Orders, Policies) using Google Gemini AI with support for English and Hindi languages.

---

## 📚 Documentation

**All documentation has been organized for easy navigation!**

### 🚀 Start Here

👉 **[Go to Documentation →](docs/INDEX.md)**

The documentation is organized by skill level:

- **🟢 Beginner** - New to the project? Setup guides & quick navigation
- **🟡 Intermediate** - Ready to develop? Complete development guides
- **🔴 Advanced** - Deep dive into architecture & design patterns
- **📖 Reference** - Quick file lookups and references

---

## ⚡ Quick Start

1. **Set up environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Add your `GEMINI_API_KEY`

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start server:**
   ```bash
   python manage.py runserver
   ```

5. **Visit:** `http://localhost:8000`

---

## 📁 Project Structure

```
ai_formal_generator/
├── docs/                    # 📚 All documentation (START HERE!)
│   ├── INDEX.md            # Documentation hub
│   ├── beginner/           # Beginner guides
│   ├── intermediate/       # Developer guides
│   ├── advanced/           # Architecture docs
│   └── reference/          # Quick references
│
├── config/                  # JSON configuration files
├── generator/               # Main Django app
│   ├── data/               # Constants & static data
│   ├── services/           # External services (AI, data loading)
│   ├── utils_new/          # Utility functions
│   ├── views/              # View controllers
│   ├── templates/          # HTML templates
│   └── fonts/              # Custom fonts
│
├── static/                  # Static files (CSS, images)
├── ai_formal_generator/     # Django project settings
└── manage.py               # Django CLI
```

---

## 🔍 Quick Links

| Need to... | Go to... |
|-----------|----------|
| **Setup the project** | [docs/beginner/README.md](docs/beginner/README.md) |
| **Find a file** | [docs/beginner/QUICK_NAVIGATION.md](docs/beginner/QUICK_NAVIGATION.md) |
| **Add a feature** | [docs/intermediate/DEVELOPER_GUIDE.md](docs/intermediate/DEVELOPER_GUIDE.md) |
| **Understand architecture** | [docs/advanced/ARCHITECTURE.md](docs/advanced/ARCHITECTURE.md) |

---

## 🎯 Features

- ✅ Generate Circulars, Office Orders, and Policies
- ✅ AI-powered content generation using Google Gemini
- ✅ Multi-language support (English & Hindi)
- ✅ Export to PDF and DOCX formats
- ✅ Document logging and tracking
- ✅ Custom fonts for Hindi text
- ✅ Professional templates

---

## 📦 Tech Stack

- **Backend:** Django 5.x
- **AI:** Google Gemini API
- **PDF Generation:** WeasyPrint, ReportLab
- **DOCX Generation:** python-docx
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, JavaScript

---

## 📖 Documentation Index

All documentation is in the `/docs` folder, organized by level:

### 🟢 Beginner
- **README.md** - Complete setup guide
- **QUICK_NAVIGATION.md** - Find files fast
- **RESTRUCTURE_SUMMARY.md** - Project overview

### 🟡 Intermediate  
- **DEVELOPER_GUIDE.md** - Development guide
- **MIGRATION.md** - Change history

### 🔴 Advanced
- **ARCHITECTURE.md** - System architecture

### 📖 Reference
- **STRUCTURE.md** - File locations

---

## 🚀 Next Steps

1. **Read the docs:** [docs/INDEX.md](docs/INDEX.md)
2. **Explore the code:** Check out the organized structure
3. **Run the app:** Follow the quick start above
4. **Start developing:** Use the developer guide

---

## 📞 Need Help?

Check the documentation in order:
1. [docs/beginner/QUICK_NAVIGATION.md](docs/beginner/QUICK_NAVIGATION.md) - Find files
2. [docs/reference/STRUCTURE.md](docs/reference/STRUCTURE.md) - File reference  
3. [docs/intermediate/DEVELOPER_GUIDE.md](docs/intermediate/DEVELOPER_GUIDE.md) - Development help

---

**Version:** 2.0 (Reorganized)  
**Last Updated:** February 17, 2026  
**Python:** 3.8+  
**Django:** 5.x

---

## 👉 **[Start with the Documentation →](docs/INDEX.md)**

