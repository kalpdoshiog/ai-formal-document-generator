# 📂 Quick File Navigation Guide

## 🎯 "I Want To..." Guide

Copy this and keep it handy!

---

### 🔧 Modify AI Generation

**Task:** Change AI prompts or AI model

**Files to Edit:**
```
1. generator/services/ai_service.py
   └─ Change AI model or API configuration

2. generator/views/circular.py
   └─ Function: generate_circular_body()
   └─ Modify: system_prompt variable

3. generator/views/office_order.py
   └─ Function: generate_body()
   └─ Modify: system_prompt variable

4. generator/views/policy.py
   └─ Function: generate_policy_body()
   └─ Modify: system_prompt variable
```

---

### 📝 Add/Edit People or Organizations

**Task:** Update the list of people for circulars

**Files to Edit:**
```
config/circular.json
{
  "people": [
    {
      "id": 1,
      "name_en": "Person Name",
      "name_hi": "व्यक्ति का नाम",
      "designation": "Manager"
    }
  ]
}
```

---

### 🏢 Add New Designation

**Task:** Add a new job title with translation

**Files to Edit:**
```
generator/data/constants.py

DESIGNATION_MAP = {
    "Your New Title": {
        "hi": "हिंदी अनुवाद",
        "en": "Your New Title"
    }
}
```

---

### 🎨 Change PDF Design

**Task:** Modify how PDFs look

**Files to Edit:**
```
1. generator/templates/generator/pdf_circular.html
2. generator/templates/generator/pdf_office_order.html
3. generator/templates/generator/pdf_policy.html

Tips:
- Use inline CSS: <style>...</style>
- Change fonts, colors, layouts
- Add/remove sections
```

---

### 💅 Change Website Styling

**Task:** Update colors, fonts, layout of web pages

**Files to Edit:**
```
1. static/generator/style.css
   └─ All website styling

2. generator/templates/generator/base.html
   └─ Common layout/header/footer

3. generator/templates/generator/home.html
   └─ Homepage specific
```

---

### 🖼️ Change Logo or Images

**Task:** Update branding images

**Files to Edit:**
```
static/generator/
├── bisag_logo.png     ← Replace this
└── bisag_img1.jpg     ← Replace this

After replacing, restart server:
python manage.py runserver
```

---

### 🌍 Add Translation

**Task:** Add new language support

**Files to Edit:**
```
1. generator/data/constants.py
   └─ Add new language key to DESIGNATION_MAP
   
2. config/*.json
   └─ Add name_XX fields (e.g., name_fr for French)
   
3. generator/views/*.py
   └─ Add new language handling in generate_*_body()
   
4. generator/templates/generator/*.html
   └─ Add language option in forms
```

---

### 📄 Add New Document Type

**Task:** Create a new document type (e.g., "Memo")

**Steps:**
```
1. Create: config/memo.json
   └─ Document configuration

2. Create: generator/views/memo.py
   └─ View logic

3. Update: generator/services/data_loader.py
   └─ Add get_memo_data() function

4. Create: generator/templates/generator/
   ├── memo_form.html
   ├── result_memo.html
   └── pdf_memo.html

5. Update: generator/urls.py
   └─ Add URL routes

6. Update: generator/views/__init__.py
   └─ Export new views
```

---

### ⚙️ Environment Configuration

**Task:** Set API keys, debug mode, etc.

**Files to Edit:**
```
.env (create from .env.example)

SECRET_KEY=your-secret-key
DEBUG=True
GEMINI_API_KEY=your-api-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

### 🗄️ Database Changes

**Task:** Modify database structure

**Files to Edit:**
```
1. generator/models.py
   └─ Add/modify model classes

2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
```

---

### 🔗 URL Routes

**Task:** Add new pages or change URLs

**Files to Edit:**
```
1. generator/urls.py
   └─ Application-level URLs

2. ai_formal_generator/urls.py
   └─ Project-level URLs
```

---

### 📊 Admin Panel

**Task:** Customize Django admin

**Files to Edit:**
```
generator/admin.py

from django.contrib import admin
from .models import DocumentLog

@admin.register(DocumentLog)
class DocumentLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'document_type', 'created_at']
```

---

### 🔍 Date/Text Formatting

**Task:** Change date formats or text processing

**Files to Edit:**
```
generator/utils_new/formatters.py

def format_date_ddmmyyyy(date_str):
    # Your custom formatting
    pass
```

---

### 📦 Add Python Package

**Task:** Install new Python library

**Steps:**
```
1. Activate virtual environment:
   .venv\Scripts\activate

2. Install package:
   pip install package-name

3. Update requirements:
   pip freeze > requirements.txt
```

---

### 🎭 Change Fonts

**Task:** Add new fonts for PDFs

**Steps:**
```
1. Add .ttf file to: generator/fonts/

2. Reference in template:
   <style>
   @font-face {
       font-family: 'MyFont';
       src: url('path/to/font.ttf');
   }
   </style>
```

---

## 🚨 Common Locations Cheat Sheet

```
📋 Config Data          → config/*.json
🤖 AI Code             → generator/services/ai_service.py
📊 Load Data           → generator/services/data_loader.py
📅 Format Utils        → generator/utils_new/formatters.py
🏷️ Constants          → generator/data/constants.py
🎯 Business Logic     → generator/views/*.py
🎨 HTML Templates     → generator/templates/generator/
💅 CSS Styles         → static/generator/style.css
🖼️ Images/Logos       → static/generator/
✍️ Fonts              → generator/fonts/
⚙️ Settings           → ai_formal_generator/settings.py
🗄️ Database Models    → generator/models.py
🔗 URL Routes         → generator/urls.py
```

---

## 🔥 Hot Tips

### Tip 1: Always Use Virtual Environment
```bash
.venv\Scripts\activate
```

### Tip 2: Check Django After Changes
```bash
python manage.py check
```

### Tip 3: Clear Cache If Needed
```bash
# Delete __pycache__ folders
# Restart server
```

### Tip 4: Use Django Shell for Testing
```bash
python manage.py shell
>>> from generator.services.data_loader import get_circular_data
>>> data = get_circular_data()
>>> print(data)
```

### Tip 5: Check Logs for Errors
```bash
# View last 20 lines
Get-Content debug.log -Tail 20
```

---

## 📚 Documentation Files

| File | Purpose | When to Read |
|------|---------|-------------|
| **STRUCTURE.md** | Find files fast | Daily |
| **README.md** | Setup & overview | First time |
| **DEVELOPER_GUIDE.md** | How to develop | When coding |
| **ARCHITECTURE.md** | System design | Deep dive |
| **MIGRATION.md** | What changed | After update |
| **QUICK_NAVIGATION.md** | This file! | Always |

---

## 🎯 Keep This File Open

**Pro Tip:** Keep this file open in a second monitor or tab while coding. It's your quick reference guide!

---

*Last Updated: February 17, 2026*

