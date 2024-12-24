import librosa
import numpy as np
from keras.models import load_model

# Load a pre-trained model (you need to have a trained model in .h5 format)
model = load_model("models/speech_emotion_model.h5")

def extract_audio_features(file_path):
    y, sr = librosa.load(file_path, duration=2.5, offset=0.6)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def analyze_speech_emotion(audio_path):
    try:
        features = extract_audio_features(audio_path)
        features = features.reshape(1, -1)
        prediction = model.predict(features)
        emotion = np.argmax(prediction)
        return emotion
    except Exception as e:
        return "Error: " + str(e)
