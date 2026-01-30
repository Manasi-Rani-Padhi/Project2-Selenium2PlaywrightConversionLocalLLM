# Gemini: Project Constitution

## Project: Selenium Java to Playwright JS/TS Converter

### Data Schemas

#### Input Payload (UI/API)
```json
{
  "source_code": "String (Selenium Java Code)",
  "target_language": "javascript | typescript",
  "framework": "testng"
}
```

#### Output Payload (Conversion Result)
```json
{
  "converted_code": "String (Playwright JS/TS)",
  "metadata": {
    "original_framework": "testng",
    "conversion_status": "success | error",
    "warnings": ["Array of conversion warnings"]
  },
  "file_path": "String (.tmp/output/...) "
}
```

### Behavioral Rules
- Prioritize readability and Playwright idiomatic patterns (e.g., `locators`, `await expect`).
- Handle TestNG annotations (`@Test`, `@BeforeMethod`, etc.) by mapping them to Playwright test hooks (`test`, `test.beforeEach`).
- Prioritize readability over strict 1:1 mapping.
- Convert everything provided in the input.

### Architectural Invariants
- 3-Layer Architecture (Architecture, Navigation, Tools).
- All intermediate data in `.tmp/`.
- `gemini.md` is the source of truth for schema and rules.

---
## Maintenance Log
- 2026-01-31: Project initialized using B.L.A.S.T. protocol.
- 2026-01-31: Full implementation completed including FastAPI backend and Glassmorphic frontend.
