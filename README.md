# Audiobook Revamper

This project takes M4B audio files, splits them into individual chapters, transcribes the chapters to text, shortens the text, and converts the shortened text back to speech using custom voices.

⚠️ This is a work in progress. It's not ready for use yet.

## Usage

```sh
pip install -r requirements.txt

# split audiobook into individual chapters
python chapterize audiobook.m4b

# redo a chapter, shortened and renarrated
python compose.py chapters/*.mp3
```

## Credits

- https://openaudible.org for downloading audiobooks as M4B files
- https://github.com/jansendotsh/m4b-split for splitting M4B files into chapters
- https://replicate.com/daanelson/whisperx for transcription
- https://replicate.com/mistralai/mixtral-8x7b-instruct-v0.1 for text shortening
- https://elevenlabs.io/voice-lab for text to speech