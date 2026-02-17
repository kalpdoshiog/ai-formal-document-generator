# Quick File Location Reference

## 🎯 Common Tasks

### I want to change...

#### ✅ Document Configuration (People, Templates, etc.)
```
📂 config/
   ├── circular.json
   ├── office_order.json
   ├── policy.json
   ├── advertisement.json
   └── purschase_order.json
```

#### ✅ AI Generation Prompts & Logic
```
📂 generator/views/
   ├── circular.py       → generate_circular_body()
   ├── office_order.py   → generate_body()
   └── policy.py         → generate_policy_body()
```

#### ✅ PDF Templates & Styling
```
📂 generator/templates/generator/
   ├── pdf_circular.html
   ├── pdf_office_order.html
   └── pdf_policy.html
```

#### ✅ Designation Names (English & Hindi)
```
📂 generator/data/
   └── constants.py      → DESIGNATION_MAP
```

#### ✅ AI Service Configuration
```
📂 generator/services/
   └── ai_service.py     → get_gemini_model()
```

#### ✅ Data Loading Logic
```
📂 generator/services/
   └── data_loader.py    → get_circular_data(), get_office_order_data(), etc.
```

#### ✅ Date & Text Formatting
```
📂 generator/utils_new/
   └── formatters.py     → format_date_ddmmyyyy(), safe_designation()
```

#### ✅ Website Styling
```
📂 static/generator/
   └── style.css
```

#### ✅ Logo & Images
```
📂 static/generator/
   ├── bisag_logo.png
   └── bisag_img1.jpg
```

#### ✅ Fonts (Hindi/Devanagari)
```
📂 generator/fonts/
   ├── NotoSansDevanagari-Regular.ttf
   ├── NotoSansDevanagari-Bold.ttf
   ├── NotoSerifDevanagari-Regular.ttf
   └── NotoSerifDevanagari-Bold.ttf
```

#### ✅ URL Routes
```
📂 generator/
   └── urls.py           → App-level routes

📂 ai_formal_generator/
   └── urls.py           → Project-level routes
```

#### ✅ Database Models
```
📂 generator/
   └── models.py         → DocumentLog model
```

#### ✅ Django Settings
```
📂 ai_formal_generator/
   └── settings.py       → All Django configuration
```

---

## 📋 New Code Structure (After Reorganization)

### Before (Old) ❌
- JSON files scattered in root
- All logic in `views/helpers.py`
- Constants mixed with views

### After (New) ✅
```
config/                    ← All JSON configuration files
generator/
  ├── data/               ← Data models & constants
  │   └── constants.py
  ├── services/           ← External services (AI, data loading)
  │   ├── ai_service.py
  │   └── data_loader.py
  ├── utils_new/          ← Utility functions
  │   └── formatters.py
  ├── views/              ← View controllers (clean, focused)
  │   ├── circular.py
  │   ├── office_order.py
  │   ├── policy.py
  │   └── home.py
  ├── templates/          ← HTML templates
  ├── fonts/              ← Font files
  └── migrations/         ← Database migrations
```

---

## 🔄 Import Examples

### Old Way ❌
```python
from .helpers import get_gemini_model, get_circular_data
from ..constants import DESIGNATION_MAP
```

### New Way ✅
```python
from ..services.ai_service import get_gemini_model
from ..services.data_loader import get_circular_data
from ..data.constants import DESIGNATION_MAP
from ..utils_new.formatters import format_date_ddmmyyyy
```

---

## 📝 Quick Commands

```bash
# Start development server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Create new migration
python manage.py makemigrations
```

---

## 🎨 File Naming Conventions

- **Python files**: `snake_case.py`
- **Templates**: `snake_case.html`
- **CSS files**: `style.css`
- **Config files**: `snake_case.json`
- **Classes**: `PascalCase`
- **Functions**: `snake_case()`
- **Constants**: `UPPER_CASE`

---

## 💡 Tips

1. **Always update imports** when moving files
2. **JSON files are in `config/`** directory now
3. **Use services layer** for external integrations
4. **Keep views clean** - move logic to services/utils
5. **Follow the separation of concerns** principle

---

Last Updated: February 17, 2026

