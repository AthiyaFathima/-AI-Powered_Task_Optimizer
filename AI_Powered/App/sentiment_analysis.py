from transformers import pipeline

# Load the Hugging Face pipeline for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_text_sentiment(text):
    try:
        result = sentiment_analyzer(text)
        sentiment = result[0]["label"]
        confidence = result[0]["score"]
        return sentiment, confidence
    except Exception as e:
        return "Error", str(e)
