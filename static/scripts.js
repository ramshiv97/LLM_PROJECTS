document.getElementById('queryForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = document.getElementById('queryInput').value;

    try {
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query }),
        });
        const data = await response.json();
        document.getElementById('resultOutput').textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        document.getElementById('resultOutput').textContent = `Error: ${err.message}`;
    }
});
