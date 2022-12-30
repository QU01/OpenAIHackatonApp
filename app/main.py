from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import replicate
from app.historyGenerator import generate_history
from app.imageGenerator import generate_image

app = Flask(__name__)
replicate.default_client.api_token = "29cd0146aaedc65bc5c87cc50e26f66df46c3163"
model = replicate.models.get("openai/whisper")
model = model.versions.get("30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed")

@app.route("/api/upload-audio", methods=["POST"])
def upload_audio():

    print(request)

    if "audio" not in request.files:
        return "No se ha encontrado ningún archivo de audio en la solicitud", 400

    audio_file = request.files["audio"]

    if audio_file.filename == "":
        return "No se ha proporcionado un nombre de archivo", 400

    filename = secure_filename(audio_file.filename)
    audio_file.save(filename)

    options = {"fp16": False, "language": None, "task": "transcribe"}
    results = model.predict(audio=open(filename, 'rb'))['transcription']

    history = generate_history(results["text"])
    image = generate_image(results["text"])

    response = {
        "transcription": results["text"],
        "image": image,
        "history": history
        }
    return jsonify(response), 200




