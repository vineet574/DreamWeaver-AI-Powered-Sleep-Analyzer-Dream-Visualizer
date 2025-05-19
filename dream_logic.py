import random

def analyze_sleep(data):
    duration = len(data)
    deep = sum(1 for d in data if d < 0.3)
    rem = sum(1 for d in data if 0.3 <= d <= 0.6)
    return {
        'duration': duration,
        'deep_sleep_minutes': deep,
        'rem_minutes': rem,
        'score': int((deep + rem) / duration * 100)
    }

def detect_emotion(journal):
    journal = journal.lower()
    if any(word in journal for word in ['happy', 'joy', 'laugh']):
        return 'joyful'
    elif any(word in journal for word in ['scared', 'dark', 'monster']):
        return 'fearful'
    elif any(word in journal for word in ['love', 'hug', 'kiss']):
        return 'romantic'
    return 'mysterious'

def generate_dream_image(emotion):
    prompts = {
        'joyful': 'a bright sunny meadow with butterflies',
        'fearful': 'a dark forest with shadows and glowing eyes',
        'romantic': 'a night sky with stars and two figures under moonlight',
        'mysterious': 'a surreal dreamscape with floating islands and fog'
    }
    return f"https://dummyimage.com/600x400/000/fff&text={prompts[emotion].replace(' ', '+')}"
