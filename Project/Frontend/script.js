let voiceEnabled = true;
let speechRate = 1;

// Page Navigation
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(pageId).classList.add('active');

    if (pageId === "scan") startCamera();
}

// Camera
let video = document.getElementById('camera');

function startCamera() {
    if (video.srcObject) return; // already running

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => console.error("Camera error:", err));
}

// Auto Scan every 4 seconds
setInterval(() => {
    if (!video || !video.srcObject) return;
    captureImage();
}, 4000);

// Capture image and send to backend
function captureImage() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL('image/png');

    fetch('http://127.0.0.1:5000/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(res => res.json())
    .then(data => {
        // Update info panel
        document.getElementById('obj').innerText = data.object;
        document.getElementById('dist').innerText = data.distance;
        document.getElementById('dir').innerText = data.direction;

        // Speak result
        const message = `${data.object}, ${data.distance}, ${data.direction}`;
        speak(message);
    })
    .catch(err => console.error("Backend error:", err));
}

// Text-to-Speech
function speak(text) {
    if (!voiceEnabled) return;
    const speech = new SpeechSynthesisUtterance(text);
    speech.rate = speechRate;
    window.speechSynthesis.cancel(); // stop previous
    window.speechSynthesis.speak(speech);
}

// Settings
document.getElementById("speed").addEventListener("input", function () {
    speechRate = this.value;
});

function toggleVoice() {
    voiceEnabled = !voiceEnabled;
    alert("Voice " + (voiceEnabled ? "ON" : "OFF"));
}

// Reader (dummy for now)
function readText() {
    const text = "Sample text detected from image";
    document.getElementById("readerOutput").innerText = text;
    speak(text);
}