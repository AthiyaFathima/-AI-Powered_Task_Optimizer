from deepface import DeepFace

def analyze_facial_emotion(image_path):
    try:
        analysis = DeepFace.analyze(image_path, actions=["emotion"])
        return analysis["dominant_emotion"]
    except Exception as e:
        return "Error: " + str(e)
