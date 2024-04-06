function extractText() {
    const input = document.getElementById('imageInput');
    const resultContainer = document.getElementById('result');

    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = new Image();
            img.src = e.target.result;

            img.onload = function () {
                
                const ocrApiEndpoint = 'YOUR_OCR_API_ENDPOINT';

                
                fetch(ocrApiEndpoint, {
                    method: 'POST',
                    body: JSON.stringify({ image: e.target.result }),
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(response => response.json())
                .then(data => {
                    resultContainer.textContent = data.text;
                })
                .catch(error => {
                    console.error('Error:', error);
                    resultContainer.textContent = 'Error extracting text.';
                });
            };
        };
        reader.readAsDataURL(file);
    } else {
        resultContainer.textContent = 'Please select an image.';
    }
}
