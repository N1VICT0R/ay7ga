from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ YouTube Audio API is Running."

@app.route("/api/stream", methods=["GET"])
def stream_audio():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing YouTube URL"}), 400
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "skip_download": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({"audioUrl": info["url"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
