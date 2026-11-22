# Veyra

Semester-sized AI/ML project: React frontend + FastAPI backend that uses FFmpeg, Groq Whisper (speech-to-text), Google Gemini and MongoDB.

> Status: folder structure and placeholders only (ready for Phase 1).

## Structure

```
veyra/
├── client/                  # React + Vite, plain CSS
│   ├── public/images/
│   ├── src/
│   │   ├── components/      # Navbar, VideoUploader, VideoPlayer, Summary,
│   │   │                    # Transcript, LanguageSelector, Chapters
│   │   ├── pages/           # Home, Results
│   │   ├── services/api.js  # backend calls
│   │   ├── css/             # Home.css, Results.css, Components.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── server/                  # FastAPI
│   ├── routes/video_routes.py
│   ├── services/            # video_processor, transcription, frame_analyzer,
│   │                        # summarizer, content_classifier, translator
│   ├── models/schemas.py
│   ├── database/db.py
│   ├── uploads/             # temporary files (git-ignored)
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── .gitignore
└── README.md
```

## Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- FFmpeg (`brew install ffmpeg` on macOS; `sudo apt install ffmpeg` on Ubuntu)
- MongoDB (local, or a MongoDB Atlas connection string)
- API keys: [Groq](https://console.groq.com) and [Google AI Studio](https://aistudio.google.com)

## Setup

### Backend
```bash
cd server
python3 -m venv venv            # skip if venv/ already exists
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env         # then edit .env and add your keys
```

### Frontend
```bash
cd client
npm install
```

## Run

```bash
# Terminal 1 - backend (http://localhost:8000, docs at /docs)
cd server && source venv/bin/activate
uvicorn main:app --reload

# Terminal 2 - frontend (http://localhost:5173)
cd client && npm run dev
```

## Security

Secrets live only in `server/.env`, which is git-ignored. Commit `server/.env.example` only, with placeholder values.
