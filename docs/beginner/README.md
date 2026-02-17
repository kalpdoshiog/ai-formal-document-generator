# AI Formal Document Generator

A Django-based application for generating formal documents (Circulars, Office Orders, Policies) using Google Gemini AI.

## 📁 Project Structure

```
ai_formal_generator/
├── config/                          # Configuration files
│   ├── circular.json                # Circular document configuration
│   ├── office_order.json            # Office order configuration
│   ├── policy.json                  # Policy document configuration
│   ├── advertisement.json           # Advertisement configuration
│   └── purschase_order.json         # Purchase order configuration
│
├── ai_formal_generator/             # Django project settings
│   ├── __init__.py
│   ├── settings.py                  # Main settings file
│   ├── urls.py                      # Root URL configuration
│   ├── wsgi.py                      # WSGI configuration
│   └── asgi.py                      # ASGI configuration
│
├── generator/                       # Main application
│   ├── data/                        # Data models and constants
│   │   ├── __init__.py
│   │   └── constants.py             # Designation mappings and constants
│   │
│   ├── services/                    # External services
│   │   ├── __init__.py
│   │   ├── ai_service.py            # Google Gemini AI integration
│   │   └── data_loader.py           # JSON data loading utilities
│   │
│   ├── utils_new/                   # Utility functions
│   │   ├── __init__.py
│   │   └── formatters.py            # Date and text formatters
│   │
│   ├── views/                       # View controllers
│   │   ├── __init__.py
│   │   ├── home.py                  # Home page view
│   │   ├── circular.py              # Circular document views
│   │   ├── office_order.py          # Office order views
│   │   ├── policy.py                # Policy document views
│   │   └── helpers.py               # (Deprecated - for backward compatibility)
│   │
│   ├── templates/                   # HTML templates
│   │   └── generator/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── circular_form.html
│   │       ├── result_circular.html
│   │       ├── pdf_circular.html
│   │       └── ...
│   │
│   ├── fonts/                       # Custom fonts
│   │   ├── NotoSansDevanagari-Bold.ttf
│   │   ├── NotoSansDevanagari-Regular.ttf
│   │   └── ...
│   │
│   ├── migrations/                  # Database migrations
│   ├── models.py                    # Database models
│   ├── admin.py                     # Admin configuration
│   ├── apps.py                      # App configuration
│   ├── urls.py                      # App URL patterns
│   └── tests.py                     # Tests
│
├── static/                          # Static files
│   └── generator/
│       ├── bisag_img1.jpg
│       ├── bisag_logo.png
│       └── style.css
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── db.sqlite3                       # SQLite database
└── debug.log                        # Application logs
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open browser:**
   Navigate to `http://localhost:8000`

## 📝 File Locations Guide

### Need to modify...

#### **Document Templates?**
- Location: `generator/templates/generator/`
- Files: `pdf_circular.html`, `pdf_office_order.html`, `pdf_policy.html`

#### **AI Generation Logic?**
- Location: `generator/services/ai_service.py`
- Function: `get_gemini_model()`

#### **Data Loading?**
- Location: `generator/services/data_loader.py`
- Functions: `get_circular_data()`, `get_office_order_data()`, `get_policy_data()`

#### **Document Configuration?**
- Location: `config/`
- Files: `circular.json`, `office_order.json`, `policy.json`

#### **Designation Mappings?**
- Location: `generator/data/constants.py`
- Variable: `DESIGNATION_MAP`

#### **Date/Text Formatting?**
- Location: `generator/utils_new/formatters.py`
- Functions: `format_date_ddmmyyyy()`, `safe_designation()`

#### **View Logic (Circular)?**
- Location: `generator/views/circular.py`
- Functions: `generate_circular_body()`, `result_circular()`, `download_circular_pdf()`

#### **View Logic (Office Order)?**
- Location: `generator/views/office_order.py`
- Functions: `generate_body()`, `result_office_order()`, `download_pdf()`

#### **View Logic (Policy)?**
- Location: `generator/views/policy.py`
- Functions: `generate_policy_body()`, `result_policy()`, `download_policy_pdf()`

#### **Styling?**
- Location: `static/generator/style.css`

#### **Database Models?**
- Location: `generator/models.py`

#### **URL Routes?**
- Location: `generator/urls.py` (app routes)
- Location: `ai_formal_generator/urls.py` (project routes)

#### **Settings?**
- Location: `ai_formal_generator/settings.py`

## 🔧 Key Features

- **Multi-language Support**: English and Hindi
- **AI-Powered Content Generation**: Using Google Gemini
- **Multiple Document Types**: Circulars, Office Orders, Policies
- **Export Options**: PDF and DOCX formats
- **Document Logging**: Track generated documents

## 📦 Dependencies

- **Django**: Web framework
- **google-generativeai**: Google Gemini AI integration
- **reportlab**: PDF generation
- **python-docx**: DOCX generation
- **weasyprint**: HTML to PDF conversion
- **PyPDF2**: PDF manipulation
- **Pillow**: Image processing

## 🛠️ Development Tips

1. **Adding a new document type:**
   - Create new view in `generator/views/`
   - Add configuration JSON in `config/`
   - Add data loader function in `generator/services/data_loader.py`
   - Create HTML templates in `generator/templates/generator/`
   - Add URL routes in `generator/urls.py`

2. **Modifying AI prompts:**
   - Edit the view file for the document type
   - Look for `system_prompt` variable in `generate_*_body()` functions

3. **Changing PDF styling:**
   - Edit the `pdf_*.html` templates
   - Use inline CSS or modify the WeasyPrint CSS settings

## 📄 License

[Add your license here]

## 👥 Contributors

[Add contributors here]

## 📞 Support

[Add support contact information here]

