import os, json, datetime
from gtts import gTTS

# Aaj ki date
DATE = datetime.datetime.now().strftime("%Y-%m-%d")
QUESTION = "UP Basic Education ka MDM full form kya hai?"
ANSWER_SHORT = "Mid Day Meal, ab PM POSHAN"
ANSWER_LONG = """
Mid Day Meal (MDM) yojana Bharat Sarkar ki ek bahut hi mahatvapurn yojana hai. Iska uddeshya sarkari aur sahayata prapt schools me bachchon ko muft me dopahar ka bhojan pradan karna hai.

Pehle iska naam Mid Day Meal tha, lekin ab iska naam badal kar **PM POSHAN (Pradhan Mantri Poshan Shakti Nirman)** kar diya gaya hai.

**PM POSHAN ke mukhya uddeshya:**
1. Bachchon ki poshan sthiti me sudhar karna.
2. School me namankan (enrollment) aur upasthiti (attendance) badhana.
3. Bachchon me samaanta aur bhai-chara badhana.

UP Assistant Teacher, Super TET aur TET pariksha me isse sambandhit prashn aksar pooche jate hain.

**Yaad karne ki trick:** MDM = Mid Day Meal = Dopahar ka Bhojan = PM POSHAN.
"""

TITLE = f"{QUESTION} - Full Details in Hindi"
TAGS = ["TET", "Praxis", "CDP", "UP Basic", "Super TET"]

# 1. AdSense Friendly Blogger HTML Generate karo (800+ words)
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{TITLE}</title>
</head>
<body>
<article>
<h1>{QUESTION}</h1>
<p><em>Last Updated: {DATE} | By My Basic Educator Team</em></p>

<p>UP Basic Education aur TET ki taiyari kar rahe hain? Aaj ka sabse important sawal hai - <strong>{QUESTION}</strong>. Chaliye isko detail me samajhte hain.</p>

<h2>{QUESTION} - Sahi Jawab</h2>
<p><strong>Sahi Jawab hai: {ANSWER_SHORT}</strong></p>
<p>{ANSWER_LONG}</p>

<h2>MDM se PM POSHAN tak ka safar</h2>
<p>Bharat me Mid Day Meal Yojana ki shuruat 15 August 1995 ko hui thi. 2021 me is yojana ko aur behtar banate hue iska naam PM POSHAN Yojana kar diya gaya. Is yojana ke tahat Class 1 se Class 8 tak ke sabhi bachchon ko poshak bhojan diya jata hai.</p>
<p>UP Basic Shiksha Parishad ke schools me ye yojana bahut hi safalta se chal rahi hai.</p>

<h2>Exam ke liye Important Points</h2>
<ul>
<li>MDM ka full form: Mid Day Meal</li>
<li>Naya Naam: PM POSHAN - Pradhan Mantri Poshan Shakti Nirman</li>
<li>Shuruat: 1995</li>
<li>Labharthi: Class 1 to 8</li>
<li>Mantralaya: Ministry of Education</li>
</ul>

<h2>FAQs - Aksar Pooche Jane Wale Sawal</h2>
<h3>Q1. MDM ka full form kya hai?</h3>
<p>Ans. MDM ka full form Mid Day Meal hai.</p>
<h3>Q2. PM POSHAN kya hai?</h3>
<p>Ans. PM POSHAN, MDM yojana ka hi naya naam hai, jiska pura naam Pradhan Mantri Poshan Shakti Nirman hai.</p>
<h3>Q3. Kya ye Super TET me poocha jata hai?</h3>
<p>Ans. Haan, UP Super TET aur Assistant Teacher bharti me is topic se har saal 1-2 sawal aate hain.</p>

<hr>
<p><strong>Disclaimer:</strong> Ye jankari shiksha ke uddeshya se di gayi hai. Kisi bhi sarkari yojana ki antim jankari ke liye official website dekhein. My Basic Educator kisi bhi sarkari sanstha se juda nahi hai.</p>
</article>
</body>
</html>
"""

# 2. JSON save
data = {"date": DATE, "title": TITLE, "description": html_content, "tags": TAGS}
os.makedirs("audio", exist_ok=True)
os.makedirs("blogger/MyBasicEducator", exist_ok=True)

with open(f"audio/{DATE}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(f"blogger/MyBasicEducator/{DATE}.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 3. Audio (Shorts ke liye chhota wala hi rakhenge)
tts = gTTS(text=f"{QUESTION}. Answer hai, {ANSWER_SHORT}. Detail ke liye blog dekhein.", lang='hi')
tts.save(f"audio/{DATE}.mp3")

print("AdSense Friendly Post Generated!")
