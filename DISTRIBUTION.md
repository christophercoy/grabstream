# Grabstream - YouTube Audio Downloader - Distribution Guide

### **For macOS Users (ARM64/Apple Silicon):**

1. **Download the executable** from you
2. **Make it executable** (if needed):
   ```bash
   chmod +x grabstream
   ```

3. **Use it directly**:
   ```bash
   ./grabstream "https://youtu.be/VIDEO_ID" "output_filename.mp3"
   ```

### **Examples:**
```bash
# Basic usage
./grabstream "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "my_song.mp3"

# With custom bitrate
./grabstream "https://youtu.be/dQw4w9WgXcQ" "audio_file.mp3" --bitrate 256

# Help
./grabstream --help
```

## 📋 System Requirements for Users

- **macOS** (Apple Silicon/ARM64)
- **No Python installation required**
- **No additional dependencies required**
- **Internet connection** for downloading

## 🔧 Creating Windows/Linux Executables

### **Option 1: GitHub Actions (Recommended)**
I've set up automated builds that create executables for all platforms:

1. **Push your code to GitHub**
2. **Create a release tag**: `git tag v1.0.0 && git push origin v1.0.0`
3. **GitHub will automatically build**:
   - `grabstream.exe` (Windows)
   - `grabstream` (macOS)
   - `grabstream` (Linux)

### **Option 2: Manual Windows Build**
If you have access to a Windows machine:

1. **Copy all files** to the Windows machine
2. **Run the build script**: `build-windows.bat`
3. **Or manually**:
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   pyinstaller --onefile --name grabstream.exe grabstream.py
   ```

### **Option 3: Linux Build**
On a Linux machine:
```bash
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile --name grabstream grabstream.py
```

## ⚠️ Important Notes

1. **Platform Specific**: This executable only works on macOS ARM64 (Apple Silicon)
2. **File Size**: 8.1 MB (includes all dependencies)
3. **Security**: Some systems may show security warnings for unsigned executables
4. **Updates**: You'll need to rebuild and redistribute for updates

## 🛡️ Security Considerations

- The executable is **unsigned**, so users may see security warnings
- Users can bypass with: "System Preferences > Security & Privacy > Allow anyway"
- For production distribution, consider code signing

## 🎯 Quick Distribution Checklist

- ✅ Executable created (`dist/grabstream`)
- ✅ Tested and working
- ✅ Documentation provided
- ✅ Platform requirements specified
- ✅ Usage examples included

**Your audio downloader is ready for distribution!**
