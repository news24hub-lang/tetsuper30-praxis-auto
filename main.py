import os, json, random
from datetime import datetime
from gtts import gTTS

QUIZ_TOPICS = [
    {"q": "Child Development me Piaget ke kitne stages hote hain?", "a": "4 stages - Sensorimotor, Preoperational, Concrete, Formal", "topic": "CDP"},
    {"q": "UP Basic Education ka MDM full form kya hai?", "a": "Mid Day Meal, ab PM POSHAN", "topic": "UP Basic"},
    {"q": "Praxis exam kis country me teacher banne ke liye hota hai?", "a": "USA me teacher certification ke liye", "topic": "Praxis"},
    {"q": "NEP 2020 me 5+3+3+4 structure kya hai?", "a": "Naya school structure hai", "topic": "NEP"},
    {"q": "Brianna case study me kya problem hoti hai?", "a": "Reading comprehension issue", "topic": "Praxis 5205"}
]

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    quiz = random.choice(QUIZ_TOPICS)
    
    os.makedirs("audio", exist_ok=True)
    os.makedirs("blogger/MyBasicEducator", exist_ok=True)
    
    text_for_audio = f"Today's Quiz. {quiz['q']}. Answer is {quiz['a']}"
    
    # Generate MP3 - Hindi + English mix
    tts = gTTS(text=text_for_audio, lang='hi', slow=False)
    tts.save(f"audio/{today}.mp3")
    
    # Create Blogger HTML + YT Shorts Script
    html_content = f"""
    <h2>{quiz['q']}</h2>
    <p><b>Answer:</b> {quiz['a']}</p>
    <p>Date: {today} | Topic: {quiz['topic']}</p>
    """
    
    with open(f"blogger/MyBasicEducator/{today}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # For YouTube Shorts description
    yt_data = {
        "date": today,
        "title": f"{quiz['q']} #shorts #tet #praxis",
        "description": f"{quiz['q']}\n\nAnswer: {quiz['a']}\n\nFull notes on mybasiceducator.com",
        "tags": ["TET", "Praxis", "CDP", quiz['topic']]
    }
    
    with open(f"audio/{today}.json", "w", encoding="utf-8") as f:
        json.dump(yt_data, f, ensure_ascii=False, indent=2)
    
    print(f"Done for {today}: {quiz['q']}")

if __name__ == "__main__":
    main()
