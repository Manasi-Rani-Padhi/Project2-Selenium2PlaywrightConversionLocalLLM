#!/bin/bash

echo "🚀 Starting Selenium to Playwright Converter..."
echo "📍 Backend: http://localhost:8000"

# Kill any existing uvicorn process on port 8000
fuser -k 8000/tcp 2>/dev/null

# Start the server
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
