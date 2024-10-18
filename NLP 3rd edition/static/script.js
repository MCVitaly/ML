document.getElementById('url-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const url = document.getElementById('url-input').value;
    fetch('/extract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerHTML = `<p>Error: ${data.error}</p>`;
        } else {
            const products = data.products.join(', ');
            document.getElementById('result').innerHTML = `<p>Extracted Products: ${products}</p>`;
        }
    })
    .catch(error => {
        document.getElementById('result').innerHTML = `<p>An error occurred: ${error}</p>`;
    });
});
