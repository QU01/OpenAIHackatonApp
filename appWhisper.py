import tkinter as tk
import customtkinter as ctk
import soundfile as sf
import sounddevice as sd
import requests
#from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from huggingface_hub import login
import openai

# pip install git+https://github.com/openai/whisper.git
import whisper

model = whisper.load_model("small")

openai.api_key = os.getenv("OPENAI_API_KEY")

#With Stable Diffusion

"""
login()




pipe = StableDiffusionPipeline.from_pretrained(
    'CompVis/stable-diffusion-v1-4',
    revision='fp16',
    torcj_dtype=torch.float16,
    use_auth_token=True
)

pipe = pipe.to("cpu")

"""

#create the app

def voice_rec():
    fs = 48000

    # seconds
    duration = 5
    main_label.configure(text="Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write("audio.wav", myrecording, fs)
    main_label.configure(text="Recording done")

def transcribe():
    audio = "audio.wav"

    # You can provide the language to the model if it is a bit to "exotic" to predict
    options = {"fp16": False, "language": None, "task": "transcribe"}
    results = model.transcribe(audio, **options)

    print(results["text"])
    main_label.configure(text=results["text"])


def generate_image():
    audio = "audio.wav"

    # You can provide the language to the model if it is a bit to "exotic" to predict
    options = {"fp16": False, "language": None, "task": "translate"}
    results = model.transcribe(audio, **options)

    text = results["text"]

    response = openai.Image.create(prompt=text, n=2, size="1024x1024")

    image = response["data"][0]["url"]

    img_data = requests.get(image).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)

    
    image = mpimg.imread('image_name.jpg')
    

    plt.imshow(image)
    plt.title(text)
    plt.axis('off')
    plt.show()

    main_label.configure(text=results["text"])

app = tk.Tk()
app.geometry("532x632")
app.title("Voice to text")
ctk.set_appearance_mode("dark")

main_label = ctk.CTkLabel(
    master=app, height=512, width=512, text_color="black", font=("Roboto Medium", -16)
)
main_label.place(x=10, y=110)


#run app

recordButton = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=voice_rec,
)
recordButton.configure(text="Record")
recordButton.place(x=206, y=60)

transcribeButton = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=transcribe,
)
transcribeButton.configure(text="Transcribe")
transcribeButton.place(x=106, y=150)

translateButton = ctk.CTkButton(
    master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=generate_image,
)
translateButton.configure(text="Generate Image")
translateButton.place(x=306, y=150)


# run app
app.mainloop()