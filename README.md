# Audiobook Revamper

Use AI to shorten an re-narrate audiobooks.

⚠️ This is a prototype. Your mileage may vary. ⚠️

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

- [Replicate](https://replicate.com) account for running language and speech-to-text models
- [Eleven Labs](https://elevenlabs.io/) account for running text-to-speech models
- Python environment (your computer, or Replit, or Google Colab)

## Usage

Add your [Replicate API token](https://replicate.com/account) and [Eleven Labs API key](https://elevenlabs.io/) to your environment:

```sh
export REPLICATE_TOKEN=r8_foobarbazzledazzle
export ELEVEN_LABS_API_KEY=eleventybillion
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

- **Play with models in the browser.** When first tinkering with an unfamiliar model, running it on Replicate's web UI makes it easier to get started, play with inputs, visualize outputs, then [grab some code](https://replicate.com/vaibhavs10/incredibly-fast-whisper?input=python) and run with it.

- **Use the Replicate dashboard** to dig into your [recent predictions](https://replicate.com) and get a helpful view of inputs, outputs, and metrics.

- **Use [Replicate deployments](https://replicate.com/docs/deployments).** Deploying your own copy of a model on Replicate gives you control over min/max instances, so you can keep a model on while you're prototyping and turn it down to zero when you're done.

- **Use Python for prototyping.** ChatGPT is good at writing Python. Python has a big standard library so you can build stuff with fewer external dependencies. No ESM/CJS shenanigans. Better Replicate client library experienc for working with local files.

- **Use Node.js for real products.** When you start building something that's going to have real users, Vercel+Next.js is a winning combination. Instead of expensive long-running processes, use webhooks + serverless functions to minimize costs.

- **Use run counts as a proxy for model quality.** - There are many [whisper variants](https://replicate.com/explore?query=whisper). Some are better than others. Some do diarization. Some fall over on large audio files. A high run count is usually a good indication that people are using a model with success.

## Extra credit

- Try running the language model locally using Ollama's [Python](https://github.com/ollama/ollama-python) or [JavaScript](https://github.com/ollama/ollama-js) client libraries.
- Try replacing Eleven Labs with a [Replicate-hosted text-to-speech model](https://replicate.com/explore?query=tts).
- Play around with the summary prompts. How do you get the best "compression" while still maintaining the essence of the original text?
- Bring your own audio file as voice training data. Eleven Labs supports training on the fly without pre-creating a voice.
- Build an app that finds and extracts utterances in audio that are followed by laughter.