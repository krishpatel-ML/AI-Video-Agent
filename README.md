# AI Video Agent

AI pipeline that transcribes, summarizes, and lets you chat with YouTube videos or local audio/video files using Whisper, LLMs, and RAG.

## Overview

AI Video Agent takes a YouTube URL or a local video/audio file and automatically generates:
- A full transcript
- A concise summary
- Action items
- Key decisions
- Open questions

It then lets you ask follow-up questions about the content through a RAG-based Q&A engine — so you can "chat" with your meeting or video instead of re-watching it.

## Features

- 🎥 **Flexible input** — accepts YouTube URLs or local video/audio files
- 📝 **Transcription** — powered by Whisper (CPU-compatible)
- 📋 **Summarization** — auto-generated summary and title
- ✅ **Extraction** — action items, key decisions, and open questions pulled from the transcript
- 💬 **RAG Chat** — ask questions about the video content and get grounded answers
- 🖥️ **Streamlit UI** — clean web interface alongside a CLI entry point

## Tech Stack

- **Python**
- **Whisper** — audio transcription
- **LangChain** — RAG pipeline orchestration
- **Streamlit** — web UI
- **yt-dlp** — YouTube audio extraction
- **uv** — Python package management

## Project Structure

```
VIDEO_AGENT/
├── core/
│   ├── extractor.py       # Action items, decisions, questions extraction
│   ├── rag_engine.py      # RAG chain build + Q&A
│   ├── summarizer.py      # Summary + title generation
│   ├── transcriber.py     # Whisper-based transcription
│   └── vector_store.py    # Vector store for RAG
├── utils/
│   └── audio_processor.py # Audio ingestion (YouTube/local) + chunking
├── app.py                 # Streamlit web app
├── main.py                # CLI entry point
├── test.py                # Test script
└── requirement.txt        # Python dependencies
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/krishpatel-ML/ai-video-agent.git
   cd ai-video-agent
   ```

2. **Install dependencies** (using `uv`)
   ```bash
   uv pip install -r requirement.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root with your API keys:
   ```
   MISTRAL_API_KEY=your_key_here
   ```
   *(adjust based on the actual keys your project uses)*

## Usage

### CLI
```bash
uv run main.py
```
Enter a YouTube URL or local file path, choose a language, and follow the prompts.

### Streamlit Web App
```bash
uv run streamlit run app.py
```
Open the local URL shown in your terminal, paste a YouTube URL or file path in the sidebar, and click **Analyse**.

## Notes

- Transcription runs on CPU by default. GPU (`cuda`) support is available but may require additional driver/CUDA configuration depending on your hardware.
- Ensure `yt-dlp` is kept up to date (`uv pip install -U yt-dlp`) to avoid YouTube extraction errors.

## License

Add your preferred license here (e.g., MIT).
