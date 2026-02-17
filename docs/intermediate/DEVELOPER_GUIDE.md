# 📚 Developer Guide

## Project Overview

This is a Django application that generates formal documents (Circulars, Office Orders, Policies) using AI assistance from Google Gemini. Documents support both English and Hindi languages and can be exported as PDF or DOCX.

---

## 🗂️ Folder Organization

### `/config` - Configuration Files
**Purpose:** Store all JSON configuration data separately from code

**Files:**
- `circular.json` - People, templates for circular documents
- `office_order.json` - Configuration for office orders
- `policy.json` - Policy document settings
- `advertisement.json` - Advertisement templates
- `purschase_order.json` - Purchase order data

**When to modify:** When adding new people, changing templates, or updating document structure.

---

### `/generator/data` - Data Models & Constants
**Purpose:** Store static data and constants used throughout the app

**Files:**
- `constants.py` - DESIGNATION_MAP with English/Hindi translations

**When to modify:** When adding new designations or updating translations.

---

### `/generator/services` - External Service Integrations
**Purpose:** Handle external APIs and data loading

**Files:**
- `ai_service.py` - Google Gemini AI integration
  - `get_gemini_model()` - Initialize and return AI model
  
- `data_loader.py` - JSON configuration loaders
  - `get_circular_data()` - Load circular config
  - `get_office_order_data()` - Load office order config
  - `get_policy_data()` - Load policy config
  - `get_advertisement_data()` - Load advertisement config
  - `get_purchase_order_data()` - Load purchase order config

**When to modify:** 
- Changing AI model or prompts → `ai_service.py`
- Adding new data sources → `data_loader.py`

---

### `/generator/utils_new` - Utility Functions
**Purpose:** Reusable helper functions

**Files:**
- `formatters.py`
  - `format_date_ddmmyyyy(date_str)` - Convert date format
  - `safe_designation(key, lang)` - Get designation translation

**When to modify:** When adding new formatting or helper functions.

---

### `/generator/views` - View Controllers
**Purpose:** Handle HTTP requests and business logic for each document type

**Files:**
- `home.py` - Home page view
- `circular.py` - Circular document CRUD operations
  - `generate_circular_body()` - AI body generation
  - `result_circular()` - Preview page
  - `download_circular_pdf()` - PDF export
  - `download_circular_docx()` - DOCX export
  
- `office_order.py` - Office order operations
  - `generate_body()` - AI body generation
  - `result_office_order()` - Preview page
  - `download_pdf()` - PDF export
  - `download_docx()` - DOCX export
  
- `policy.py` - Policy document operations
  - `generate_policy_body()` - AI body generation
  - `result_policy()` - Preview page
  - `download_policy_pdf()` - PDF export
  - `download_policy_docx()` - DOCX export

**When to modify:** When changing document generation logic or adding features.

---

### `/generator/templates` - HTML Templates
**Purpose:** Frontend templates for rendering pages

**Structure:**
```
templates/generator/
  ├── base.html              # Base template with common layout
  ├── home.html              # Homepage
  ├── circular_form.html     # Circular input form
  ├── result_circular.html   # Circular preview
  ├── pdf_circular.html      # Circular PDF template
  ├── result_office_order.html
  ├── pdf_office_order.html
  ├── result_policy.html
  └── pdf_policy.html
```

**When to modify:** When changing UI/UX or page layouts.

---

### `/generator/fonts` - Custom Fonts
**Purpose:** Store custom fonts for PDF generation (especially for Hindi text)

**Files:**
- `NotoSansDevanagari-Regular.ttf`
- `NotoSansDevanagari-Bold.ttf`
- `NotoSerifDevanagari-Regular.ttf`
- `NotoSerifDevanagari-Bold.ttf`

**When to modify:** When adding support for new languages or changing fonts.

---

### `/static/generator` - Static Assets
**Purpose:** CSS, images, JavaScript files

**Files:**
- `style.css` - Main stylesheet
- `bisag_logo.png` - Organization logo
- `bisag_img1.jpg` - Banner image

**When to modify:** When updating styling or branding.

---

## 🔧 Common Development Tasks

### Adding a New Document Type

1. **Create view file:** `generator/views/new_document.py`
2. **Add configuration:** `config/new_document.json`
3. **Create data loader:** Add function to `generator/services/data_loader.py`
4. **Create templates:** 
   - `templates/generator/new_document_form.html`
   - `templates/generator/result_new_document.html`
   - `templates/generator/pdf_new_document.html`
5. **Add URL routes:** Update `generator/urls.py`
6. **Import views:** Update `generator/views/__init__.py`

### Modifying AI Generation

**Location:** `generator/views/{document_type}.py`

Find the `generate_*_body()` function and modify the `system_prompt` variable.

Example:
```python
def generate_circular_body(request):
    # ...
    if lang == "hi":
        system_prompt = """
        आप BISAG-N के लिए एक परिपत्र लिख रहे हैं।
        [Your custom instructions in Hindi]
        """
    else:
        system_prompt = """
        You are writing a circular for BISAG-N.
        [Your custom instructions in English]
        """
    # ...
```

### Changing PDF Layout

**Location:** `generator/templates/generator/pdf_{document_type}.html`

These are HTML templates that get converted to PDF. You can:
- Add inline CSS for styling
- Modify structure
- Add/remove sections
- Change fonts

Example:
```html
<style>
    body { font-family: 'Noto Sans Devanagari', sans-serif; }
    .header { text-align: center; font-weight: bold; }
</style>
```

### Adding New Designation

**Location:** `generator/data/constants.py`

Add to `DESIGNATION_MAP`:
```python
DESIGNATION_MAP = {
    # ... existing entries ...
    "New Position": {
        "hi": "नया पद",
        "en": "New Position",
    },
}
```

### Updating Configuration Data

**Location:** `config/{document_type}.json`

Example structure:
```json
{
    "people": [
        {
            "id": 1,
            "name_en": "John Doe",
            "name_hi": "जॉन डो",
            "designation": "Manager"
        }
    ],
    "templates": {
        "header": "...",
        "footer": "..."
    }
}
```

---

## 🧪 Testing Your Changes

### 1. Manual Testing
```bash
python manage.py runserver
# Visit http://localhost:8000
# Test each document type
```

### 2. Check for Python Errors
```bash
python manage.py check
```

### 3. Run Migrations (if models changed)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Test Imports
```bash
python -c "from generator.views import circular; print('OK')"
```

---

## 📖 Code Style Guide

### Python
- Use PEP 8 style guide
- Functions: `snake_case()`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Max line length: 100 characters

### HTML/Templates
- Indent with 2 spaces
- Use Django template tags: `{% %}` and `{{ }}`
- Keep logic in views, not templates

### CSS
- Use semantic class names
- Prefix custom classes with `doc-` (e.g., `doc-header`)
- Group related styles together

---

## 🐛 Debugging Tips

### Enable Debug Mode
In `.env`:
```
DEBUG=True
```

### Check Logs
```bash
# View recent log entries
tail -n 50 debug.log
```

### Python Shell
```bash
python manage.py shell
```
```python
from generator.services.data_loader import get_circular_data
data = get_circular_data()
print(data)
```

### Common Issues

**Issue:** Import Error
- Check `__init__.py` files exist
- Verify correct import path
- Restart IDE

**Issue:** JSON Not Found
- Ensure file is in `config/` directory
- Check spelling
- Verify file encoding is UTF-8

**Issue:** PDF Not Generating
- Check WeasyPrint installation
- Verify fonts are accessible
- Check template syntax

---

## 📦 Dependencies Explained

```
django                  # Web framework
google-generativeai     # AI generation
python-dotenv           # Environment variables
reportlab               # PDF generation (alternative)
python-docx             # DOCX generation
weasyprint              # HTML to PDF conversion
PyPDF2                  # PDF manipulation
pdf2image               # PDF to image conversion
Pillow                  # Image processing
```

---

## 🚀 Deployment Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Update `SECRET_KEY` to a secure random value
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Configure production database
- [ ] Set up static file serving
- [ ] Configure media file storage
- [ ] Set up proper logging
- [ ] Enable HTTPS
- [ ] Set up backup system
- [ ] Configure email settings (if needed)

---

## 📞 Getting Help

1. Check **STRUCTURE.md** for file locations
2. Check **README.md** for setup instructions
3. Check **MIGRATION.md** for recent changes
4. Review error logs in `debug.log`
5. Use Django shell for debugging

---

Last Updated: February 17, 2026

