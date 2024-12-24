from App.sentiment_analysis import analyze_text_sentiment
from App.facial_emotion_recognition import analyze_facial_emotion
from App.speech_emotion_recognition import analyze_speech_emotion
from App.task_recommendation import recommend_task


def main_system(text, image_path, audio_path):
    # Analyze text sentiment
    text_sentiment, _ = analyze_text_sentiment(text)
    
    # Analyze facial emotion
    facial_emotion = analyze_facial_emotion(image_path)
    
    # Analyze speech emotion
    speech_emotion = analyze_speech_emotion(audio_path)
    
    # Aggregate emotions (majority voting)
    emotions = [text_sentiment, facial_emotion, speech_emotion]
    dominant_emotion = max(set(emotions), key=emotions.count)
    
    # Get task recommendations
    tasks = recommend_task(dominant_emotion)
    
    return {
        "dominant_emotion": dominant_emotion,
        "recommended_tasks": tasks
    }

if __name__ == "__main__":
    # Example inputs
    text_input = "I am feeling a bit stressed today."
    image_path = "sample_employee_photo.jpg"
    audio_path = "sample_employee_audio.wav"

    # Run the system
    result = main_system(text_input, image_path, audio_path)
    print("Dominant Emotion:", result["dominant_emotion"])
    print("Recommended Tasks:", result["recommended_tasks"])
