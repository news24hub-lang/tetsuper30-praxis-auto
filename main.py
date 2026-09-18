import os, json, random
from datetime import datetime
from gtts import gTTS

# Daily TET / Praxis Topics
QUIZ_TOPICS = [
    {"q": "Child Development me Piaget ke kitne stages hote hain?", "options": ["3", "4", "5", "2"], "ans": "4", "explain": "Piaget ne 4 stages bataye hain - Sensorimotor, Preoperational, Concrete, Formal."},
    {"q": "UP Basic Education ka MDM full form kya hai?", "options": ["Mid Day Meal", "Mid Daily Meal", "Main Day Meal", "Meal Day Management"], "ans": "Mid Day Meal", "explain": "MDM matlab Mid Day Meal yojana."},
    {"q": "Praxis exam kis country me teachers ke liye hota hai?", "options": ["USA", "UK", "India", "Canada"], "ans": "USA", "explain": "Praxis USA me teacher certification ke liye hota hai."},
]

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    quiz = random.choice(QUIZ_TOPICS)
    
    # Create audio folder
    os.makedirs("audio", exist_ok=True)
    
    text_for_audio = f"Today's Quiz. {quiz['q']} Options are. {', '.join(quiz['options'])}. Correct answer is {quiz['ans']}. {quiz['explain']}"
    
    # Generate MP3
    tts = gTTS(text=text_for_audio, lang='hi', slow=False)
    mp3_path = f"audio/quiz-{today}.mp3"
    tts.save(mp3_path)
    
    # Save JSON for website
    os.makedirs("blogger/MyBasicEducator/quiz", exist_ok=True)
    with open(f"blogger/MyBasicEducator/quiz/{today}.json", "w", encoding="utf-8") as f:
        json.dump({"date": today, "quiz": quiz, "audio": mp3_path}, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {mp3_path}")

if __name__ == "__main__":
    main()
