# GitHub Upload Quick Start Script
# Run this script to prepare and upload your project to GitHub

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  GitHub Upload - Quick Start" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check if Git is installed
Write-Host "Step 1: Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git is NOT installed!" -ForegroundColor Red
    Write-Host "  Please install Git from: https://git-scm.com/downloads" -ForegroundColor Yellow
    exit
}

Write-Host ""

# Step 2: Check for sensitive files
Write-Host "Step 2: Checking for sensitive files..." -ForegroundColor Yellow

$hasSensitiveFiles = $false

if (Test-Path ".env") {
    Write-Host "⚠️  .env file found! Make sure it's in .gitignore" -ForegroundColor Red
    $hasSensitiveFiles = $true
}

if (Test-Path "db.sqlite3") {
    Write-Host "✓ db.sqlite3 found (will be ignored)" -ForegroundColor Green
}

if (-not $hasSensitiveFiles) {
    Write-Host "✓ No sensitive files to worry about" -ForegroundColor Green
}

Write-Host ""

# Step 3: Check .gitignore
Write-Host "Step 3: Verifying .gitignore..." -ForegroundColor Yellow
if (Test-Path ".gitignore") {
    Write-Host "✓ .gitignore exists" -ForegroundColor Green
} else {
    Write-Host "✗ .gitignore missing!" -ForegroundColor Red
}

Write-Host ""

# Step 4: Prompt for GitHub username
Write-Host "Step 4: GitHub Configuration" -ForegroundColor Yellow
$username = Read-Host "Enter your GitHub username"
$repoName = Read-Host "Enter repository name (default: ai-formal-document-generator)"

if ([string]::IsNullOrWhiteSpace($repoName)) {
    $repoName = "ai-formal-document-generator"
}

Write-Host ""

# Step 5: Check if git is initialized
Write-Host "Step 5: Checking Git initialization..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "✓ Git already initialized" -ForegroundColor Green
    $initGit = $false
} else {
    Write-Host "! Git not initialized yet" -ForegroundColor Yellow
    $initGit = $true
}

Write-Host ""

# Step 6: Show next steps
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Next Steps to Upload to GitHub" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. Create GitHub Repository:" -ForegroundColor Yellow
Write-Host "   • Go to: https://github.com/new" -ForegroundColor White
Write-Host "   • Repository name: $repoName" -ForegroundColor White
Write-Host "   • Make it Public or Private" -ForegroundColor White
Write-Host "   • DO NOT initialize with README, .gitignore, or license" -ForegroundColor White
Write-Host "   • Click 'Create repository'" -ForegroundColor White
Write-Host ""

Write-Host "2. Run these commands in order:" -ForegroundColor Yellow
Write-Host ""

if ($initGit) {
    Write-Host "   git init" -ForegroundColor Cyan
}

Write-Host "   git config user.name `"Your Name`"" -ForegroundColor Cyan
Write-Host "   git config user.email `"your.email@example.com`"" -ForegroundColor Cyan
Write-Host "   git add ." -ForegroundColor Cyan
Write-Host "   git commit -m `"Initial commit: AI Formal Document Generator`"" -ForegroundColor Cyan
Write-Host "   git remote add origin https://github.com/$username/$repoName.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""

Write-Host "3. When prompted for password:" -ForegroundColor Yellow
Write-Host "   • Use a Personal Access Token (NOT your GitHub password)" -ForegroundColor White
Write-Host "   • Create token at: https://github.com/settings/tokens" -ForegroundColor White
Write-Host "   • Select scope: 'repo' (full control)" -ForegroundColor White
Write-Host ""

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Complete Guide Available:" -ForegroundColor Cyan
Write-Host "  docs/beginner/GITHUB_UPLOAD_GUIDE.md" -ForegroundColor White
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Ask if user wants to execute commands
$execute = Read-Host "Do you want to execute the Git commands now? (y/N)"

if ($execute -eq 'y' -or $execute -eq 'Y') {
    Write-Host ""
    Write-Host "Executing Git commands..." -ForegroundColor Green
    Write-Host ""

    if ($initGit) {
        Write-Host "Initializing Git repository..." -ForegroundColor Yellow
        git init
    }

    Write-Host ""
    Write-Host "Please enter your Git configuration:" -ForegroundColor Yellow
    $gitName = Read-Host "Your name"
    $gitEmail = Read-Host "Your email"

    git config user.name "$gitName"
    git config user.email "$gitEmail"

    Write-Host ""
    Write-Host "Adding files..." -ForegroundColor Yellow
    git add .

    Write-Host ""
    Write-Host "Creating commit..." -ForegroundColor Yellow
    git commit -m "Initial commit: AI Formal Document Generator with organized structure"

    Write-Host ""
    Write-Host "Adding remote repository..." -ForegroundColor Yellow
    git remote add origin "https://github.com/$username/$repoName.git"

    Write-Host ""
    Write-Host "Setting main branch..." -ForegroundColor Yellow
    git branch -M main

    Write-Host ""
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host "  Ready to Push!" -ForegroundColor Cyan
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Now run this command to push to GitHub:" -ForegroundColor Yellow
    Write-Host "   git push -u origin main" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "When prompted, use your Personal Access Token as password" -ForegroundColor Yellow
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Okay! Run the commands manually when ready." -ForegroundColor Green
    Write-Host "See: docs/beginner/GITHUB_UPLOAD_GUIDE.md for detailed instructions" -ForegroundColor White
    Write-Host ""
}

Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

