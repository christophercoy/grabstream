# Grabstream - YouTube Audio Downloader

A simple command-line tool to extract high-quality audio from YouTube videos and save them as MP3 files.

## Features

- 🎵 Download audio from YouTube videos
- 🎧 High-quality MP3 output (up to 320kbps)
- 📁 Custom output filename support
- ✅ Input validation and error handling
- 🔄 Progress indicators during download
- 🛡️ Safe filename sanitization
- 📊 File size and duration information

## Prerequisites

### System Requirements
- Python 3.6 or higher
- ffmpeg (for audio conversion)

### Installing ffmpeg

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
1. Download ffmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract and add to your system PATH

## Installation

1. **Clone or download the script:**
   ```bash
   git clone <repository-url>
   cd grabstream
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable (optional):**
   ```bash
   chmod +x youtube_audio_downloader.py
   ```

## Usage

### Basic Usage
```bash
python youtube_audio_downloader.py "YOUTUBE_URL" "OUTPUT_FILENAME"
```

### Examples

**Download with automatic .mp3 extension:**
```bash
python youtube_audio_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "my_song"
```

**Specify complete filename:**
```bash
python youtube_audio_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "my_song.mp3"
```

**Use different bitrate:**
```bash
python youtube_audio_downloader.py "https://youtu.be/dQw4w9WgXcQ" "audio_file" --bitrate 256
```

**Short URL format:**
```bash
python youtube_audio_downloader.py "https://youtu.be/dQw4w9WgXcQ" "output"
```

### Command-Line Options

- `url` - YouTube video URL (required)
- `output` - Output filename (required, .mp3 extension added automatically if missing)
- `--bitrate`, `-b` - Audio bitrate: 128, 192, 256, or 320 kbps (default: 320)
- `--version`, `-v` - Show version information
- `--help`, `-h` - Show help message

### Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`

## Output

The tool provides detailed feedback during operation:

```
🎵 Downloading audio from: https://www.youtube.com/watch?v=dQw4w9WgXcQ
📁 Output file: my_song.mp3
🎧 Bitrate: 320kbps
--------------------------------------------------
📺 Title: Rick Astley - Never Gonna Give You Up
⏱️  Duration: 03:32
--------------------------------------------------
[download] 100% of 3.45MiB in 00:02
[ffmpeg] Converting audio...
✅ Success! Audio saved as: my_song.mp3
📊 File size: 8.23 MB

🎉 Download completed successfully!
```

## Error Handling

The tool includes comprehensive error handling for:

- Invalid YouTube URLs
- Network connection issues
- Missing ffmpeg installation
- File permission problems
- Existing file conflicts (with overwrite prompt)

## Technical Details

- **Audio Quality:** Downloads the best available audio quality from YouTube
- **Conversion:** Uses ffmpeg for high-quality MP3 conversion
- **Sample Rate:** 44.1 kHz (CD quality)
- **Bitrate Options:** 128, 192, 256, or 320 kbps
- **File Safety:** Automatically sanitizes filenames to prevent filesystem issues

## Dependencies

- `yt-dlp` - Modern YouTube downloader (actively maintained fork of youtube-dl)
- `ffmpeg` - Audio/video processing (system dependency)

## Troubleshooting

### "ffmpeg not found" error
Make sure ffmpeg is installed and available in your system PATH. Test with:
```bash
ffmpeg -version
```

### Download fails with network error
- Check your internet connection
- Verify the YouTube URL is correct and the video is publicly accessible
- Some videos may be geo-restricted or have download limitations

### Permission denied error
- Ensure you have write permissions in the output directory
- Try running with appropriate permissions or choose a different output location

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.
