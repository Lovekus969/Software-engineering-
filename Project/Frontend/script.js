let voiceEnabled = true;
let speechRate = 1;

// Page Navigation
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });

    document.getElementById(pageId).classList.add('active');

    if (pageId === "scan") {
        startCamera();
    }
}

// Camera
let video = null;

window.onload = () => {
    video = document.getElementById('camera');

    document.getElementById("speed").addEventListener("input", function () {
        speechRate = this.value;
    });
};

function startCamera() {
    if (video.srcObject) return;

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Camera error:", err);
            alert("Camera not accessible");
        });
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
        updateUI(data.object, data.distance, data.direction);
    })
    .catch(err => {
        console.log("Backend not running — using demo mode");
        fakeDetection(); // 🔥 fallback
    });
}

// UI Update
function updateUI(obj, dist, dir) {
    document.getElementById('obj').innerText = obj;
    document.getElementById('dist').innerText = dist;
    document.getElementById('dir').innerText = dir;

    speak(`${obj} detected ${dir}, distance ${dist}`);
}

// 🔥 FAKE MODE (VERY IMPORTANT FOR DEMO)
function fakeDetection() {
    const objects = ["Bottle", "Chair", "Person"];
    const directions = ["Left", "Right", "Center"];

    const obj = objects[Math.floor(Math.random() * objects.length)];
    const dir = directions[Math.floor(Math.random() * directions.length)];
    const dist = (Math.random() * 2 + 0.5).toFixed(1) + "m";

    updateUI(obj, dist, dir);
}

// Text-to-Speech
function speak(text) {
    if (!voiceEnabled) return;

    const speech = new SpeechSynthesisUtterance(text);
    speech.rate = speechRate;

    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(speech);
}

// Toggle voice
function toggleVoice() {
    voiceEnabled = !voiceEnabled;
    alert("Voice " + (voiceEnabled ? "ON" : "OFF"));
}

// Reader
function readText() {
    const text = "Sample text detected from image";
    document.getElementById("readerOutput").innerText = text;
    speak(text);
}