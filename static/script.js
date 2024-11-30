// function uploadImage() {
//     const fileInput = document.getElementById('imageInput');
//     const resultDisplay = document.getElementById('result');
//     const file = fileInput.files[0];

//     if (file) {
//         const formData = new FormData();
//         formData.append('image', file);

//         fetch('/detect_skin_tone', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             resultDisplay.innerText = "Skin Tone Detected: " + data.result;
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             resultDisplay.innerText = 'An error occurred. Please try again.';
//         });
//     } else {
//         resultDisplay.innerText = 'Please select an image first.';
//     }
// }








// async function uploadImage() {
//     const input = document.getElementById('imageInput');
//     const file = input.files[0];
//     const formData = new FormData();
//     formData.append('file', file);

//     const response = await fetch('/predict', {
//         method: 'POST',
//         body: formData
//     });

//     const data = await response.json();
//     document.getElementById('result').innerText = data.predicted_skin_tone || data.error;
// }
