import tkinter as tk
import customtkinter as ctk
import soundfile as sf
import sounddevice as sd
import requests
#from diffusers import StableDiffusionPipeline
#from huggingface_hub import login

# pip install git+https://github.com/openai/whisper.git


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
    pass


def generate_image():
    pass

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