from transformers import AutoProcessor, AutoModelForCTC

processor = AutoProcessor.from_pretrained("codenamewei/speech-to-text")

model = AutoModelForCTC.from_pretrained("codenamewei/speech-to-text")

import wave

# Open the audio file using the wave module
with wave.open(r'data\test\TestAudio.wav', 'rb') as audio_file:
    # Extract the audio data and sample rate from the file
    audio_data = audio_file.readframes(audio_file.getnframes())
    sample_rate = audio_file.getframerate()

# Preprocess the audio data to convert it into a format that can be fed into the transformer model
# This might involve converting the audio data into a different sample rate, encoding it into a specific format, etc.

# Feed the preprocessed audio data into the transformer model
prediction = model.predict(audio_data)
#use audio file as input and predict the text
print(prediction)
# import torch

# import librosa
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # Load the audio file
# y, sr = librosa.load("data/test/TestAudio.wav")

# # Compute the STFT of the audio signal
# stft = librosa.core.stft(y)

# # Convert the STFT matrix to a PyTorch tensor
# input_tensor = torch.tensor(stft).unsqueeze(0)

# # Move the input tensor to the device where the model will be run
# input_tensor = input_tensor.to(device)

# generate the transcription using the model
output = model("data/test/TestAudio.wav", return_dict=True)
transcription = output['prediction'][0]

# decode the transcription
#transcription = processor.postprocess(transcription)
print(transcription)
