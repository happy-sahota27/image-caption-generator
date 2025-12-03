# Deployment Guide

This application is designed to work seamlessly in both local and Hugging Face Spaces environments without any code changes.

## 🏠 Running Locally

### Prerequisites
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)

### Steps

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Access the interface**
   - The app will automatically open in your browser
   - Or visit the URL shown in the terminal (usually http://127.0.0.1:7860)
   - A public shareable link will also be created

### Configuration

The app automatically detects it's running locally and configures itself accordingly. If you want to customize settings, you can modify `config.py`:

- `GRADIO_CONFIG["share"]`: Set to `False` if you don't want a public URL
- `GRADIO_CONFIG["server_port"]`: Change the port number
- `MODEL_NAME`: Use a different model (e.g., "Salesforce/blip-image-captioning-base" for smaller model)

---

## ☁️ Deploying to Hugging Face Spaces

### Option 1: Web Interface (Easiest)

1. **Create a new Space**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `image-caption-generator`
   - License: MIT
   - SDK: Gradio
   - Click "Create Space"

2. **Upload files**
   - Click "Files" → "Add file" → "Upload files"
   - Upload these files:
     - `app.py`
     - `caption_generator.py`
     - `config.py`
     - `requirements.txt`
     - `README.md`
   - Click "Commit changes to main"

3. **Wait for build**
   - The Space will automatically build (5-10 minutes first time)
   - Once complete, your app is live!

### Option 2: Git CLI

1. **Create Space on Hugging Face website first**

2. **Clone and push**
   ```bash
   # Clone your HF Space
   git clone https://huggingface.co/spaces/YOUR_USERNAME/image-caption-generator
   cd image-caption-generator
   
   # Copy files
   cp /path/to/project/{app.py,caption_generator.py,config.py,requirements.txt,README.md} .
   
   # Commit and push
   git add .
   git commit -m "🚀 Deploy Image Caption Generator"
   git push origin main
   ```

### Option 3: From Existing Git Repository

If your code is already on GitHub:

1. Create a new Space on Hugging Face
2. In Space settings, connect your GitHub repository
3. Hugging Face will automatically sync your code

---

## 🔧 How Auto-Detection Works

The application uses environment detection in `config.py`:

```python
# Detects Hugging Face by checking for SPACE_ID environment variable
IS_HUGGINGFACE = os.getenv("SPACE_ID") is not None
```

**On Hugging Face Spaces:**
- No public share link (uses Space's own URL)
- Optimized for cloud deployment
- Automatic restarts on updates

**Running Locally:**
- Creates shareable public URL
- Binds to localhost:7860
- Shows detailed startup messages

---

## 📝 Files Explanation

| File | Purpose |
|------|---------|
| `app.py` | Main Gradio web interface |
| `caption_generator.py` | Core BLIP model logic |
| `config.py` | **Auto-detects environment** and configures settings |
| `requirements.txt` | Python dependencies |
| `README.md` | Documentation (includes HF metadata) |
| `.env.example` | Example environment configuration |
| `.gitignore` | Files to exclude from Git |

---

## 🚀 Quick Deploy Commands

**From your project directory:**

```bash
# Add config.py to git
git add config.py .env.example .gitignore

# Commit changes
git commit -m "✨ Add environment auto-detection for local and HF deployment"

# Push to GitHub (if using GitHub)
git push origin main

# Or push directly to Hugging Face Space
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/image-caption-generator
git push hf main
```

---

## ✅ Testing Both Environments

**Test Locally:**
```bash
python app.py
# Should show: "Environment: local"
# Should create a shareable link
```

**Test on Hugging Face:**
- After deployment, check Space logs
- Should show: "Environment: huggingface"
- Should use Space's own URL

---

## 🐛 Troubleshooting

### Local Issues

**Port already in use:**
```python
# Edit config.py
GRADIO_CONFIG = {
    "server_port": 7861,  # Change port
    ...
}
```

**Model download fails:**
- Check internet connection
- Ensure ~2GB free disk space

### Hugging Face Issues

**Build fails:**
- Check logs in "Logs" tab
- Verify all files uploaded correctly
- Ensure requirements.txt has correct versions

**Out of memory:**
- Use smaller model: `Salesforce/blip-image-captioning-base`
- Request upgraded hardware in Space settings

---

## 🎉 Success!

Your application now:
- ✅ Runs locally without modifications
- ✅ Deploys to Hugging Face without modifications
- ✅ Auto-detects environment
- ✅ Configures itself appropriately

No environment variables to set, no code changes needed - it just works! 🚀
