#!/usr/bin/env python3
"""
Grabstream - YouTube Audio Downloader
A command-line tool to extract high-quality audio from YouTube videos and save as MP3.
"""

import argparse
import sys
import os
import yt_dlp
from pathlib import Path


def validate_youtube_url(url):
    """Basic validation for YouTube URLs"""
    youtube_domains = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
    return any(domain in url.lower() for domain in youtube_domains)


def sanitize_filename(filename):
    """Ensure the filename is safe for the filesystem"""
    if not filename.endswith('.mp3'):
        filename += '.mp3'
    
    # Remove or replace problematic characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    return filename


def download_audio(youtube_url, output_filename, bitrate='320'):
    """
    Download audio from YouTube video and convert to MP3
    
    Args:
        youtube_url (str): The YouTube video URL
        output_filename (str): Desired output filename
        bitrate (str): Audio bitrate (default: 320kbps)
    """
    
    # Sanitize the output filename
    output_filename = sanitize_filename(output_filename)
    output_path = Path(output_filename).resolve()
    
    # Configure yt-dlp options with enhanced settings to bypass restrictions
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_path.with_suffix('')),  # Remove extension, yt-dlp will add it
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        }],
        'postprocessor_args': [
            '-ar', '44100',  # Sample rate
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,
        # Enhanced options to bypass YouTube restrictions
        'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.youtube.com/',
        'headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        },
        'extractor_args': {
            'youtube': {
                'skip': ['hls', 'dash'],  # Skip problematic formats
                'player_client': ['android', 'web'],  # Try multiple clients
            }
        },
        'sleep_interval': 1,  # Add delay between requests
        'max_sleep_interval': 5,
        'ignoreerrors': False,
        'no_warnings': False,
        'extract_flat': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🎵 Downloading audio from: {youtube_url}")
            print(f"📁 Output file: {output_filename}")
            print(f"🎧 Bitrate: {bitrate}kbps")
            print("-" * 50)
            
            # Extract video info first
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            
            print(f"📺 Title: {title}")
            if duration:
                minutes, seconds = divmod(duration, 60)
                print(f"⏱️  Duration: {minutes:02d}:{seconds:02d}")
            print("-" * 50)
            
            # Download and convert
            ydl.download([youtube_url])
            
            # Check if file was created successfully
            if output_path.exists():
                file_size = output_path.stat().st_size / (1024 * 1024)  # Size in MB
                print(f"✅ Success! Audio saved as: {output_filename}")
                print(f"📊 File size: {file_size:.2f} MB")
            else:
                print("❌ Error: Output file was not created")
                return False
                
    except yt_dlp.DownloadError as e:
        print(f"❌ Download error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False
    
    return True


def main():
    """Main function to handle command-line arguments and execute download"""
    
    parser = argparse.ArgumentParser(
        description='Download high-quality audio from YouTube videos as MP3',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "my_song.mp3"
  %(prog)s "https://youtu.be/dQw4w9WgXcQ" "audio_file" --bitrate 256
        """
    )
    
    parser.add_argument(
        'url',
        help='YouTube video URL'
    )
    
    parser.add_argument(
        'output',
        help='Output filename (will add .mp3 extension if not present)'
    )
    
    parser.add_argument(
        '--bitrate', '-b',
        default='320',
        choices=['128', '192', '256', '320'],
        help='Audio bitrate in kbps (default: 320)'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='YouTube Audio Downloader 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Validate YouTube URL
    if not validate_youtube_url(args.url):
        print("❌ Error: Please provide a valid YouTube URL")
        print("   Supported formats:")
        print("   - https://www.youtube.com/watch?v=VIDEO_ID")
        print("   - https://youtu.be/VIDEO_ID")
        sys.exit(1)
    
    # Check if output file already exists
    output_filename = sanitize_filename(args.output)
    if os.path.exists(output_filename):
        response = input(f"⚠️  File '{output_filename}' already exists. Overwrite? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Operation cancelled.")
            sys.exit(0)
    
    # Check if ffmpeg is available
    try:
        import subprocess
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: ffmpeg is required but not found in PATH")
        print("   Please install ffmpeg:")
        print("   - macOS: brew install ffmpeg")
        print("   - Ubuntu/Debian: sudo apt install ffmpeg")
        print("   - Windows: Download from https://ffmpeg.org/download.html")
        sys.exit(1)
    
    # Perform the download
    success = download_audio(args.url, args.output, args.bitrate)
    
    if success:
        print("\n🎉 Download completed successfully!")
        sys.exit(0)
    else:
        print("\n💥 Download failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()
