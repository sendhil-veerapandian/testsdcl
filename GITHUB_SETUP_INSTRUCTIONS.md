# GitHub Setup Instructions for SDLC Project

## Prerequisites
1. **Check if Git is installed:**
   ```bash
   git --version
   ```
   
   If not installed, download from: https://git-scm.com/download/win

2. **Ensure you have a GitHub account** and are logged in

## Step-by-Step Setup

### Step 1: Initialize Git Repository
```bash
# Navigate to your project folder (if not already there)
cd "C:\Users\Sandeep Yewale\Code\SDLC"

# Initialize Git repository
git init
```

### Step 2: Add Your Files
```bash
# Add all files to Git
git add .

# Check what files are staged
git status
```

### Step 3: Configure Git Identity (First Time Only)
```bash
# Set your Git username and email (replace with your actual details)
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"

# Verify your configuration
git config --list
```

### Step 4: Make First Commit
```bash
# Commit your files
git commit -m "Initial commit: SDLC AI Assistance project"
```

### Step 5: Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in top right corner
3. Select "New repository"
4. Repository name: `SDLC`
5. Description: `SDLC AI Assistance Project`
6. Choose Public or Private
7. **DO NOT** check "Add a README file" (you already have one)
8. **DO NOT** check "Add .gitignore" (you already have one)
9. **DO NOT** check "Choose a license" (you already have one)
10. Click "Create repository"

### Step 6: Connect Local to GitHub
```bash
# Add remote origin (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/S3K-Tech/SDLC.git

# Verify remote was added
git remote -v
```

### Step 7: Push to GitHub
```bash
# Set main as default branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 8: Verify
1. Go to your GitHub repository: `https://github.com/S3K-Tech/SDLC`
2. Confirm all files are visible
3. Check that `venv/` folder is NOT visible (correctly ignored)

## For Future Updates

When you make changes to your code:

```bash
# Add changes
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push origin main
```

## Troubleshooting

### If you get "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/S3K-Tech/SDLC.git
```

### If you get "Author identity unknown" error
```bash
# Set your Git identity (replace with your actual details)
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"

# Verify configuration
git config --list
```

### If you get authentication errors
1. Use GitHub Personal Access Token instead of password
2. Or use GitHub CLI: `gh auth login`

### If you need to check Git status
```bash
git status
git remote -v
git branch -a
```

## Important Notes

- Your `venv/` folder will NOT be uploaded (correctly ignored)
- Large files like `workflow_graph.png` will be uploaded
- Make sure no sensitive data (API keys, passwords) are in your code
- The `.gitignore` file will prevent unnecessary files from being uploaded

## Next Steps After Setup

1. **Clone on other machines:**
   ```bash
   git clone https://github.com/S3K-Tech/SDLC.git
   ```

2. **Create new branches for features:**
   ```bash
   git checkout -b feature-name
   git push -u origin feature-name
   ```

3. **Pull latest changes:**
   ```bash
   git pull origin main
   ```

## For New Users: How to Clone and Set Up the Project

### Prerequisites for New Users
1. **Install Git:**
   - Windows: Download from [https://git-scm.com/download/win](https://git-scm.com/download/win)
   - macOS: `brew install git` (if you have Homebrew) or download from Git website
   - Linux: `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/RHEL)

2. **Install Python 3.8+** (if not already installed)
   - Windows: Download from [https://python.org/downloads](https://python.org/downloads)
   - macOS: `brew install python` or download from Python website
   - Linux: `sudo apt-get install python3` (Ubuntu/Debian)

### Step-by-Step Cloning Instructions

#### Step 1: Clone the Repository
```bash
# Navigate to where you want to store the project
cd "C:\Users\YourUsername\Code"  # Windows
# OR
cd ~/Code  # macOS/Linux

# Clone the repository
git clone https://github.com/S3K-Tech/SDLC.git

# Navigate into the project folder
cd SDLC
```

#### Step 2: Set Up Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Verify activation (you should see (venv) in your prompt)
```

#### Step 3: Install Dependencies
```bash
# Make sure you're in the project root and virtual environment is activated
pip install -r requirements.txt

# Verify installation
pip list
```

#### Step 4: Configure Git Identity (First Time Only)
```bash
# Set your Git username and email
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"

# Verify configuration
git config --list
```

#### Step 5: Verify Setup
```bash
# Check Git status
git status

# Check if you can see all files
dir  # Windows
# OR
ls -la  # macOS/Linux

# Check Python and packages
python --version
pip list
```

### Troubleshooting for New Users

#### If Git clone fails:
```bash
# Check if you have access to the repository
# Make sure you're logged into GitHub in your browser
# Try cloning with HTTPS instead of SSH
git clone https://github.com/S3K-Tech/SDLC.git
```

#### If virtual environment creation fails:
```bash
# Make sure Python is installed and in PATH
python --version

# Try using python3 instead
python3 -m venv venv
```

#### If pip install fails:
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try installing with --user flag
pip install --user -r requirements.txt
```

#### If you get permission errors:
```bash
# Windows: Run PowerShell as Administrator
# macOS/Linux: Use sudo (be careful)
sudo pip install -r requirements.txt
```

### Project Structure After Cloning
```
SDLC/
├── src/                    # Source code
├── venv/                   # Virtual environment (created locally)
├── app_api.py             # API application
├── app_streamlit.py       # Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore            # Git ignore rules
└── ... (other project files)
```

### Running the Project
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# Run Streamlit app
streamlit run app_streamlit.py

# Run API (if applicable)
python app_api.py
```

## Quick Commands Reference

| Command | Description |
|---------|-------------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git push origin main` | Push to GitHub |
| `git pull origin main` | Pull latest changes |
| `git remote -v` | Check remote connections |
| `git branch -a` | List all branches |
| `git log --oneline` | View commit history |

## File Structure That Will Be Uploaded

✅ **Will be uploaded:**
- `src/` - Your source code
- `app_api.py` - API application
- `app_streamlit.py` - Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `CODEBASE_OVERVIEW.md` - Codebase overview
- `IMPROVEMENT_ROADMAP.md` - Project roadmap
- `LICENSE` - Project license
- `dockerfile` - Docker configuration
- `workflow_graph.png` - Workflow diagram

❌ **Will NOT be uploaded (ignored):**
- `venv/` - Virtual environment
- `logs/` - Log files
- `__pycache__/` - Python cache files
- `.env` - Environment variables
- IDE configuration files

## Security Checklist

Before pushing to GitHub, ensure:
- [ ] No API keys or secrets in your code
- [ ] No database credentials exposed
- [ ] No personal information in comments
- [ ] No sensitive configuration files
- [ ] Virtual environment is properly ignored

## Need Help?

If you encounter any issues:
1. Check the troubleshooting section above
2. Use `git status` to understand current state
3. Check GitHub's documentation: https://docs.github.com/
4. Common Git commands: https://git-scm.com/docs
