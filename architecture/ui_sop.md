# SOP: Web Interface (FastAPI + Vanilla JS)

## Overview
A web-based interface for users to paste Java code and receive Playwright code.

## Components
1. **Backend (FastAPI)**:
    - `POST /convert`: Accepts Java code, calls `converter.py`, returns JS/TS.
    - `GET /`: Serves the static `index.html`.
2. **Frontend (Vanilla HTML/CSS/JS)**:
    - **Aesthetics**: Glassmorphism, dark mode.
    - **Inputs**: Textarea for Java code, dropdown for Target (JS/TS).
    - **Display**: Syntax-highlighted (or formatted) result area.

## Data Flow
1. User clicks "Convert".
2. JS sends fetch request to `/convert`.
3. Backend processes via `ollama_client.py`.
4. Response is displayed in the UI.
