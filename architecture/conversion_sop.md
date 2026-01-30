# SOP: Conversion Logic (Selenium Java to Playwright)

## Overview
This SOP defines how requested Selenium Java code parsed from TestNG tests is converted into Playwright JS/TS.

## Logic Flow
1. **Input Reception**: Receive raw Java string.
2. **Context Enrichment**: Prepend Playwright best practices and the conversion mapping to the prompt.
3. **LLM Inference**: Call Ollama (`llama3.2:3b` preferred) with a system instruction to convert code.
4. **Validation**: Ensure the output contains basic Playwright keywords (`page`, `await`, `test`).
5. **Output Generation**: Return the formatted JS/TS code.

## Mapping Table
Refer to `findings.md` for the latest mapping table.

## Edge Cases
- **Unsupported Annotations**: If a TestNG annotation isn't mapped, wrap it in a comment in the output.
- **Complex Page Objects**: Inform the user if the logic is too complex for 1:1 conversion and provide a skeleton.
- **Timeouts**: Convert `Thread.sleep` to `page.waitForTimeout` but warn against it.
