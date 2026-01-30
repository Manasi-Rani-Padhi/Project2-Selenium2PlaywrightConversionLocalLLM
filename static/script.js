document.getElementById('convertBtn').addEventListener('click', async () => {
    const sourceCode = document.getElementById('sourceCode').value;
    const targetLang = document.getElementById('targetLang').value;
    const loader = document.getElementById('loader');
    const outputCode = document.getElementById('outputCode');

    if (!sourceCode.trim()) {
        alert("Please enter some Java code.");
        return;
    }

    loader.classList.remove('hidden');

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                source_code: sourceCode,
                target_lang: targetLang
            }),
        });

        const data = await response.json();

        if (response.ok) {
            outputCode.textContent = data.converted_code;
        } else {
            outputCode.textContent = "Error: " + (data.detail || "Unknown error occurred.");
        }
    } catch (error) {
        outputCode.textContent = "Error: Could not connect to the server.";
        console.error(error);
    } finally {
        loader.classList.add('hidden');
    }
});

document.getElementById('copyBtn').addEventListener('click', () => {
    const code = document.getElementById('outputCode').textContent;
    navigator.clipboard.writeText(code).then(() => {
        const btn = document.getElementById('copyBtn');
        const originalText = btn.textContent;
        btn.textContent = "Copied!";
        setTimeout(() => {
            btn.textContent = originalText;
        }, 2000);
    });
});
