async function runCode() {
    const code = document.getElementById('code').value;
    const response = await fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code })
    });
    const result = await response.json();
    document.getElementById('output').innerText = result.output || result.error;
}
