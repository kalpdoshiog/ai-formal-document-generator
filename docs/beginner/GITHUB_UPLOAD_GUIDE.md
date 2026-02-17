# 🚀 How to Upload This Project to GitHub

This guide will walk you through uploading your AI Formal Document Generator project to GitHub.

---

## 📋 Prerequisites

1. **Git installed** on your computer
   - Download from: https://git-scm.com/downloads
   - Verify: Run `git --version` in terminal

2. **GitHub account**
   - Create at: https://github.com/signup
   - Free account is sufficient

3. **Project ready** (✅ Already done!)
   - Code organized
   - Documentation complete
   - .gitignore configured

---

## 🎯 Quick Upload (Step-by-Step)

### Step 1: Create GitHub Repository

1. **Go to GitHub:**
   - Visit: https://github.com
   - Log in to your account

2. **Create New Repository:**
   - Click the `+` icon (top right) → `New repository`
   
3. **Repository Settings:**
   ```
   Repository name:     ai-formal-document-generator
   Description:         Django app for generating formal documents using Google Gemini AI
   Visibility:          ☑ Public (or Private if preferred)
   
   DO NOT initialize with:
   ☐ README.md (you already have one)
   ☐ .gitignore (you already have one)
   ☐ License (add later if needed)
   ```

4. **Click:** `Create repository`

---

### Step 2: Prepare Your Local Project

Open **PowerShell** or **Command Prompt** in your project folder:

```powershell
# Navigate to your project
cd D:\DocumentGenerator-main\FormalDocument\ai_formal_generator
```

---

### Step 3: Initialize Git (First Time Only)

```powershell
# Initialize git repository
git init

# Configure your identity (first time only)
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

---

### Step 4: Add All Files

```powershell
# Add all files to staging
git add .

# Check what will be committed
git status
```

**Expected output:** List of files to be committed (should NOT include .env, __pycache__, db.sqlite3, etc.)

---

### Step 5: Create First Commit

```powershell
# Create your first commit
git commit -m "Initial commit: AI Formal Document Generator with organized structure"
```

---

### Step 6: Connect to GitHub

Replace `YOUR-USERNAME` with your GitHub username:

```powershell
# Add remote repository
git remote add origin https://github.com/YOUR-USERNAME/ai-formal-document-generator.git

# Verify remote was added
git remote -v
```

---

### Step 7: Push to GitHub

```powershell
# Push to GitHub (main branch)
git branch -M main
git push -u origin main
```

**Enter credentials when prompted:**
- Username: Your GitHub username
- Password: Use **Personal Access Token** (see below)

---

### Step 8: Verify Upload

1. **Go to your GitHub repository:**
   - `https://github.com/YOUR-USERNAME/ai-formal-document-generator`

2. **You should see:**
   - All your files
   - README.md displayed on homepage
   - Folder structure intact

---

## 🔑 GitHub Personal Access Token (Required)

GitHub no longer accepts passwords for git operations. You need a Personal Access Token:

### Creating a Token:

1. **Go to:** https://github.com/settings/tokens
2. **Click:** `Generate new token` → `Generate new token (classic)`
3. **Settings:**
   ```
   Note: Git operations for ai-formal-document-generator
   Expiration: 90 days (or custom)
   
   Select scopes:
   ☑ repo (full control of private repositories)
   ```
4. **Click:** `Generate token`
5. **Copy token immediately** (you won't see it again!)
6. **Use this token** as your password when pushing to GitHub

### Saving Credentials (Optional):

```powershell
# Save credentials so you don't have to enter token every time
git config --global credential.helper wincred
```

---

## 📝 Complete Upload Commands (Copy-Paste)

**After creating GitHub repository, run these commands:**

```powershell
# Navigate to project
cd D:\DocumentGenerator-main\FormalDocument\ai_formal_generator

# Initialize git
git init

# Configure (replace with your info)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Formal Document Generator with organized structure and documentation"

# Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/ai-formal-document-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 🔒 Security Checklist (Before Uploading)

✅ **Already Protected:**
- ✅ `.env` file is in .gitignore (won't be uploaded)
- ✅ `db.sqlite3` is in .gitignore (won't be uploaded)
- ✅ `__pycache__/` is in .gitignore (won't be uploaded)
- ✅ `.venv/` is in .gitignore (won't be uploaded)
- ✅ `.env.example` is safe to upload (no secrets)

**IMPORTANT:** Make sure your `.env` file (if it exists) is NOT uploaded!

```powershell
# Verify .env is ignored
git status

# Should NOT show .env in the list
```

---

## 📦 What Will Be Uploaded

Your GitHub repository will include:

```
✅ Source code (all .py files)
✅ Configuration files (config/*.json)
✅ Templates (generator/templates/)
✅ Static files (static/)
✅ Documentation (docs/)
✅ Requirements (requirements.txt)
✅ Environment example (.env.example)
✅ README.md
✅ .gitignore

❌ NOT uploaded (ignored):
❌ .env (your secrets)
❌ db.sqlite3 (database)
❌ __pycache__/ (Python cache)
❌ .venv/ (virtual environment)
❌ *.log (log files)
```

---

## 🎨 Make Your Repository Look Professional

### 1. Add Topics (Tags)

On GitHub repository page:
- Click `⚙️ Settings` (gear icon near About)
- Add topics: `django`, `python`, `ai`, `gemini`, `document-generator`, `pdf`, `docx`

### 2. Update Repository Description

Add description:
```
Django application for generating formal documents (Circulars, Office Orders, Policies) 
using Google Gemini AI with English and Hindi support. Export to PDF and DOCX.
```

### 3. Add Website URL (Optional)

If you deploy it later, add the URL in repository settings.

---

## 🔄 Future Updates (After Initial Upload)

When you make changes to your project:

```powershell
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add feature: X" 

# Push to GitHub
git push
```

### Commit Message Best Practices:

```powershell
# Good commit messages:
git commit -m "Add: New document type for memos"
git commit -m "Fix: PDF generation for Hindi text"
git commit -m "Update: Documentation for deployment"
git commit -m "Refactor: Simplify data loader service"

# Bad commit messages:
git commit -m "update"
git commit -m "fixes"
git commit -m "changes"
```

---

## 📄 Adding a License (Recommended)

1. **On GitHub repository:**
   - Click `Add file` → `Create new file`
   - Name: `LICENSE`
   - Click `Choose a license template`
   - Select: `MIT License` (most common for open source)
   - Fill in year and name
   - Commit

2. **Or add locally:**
   - Create LICENSE file
   - Add license text
   - Commit and push

---

## 🌟 README Badges (Optional)

Add these to your README.md for a professional look:

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-5.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
```

---

## 🐛 Troubleshooting

### Issue: "Permission denied"
**Solution:** Use Personal Access Token instead of password

### Issue: "Repository not found"
**Solution:** Check repository URL is correct
```powershell
git remote -v
# If wrong:
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/ai-formal-document-generator.git
```

### Issue: ".env file uploaded by mistake"
**Solution:** Remove from history
```powershell
git rm --cached .env
git commit -m "Remove .env from tracking"
git push
```

### Issue: "Large files rejected"
**Solution:** Check file sizes. GitHub limit is 100MB per file
```powershell
# Find large files
Get-ChildItem -Recurse | Where-Object {$_.Length -gt 50MB} | Select-Object FullName, Length
```

---

## ✅ Verification Checklist

After uploading, verify:

- [ ] Repository is created on GitHub
- [ ] All files are visible
- [ ] README.md displays correctly
- [ ] Documentation folder structure is intact
- [ ] .env file is NOT visible
- [ ] Repository has proper name and description
- [ ] You can clone it to verify:
  ```powershell
  git clone https://github.com/YOUR-USERNAME/ai-formal-document-generator.git test-clone
  cd test-clone
  # Check if everything is there
  ```

---

## 📚 Additional Resources

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Markdown Guide:** https://guides.github.com/features/mastering-markdown

---

## 🎯 Quick Reference Commands

```powershell
# Check status
git status

# Add specific file
git add filename.py

# Add all changes
git add .

# Commit
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# See differences
git diff
```

---

## 🎊 Success!

Once uploaded, your repository will be at:
```
https://github.com/YOUR-USERNAME/ai-formal-document-generator
```

Share this URL with others, add it to your portfolio, or continue developing!

---

**Last Updated:** February 17, 2026  
**Guide Version:** 1.0

