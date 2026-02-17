# 🚀 UPLOAD TO GITHUB - QUICK START

## Choose Your Method:

### 🤖 Method 1: Automated Script (Recommended)
```powershell
.\upload_to_github.ps1
```
**Easiest way!** The script will guide you through everything.

---

### ⚡ Method 2: Manual (5 Minutes)

**1. Create GitHub repository:**
   - Go to: https://github.com/new
   - Name: `ai-formal-document-generator`
   - Don't initialize with anything
   - Click "Create repository"

**2. Run these commands:**
```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .
git commit -m "Initial commit: AI Formal Document Generator"
git remote add origin https://github.com/YOUR-USERNAME/ai-formal-document-generator.git
git branch -M main
git push -u origin main
```

**3. Enter credentials:**
   - Username: Your GitHub username
   - Password: Personal Access Token (get from https://github.com/settings/tokens)

---

### 🖱️ Method 3: GitHub Desktop (No Commands)
1. Download: https://desktop.github.com/
2. Add this folder as a repository
3. Click "Publish repository"

---

## 📚 Need More Help?

**Complete Guide:** `docs/beginner/GITHUB_UPLOAD_GUIDE.md`  
**Quick Checklist:** `docs/beginner/GITHUB_CHECKLIST.md`

---

## 🔑 Important: Personal Access Token

GitHub requires a token (not your password):
1. Go to: https://github.com/settings/tokens
2. Click: "Generate new token (classic)"
3. Select scope: ☑ repo
4. Copy the token
5. Use it as your password when pushing

---

## ✅ Ready?

Choose a method above and upload your project now! 🚀

**Your repository will be at:**
`https://github.com/YOUR-USERNAME/ai-formal-document-generator`

