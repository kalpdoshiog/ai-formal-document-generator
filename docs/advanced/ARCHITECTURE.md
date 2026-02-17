# Project Architecture Overview

## 📊 Request Flow Diagram

```
User Browser
     ↓
[Django URLs] ──→ generator/urls.py
     ↓
[View Layer] ──→ generator/views/
     │             ├── home.py
     │             ├── circular.py
     │             ├── office_order.py
     │             └── policy.py
     │
     ├──→ [Services] ──→ generator/services/
     │                    ├── ai_service.py (Google Gemini)
     │                    └── data_loader.py (JSON files)
     │
     ├──→ [Data] ──→ generator/data/
     │                └── constants.py (Designations)
     │
     ├──→ [Utils] ──→ generator/utils_new/
     │                └── formatters.py
     │
     └──→ [Templates] ──→ generator/templates/
                          ├── HTML Forms
                          └── PDF Templates
                               ↓
                          [Export]
                          ├── PDF (WeasyPrint)
                          └── DOCX (python-docx)
```

## 🗂️ Directory Tree (Organized)

```
ai_formal_generator/
│
├── 📋 Documentation
│   ├── README.md                    # Main documentation
│   ├── STRUCTURE.md                 # Quick file reference
│   ├── MIGRATION.md                 # Restructuring changes
│   ├── DEVELOPER_GUIDE.md           # Development guide
│   └── ARCHITECTURE.md              # This file
│
├── ⚙️ Configuration
│   ├── .env.example                 # Environment template
│   ├── .gitignore                   # Git ignore rules
│   ├── requirements.txt             # Python dependencies
│   └── config/                      # JSON configs
│       ├── circular.json
│       ├── office_order.json
│       ├── policy.json
│       ├── advertisement.json
│       └── purschase_order.json
│
├── 🌐 Django Project (ai_formal_generator/)
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # Root URL config
│   ├── wsgi.py                      # WSGI server
│   └── asgi.py                      # ASGI server
│
├── 📱 Application (generator/)
│   │
│   ├── 📊 Data Layer
│   │   └── data/
│   │       ├── __init__.py
│   │       └── constants.py         # DESIGNATION_MAP
│   │
│   ├── 🔧 Service Layer
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── ai_service.py        # Google Gemini AI
│   │       └── data_loader.py       # JSON loaders
│   │
│   ├── 🛠️ Utility Layer
│   │   └── utils_new/
│   │       ├── __init__.py
│   │       └── formatters.py        # Date/text formatters
│   │
│   ├── 🎯 View Layer
│   │   └── views/
│   │       ├── __init__.py
│   │       ├── home.py              # Home page
│   │       ├── circular.py          # Circular CRUD
│   │       ├── office_order.py      # Office Order CRUD
│   │       ├── policy.py            # Policy CRUD
│   │       └── helpers.py           # (Deprecated)
│   │
│   ├── 🎨 Presentation Layer
│   │   ├── templates/generator/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── *_form.html
│   │   │   ├── result_*.html
│   │   │   └── pdf_*.html
│   │   │
│   │   └── fonts/
│   │       └── Noto*.ttf
│   │
│   ├── 💾 Data Layer
│   │   ├── models.py                # DocumentLog model
│   │   └── migrations/
│   │
│   └── 🔌 Configuration
│       ├── admin.py                 # Django admin
│       ├── apps.py                  # App config
│       └── urls.py                  # App URLs
│
├── 🎨 Static Files (static/generator/)
│   ├── style.css
│   ├── bisag_logo.png
│   └── bisag_img1.jpg
│
└── 🗄️ Runtime Files
    ├── db.sqlite3                   # Database
    ├── debug.log                    # Application logs
    └── manage.py                    # Django CLI
```

## 🔄 Data Flow for Document Generation

### 1. Circular Generation Flow

```
[User] → Fill Form
   ↓
[View: circular.py]
   ├→ Generate Body?
   │   ├→ [ai_service.py] → Google Gemini → AI Generated Text
   │   └→ Return to Form
   │
   └→ Submit Form
       ├→ [data_loader.py] → Load config/circular.json
       ├→ [formatters.py] → Format dates & designations
       ├→ [constants.py] → Get designation translations
       │
       └→ Render Preview
           ├→ Display HTML Preview
           │
           └→ Download?
               ├→ PDF: templates/pdf_circular.html → WeasyPrint → PDF
               └→ DOCX: python-docx → DOCX file
```

### 2. Office Order Generation Flow

```
[User] → Fill Form → Submit
   ↓
[View: office_order.py]
   ├→ [data_loader.py] → config/office_order.json
   ├→ [ai_service.py] → AI Body (optional)
   ├→ [formatters.py] → Date formatting
   │
   └→ Export
       ├→ PDF: templates/pdf_office_order.html → WeasyPrint
       └→ DOCX: python-docx
```

### 3. Policy Generation Flow

```
[User] → Fill Form → Submit
   ↓
[View: policy.py]
   ├→ [data_loader.py] → config/policy.json
   ├→ [ai_service.py] → AI Body (optional)
   ├→ [formatters.py] → Date formatting
   │
   └→ Export
       ├→ PDF: templates/pdf_policy.html → WeasyPrint → PyPDF2
       └→ DOCX: python-docx
```

## 🎯 Design Patterns Used

### 1. **Separation of Concerns**
- **Views**: Handle HTTP & business logic
- **Services**: Handle external integrations (AI, data)
- **Utils**: Reusable helper functions
- **Data**: Static constants and models

### 2. **Service Layer Pattern**
```python
# Services are separate from views
from generator.services.ai_service import get_gemini_model
from generator.services.data_loader import get_circular_data
```

### 3. **Template Method Pattern**
All document types follow similar workflow:
1. Form input
2. AI generation (optional)
3. Preview
4. Export (PDF/DOCX)

### 4. **Lazy Loading**
```python
@lru_cache(maxsize=1)
def get_circular_data():
    # Loads JSON only once, then cached
```

### 5. **Factory Pattern**
```python
def get_gemini_model():
    # Single instance created and reused
    global _gemini_model
    if _gemini_model is None:
        _gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")
    return _gemini_model
```

## 🔐 Security Layers

```
Environment Variables (.env)
    ↓
settings.py
    ↓
CSRF Protection (Django Middleware)
    ↓
Views (Request validation)
    ↓
Services (API key management)
    ↓
External APIs (Google Gemini)
```

## 📈 Scalability Considerations

### Current Structure Supports:
✅ Adding new document types easily
✅ Swapping AI providers (just change ai_service.py)
✅ Multiple export formats (PDF, DOCX, future: ODT, HTML)
✅ Multi-language support (English, Hindi, future: more)
✅ Microservice migration (services can be separated)

### Future Enhancements:
- Move services to separate microservices
- Add caching layer (Redis)
- Queue system for document generation (Celery)
- API endpoints for external integrations
- Database backend for configurations (instead of JSON)

## 🧩 Module Dependencies

```
Views Layer
    ↓
├── Services Layer (External integrations)
│   ├── ai_service.py → google.generativeai
│   └── data_loader.py → JSON files
│
├── Utils Layer (Helpers)
│   └── formatters.py → datetime
│
└── Data Layer (Constants & Models)
    ├── constants.py → Static data
    └── models.py → Database
```

## 📝 File Naming Convention

```
Type                  Naming Pattern           Example
─────────────────────────────────────────────────────────
Python Modules        snake_case.py            ai_service.py
Classes               PascalCase               DocumentLog
Functions             snake_case()             get_circular_data()
Constants             UPPER_CASE               DESIGNATION_MAP
Templates             snake_case.html          pdf_circular.html
Config Files          snake_case.json          office_order.json
CSS Files             kebab-case.css           style.css
```

## 🎨 Frontend Architecture

```
base.html (Common layout)
    ↓
home.html (Document selector)
    ↓
{type}_form.html (Input form)
    ↓
result_{type}.html (Preview)
    ↓
Download Links
    ├→ PDF: pdf_{type}.html (WeasyPrint template)
    └→ DOCX: Generated by python-docx
```

---

**Last Updated:** February 17, 2026
**Django Version:** 5.x
**Python Version:** 3.8+

