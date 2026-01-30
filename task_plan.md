# Task Plan - Selenium Java to Playwright JS/TS Converter

## Phase 1: Blueprint (Vision & Logic)
- [x] Answer Discovery Questions
- [x] Define Data Schema in `gemini.md`
- [x] Research existing Selenium converters and Playwright APIs
- [x] Define conversion mapping (Selenium commands -> Playwright commands)

## Phase 2: Link (Connectivity)
- [x] Verify local LLM connectivity (Ollama)
- [x] Verify environment for FastAPI/Frontend development

## Phase 3: Architect (The 3-Layer Build)
- [x] Create Architecture SOPs for:
    - [x] Java Parsing Logic (LLM Prompting)
    - [x] Playwright Code Generation
- [x] Build Tools:
    - [x] `ollama_client.py`: Interface with local LLM.
    - [x] `converter.py`: Orchestrates conversion logic.
    - [x] `app.py`: FastAPI backend for the UI.

## Phase 4: Stylize (Refinement & UI)
- [x] Build Glassmorphic Web UI:
    - [x] Code input area (Java).
    - [x] Language toggle (JS/TS).
    - [x] Result display (Playwright).
    - [x] "Download/Save" button.

## Phase 5: Trigger (Deployment)
- [x] Finalize local server script.
- [x] Documentation update in `gemini.md`.
