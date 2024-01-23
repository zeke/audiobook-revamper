# Audiobook Revamper

Use AI models to shorten audiobooks and renarrate them in a custom voice.

⚠️ This is an alpha-quality prototype. Your mileage may vary. ⚠️

## Why?

- Reading is hard for some people, like me.
- Some narrators don't have soothing voices.
- Some audiobooks are too long.

## How it works

1. **Download** an audiobook from Audible as an M4B file using [OpenAudible](https://openaudible.org).
1. **Chapterize** the M4B file into individual M4A audio files using FFMPEG.
1. **Transcribe** chapter audio files to text using [WhisperX](https://replicate.com/daanelson/whisperx).
1. **Shorten** chapter text using [Llama](https://replicate.com/meta/llama-2-70b-chat) or [Mixtral](https://replicate.com/mistralai/mixtral-8x7b-instruct-v0.1).
1. **Speak** new chapter in a custom voice using a text-to-speech model like [Eleven Labs](https://elevenlabs.io/voice-lab).

## Prerequisites

- [Replicate](https://replicate.com) account
- Python environment (your computer, or Replit, or Google Colab)

## Usage

Add your [Replicate API token](https://replicate.com/account) to your environment:

```sh
export REPLICATE_TOKEN=r8_foobarbazzledazzle
```

Install Python dependencies and run the script:

```sh
pip install -r requirements.txt
```

Split audiobook into individual chapters

```sh
python chapterize audiobook.m4b
```

Redo a chapter, shortened and renarrated

```sh
python compose.py chapters/*.mp3
```

## Tips

- **Start in the browser.** When first tinkering with a model, running it on Replicate's web UI make it easier to get started, play with inputs, visualize outputs, then grab some code and run with it.

- **Use [Replicate deployments](https://replicate.com/docs/deployments).** Deploying your own copy of a model on Replicate gives you control over min/max instances, so you can keep a model on while you're prototyping and turn it down to zero when you're done.

- **Use Python for prototyping.** ChatGPT is good at writing Python. Python has a big standard library so you can build stuff with fewer external dependencies. No ESM/CJS shenanigans. Better Replicate client library experienc for working with local files.

- **Use Node.js for real products.** When you start building something that's going to have real users, Vercel+Next.js is a winning combination. Instead of expensive long-running processes, use webhooks + serverless functions to minimize costs.

- **Use run counts as a proxy for model quality.** - There are many [whisper variants](https://replicate.com/explore?query=whisper). Some are better than others. Some do diarization. Some fall over on large audio files. A high run count is usually a good indication that people are using a model with success.

- Idea: Find the utterances that are followed by laughter