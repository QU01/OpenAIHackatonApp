from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import whisper
from historyGenerator import generate_history
from imageGenerator import generate_image

app = Flask(__name__)
model = whisper.load_model("small")

@app.route("/api/upload-audio", methods=["POST"])
def upload_audio():
    if "audio" not in request.files:
        return "No se ha encontrado ningún archivo de audio en la solicitud", 400

    audio_file = request.files["audio"]

    if audio_file.filename == "":
        return "No se ha proporcionado un nombre de archivo", 400

    filename = secure_filename(audio_file.filename)
    audio_file.save(filename)

    options = {"fp16": False, "language": None, "task": "transcribe"}
    results = model.transcribe(filename, **options)

    history = generate_history(results["text"])
    image = generate_image(results["text"])

    response = {
        "transcription": results["text"],
        "image": image,
        "history": history
        }
    return jsonify(response), 200

@app.route("/api/get-transcription", methods=["GET"])
def get_transcription():
    global transcription

    if transcription is None:
        return "No se ha procesado ningún archivo de audio todavía", 400

    return transcription

if __name__ == "__main__":
    app.run()




