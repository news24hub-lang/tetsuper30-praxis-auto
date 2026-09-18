import json, os, random
from datetime import datetime

TOPICS = [
 {
  "keyword": "Prerna DBT App Status Check",
  "title": "Prerna DBT App Status Check Kaise Kare 2026 - Step by Step Guide",
  "intro": "Uttar Pradesh ke basic teachers ke liye Prerna DBT App bahut zaruri hai.",
  "h1": "Prerna DBT Kya Hai?",
  "p1": "Prerna DBT (Direct Benefit Transfer) ek yojana hai jisme students ke account me paise bheje jate hain. Teachers ko iska status update karna hota hai.",
  "h2": "Prerna DBT Status Check Karne Ka Tarika",
  "p2": "1. Prerna portal par login karein. 2. DBT module par click karein. 3. UDISE code dalein. 4. Student list me status dekhein. Agar pending hai to documents re-upload karein.",
  "h3": "DBT Me Aane Wali Samasyaen",
  "p3": "Aksar Aadhaar mismatch ya bank error se DBT fail ho jata hai. Parents se sahi documents lekar update karein. Technical issue ho to BRC par sampark karein."
 },
 {
  "keyword": "MDM Calculator UP",
  "title": "MDM Calculator UP 2026 - Mid Day Meal Hisab Kaise Lagayen",
  "intro": "UP ke primary schools me MDM ka hisab lagana har teacher ki zimmedari hai.",
  "h1": "MDM Kya Hai?",
  "p1": "Mid Day Meal me bachchon ko dopahar ka bhojan diya jata hai. Sarkar chawal, gehun aur conversion cost deti hai.",
  "h2": "MDM Calculator Kaise Use Karein",
  "p2": "1. Month select karein. 2. Attendance dalein. 3. Primary 100g aur Upper Primary 150g ka ration auto calculate hoga. 4. Print karke register me chipka dein.",
  "h3": "MDM Ke Naye Niyam 2026",
  "p3": "2026 me nutrition badhane ke liye millet bhi dena hai. Iska record portal par upload karna hoga."
 }
]

today = datetime.now().strftime("%Y-%m-%d")
today_long = datetime.now().strftime("%d %B %Y")
topic = random.choice(TOPICS)

html = f"""
<p><em>Last Updated: {today_long} | By MyBasicEducator Team</em></p>
<p>{topic['intro']} Is article me hum {topic['keyword']} ki puri jankari denge.</p>
<h2>{topic['h1']}</h2>
<p>{topic['p1']} UP Basic Education Department ne is process ko digital kar diya hai.</p>
<h2>{topic['h2']}</h2>
<p>{topic['p2']} Teachers ko salah hai ki ve daily data update karein.</p>
<h2>{topic['h3']}</h2>
<p>{topic['p3']}</p>
<h2>Important Links</h2>
<ul><li>prernaup.in</li><li>udiseplus.gov.in</li><li>mdm.nic.in</li></ul>
<h2>FAQs</h2>
<p><b>Q. {topic['keyword']} kaise karein?</b><br>Ans: Upar diye steps follow karein.</p>
<p><b>Q. Error aaye to kya karein?</b><br>Ans: BRC ya BEO se sampark karein.</p>
<h3>Conclusion</h3>
<p>Umeed hai ye jankari pasand aayi hogi. Aise hi updates ke liye MyBasicEducator.com par bane rahein.</p>
<p><b>Disclaimer:</b> Ye jankari official portals ke adhar par hai. Official website zarur check karein.</p>
"""

post = {"title": topic['title'], "content": html, "labels": f"{topic['keyword']}, Basic Teacher, UP News"}

os.makedirs(f"blogger/MyBasicEducator/{today}", exist_ok=True)
with open(f"blogger/MyBasicEducator/{today}/adsense_post.json","w",encoding="utf-8") as f:
    json.dump(post,f,indent=2,ensure_ascii=False)

print("AdSense Post Ready")

# --- AUDIO PUBLISH ON ---
try:
    from gtts import gTTS
    os.makedirs(f"blogger/MyBasicEducator/{today}", exist_ok=True)
    title_for_audio = topic['title']
    tts = gTTS(text=title_for_audio, lang='hi', slow=False)
    tts.save(f"blogger/MyBasicEducator/{today}/audio.mp3")
    print("AUDIO BAN GAYA!")
except Exception as e:
    print(e)
