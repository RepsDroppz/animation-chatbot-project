async function submitInput() {
    const textInput = document.getElementById('textInput').value;
    let response;

    if (textInput) {
        response = await fetch('http://localhost:5000/api/animate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: textInput }),
        });

        const result = await response.json();
        const outputArea = document.getElementById('outputArea');
        outputArea.innerHTML = `<video controls src="${result.animation}" width="600"></video>`;
    } else {
        document.getElementById('outputArea').innerHTML = 'Please enter text to create an animation.';
    }
}
