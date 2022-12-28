import replicate

replicate.default_client.api_token = "29cd0146aaedc65bc5c87cc50e26f66df46c3163"


model = replicate.models.get("openai/whisper")
version = model.versions.get("30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed")
output = version.predict(audio=open("audio.wav", 'rb'))

print(output)