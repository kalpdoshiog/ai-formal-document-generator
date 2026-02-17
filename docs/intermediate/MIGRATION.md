# Migration Guide - Project Restructuring

## 🔄 What Changed?

The project has been reorganized for better maintainability and easier navigation. Here's what moved:

### 1. Configuration Files
```
BEFORE: *.json files in root directory
AFTER:  All JSON files moved to config/ directory
```

**Files Moved:**
- `circular.json` → `config/circular.json`
- `office_order.json` → `config/office_order.json`
- `policy.json` → `config/policy.json`
- `advertisement.json` → `config/advertisement.json`
- `purschase_order.json` → `config/purschase_order.json`

### 2. Constants & Data
```
BEFORE: generator/constants.py
AFTER:  generator/data/constants.py
```

### 3. Helper Functions Split
```
BEFORE: generator/views/helpers.py (all logic mixed)
AFTER:  Split into organized modules:
  - generator/services/ai_service.py (AI integration)
  - generator/services/data_loader.py (JSON loading)
  - generator/utils_new/formatters.py (formatting functions)
```

## 📝 Import Changes Required

If you have custom code, update your imports:

### AI Service
```python
# OLD
from .helpers import get_gemini_model

# NEW
from ..services.ai_service import get_gemini_model
```

### Data Loading
```python
# OLD
from .helpers import get_circular_data, get_office_order_data, get_policy_data

# NEW
from ..services.data_loader import get_circular_data, get_office_order_data, get_policy_data
```

### Formatters
```python
# OLD
from .helpers import format_date_ddmmyyyy, safe_designation

# NEW
from ..utils_new.formatters import format_date_ddmmyyyy, safe_designation
```

### Constants
```python
# OLD
from ..constants import DESIGNATION_MAP

# NEW
from ..data.constants import DESIGNATION_MAP
```

## ✅ What Still Works?

The `helpers.py` file has been kept for **backward compatibility** with re-exports. So old imports will still work, but you'll get a deprecation notice to update to the new structure.

## 🔍 How to Find Files Now?

Use the **STRUCTURE.md** file as your quick reference guide. It tells you exactly where to find everything!

## 🚨 Breaking Changes

### JSON File Paths
If you have code that directly references JSON files, update the paths:

```python
# OLD
path = os.path.join(settings.BASE_DIR, "circular.json")

# NEW
path = os.path.join(settings.BASE_DIR, "config", "circular.json")
```

**Note:** The data loader functions in `services/data_loader.py` have already been updated.

## 🧪 Testing After Migration

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Test each document type:**
   - Go to home page
   - Try generating a Circular
   - Try generating an Office Order
   - Try generating a Policy
   - Download PDF and DOCX for each

3. **Check for errors:**
   - Monitor the console output
   - Check `debug.log` file

## 📦 No Changes Needed For:

- Templates (`generator/templates/`)
- Static files (`static/`)
- Fonts (`generator/fonts/`)
- Database models (`generator/models.py`)
- URL routes (`generator/urls.py`)
- Admin configuration (`generator/admin.py`)
- Main settings (`ai_formal_generator/settings.py`)

## 💡 Benefits of New Structure

1. **Better Organization**: Files are grouped by purpose
2. **Easier to Find**: Logical folder structure
3. **Separation of Concerns**: Services, data, utils are separate
4. **Scalability**: Easy to add new document types
5. **Maintainability**: Smaller, focused files
6. **Clear Dependencies**: Import paths show relationships

## 🆘 Troubleshooting

### Import Error: "No module named 'generator.services'"
- Make sure `__init__.py` files exist in new directories
- Restart your IDE/editor
- Clear Python cache: Delete `__pycache__` folders

### JSON File Not Found
- Ensure all JSON files are in `config/` directory
- Check file names (no typos)
- Verify the data_loader.py is using correct paths

### Still Using Old Imports?
- Search your project for `from .helpers import`
- Update to new structure for better performance
- helpers.py is deprecated and may be removed in future

## 📞 Need Help?

Refer to:
- **STRUCTURE.md** - Quick file location reference
- **README.md** - Complete project documentation
- Check the updated imports in view files for examples

---

Migration completed on: February 17, 2026

