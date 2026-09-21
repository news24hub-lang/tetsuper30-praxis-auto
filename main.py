import os, json, random
from datetime import datetime
from gtts import gTTS

# AdSense Friendly Database - Har topic ka detail
QUIZ_TOPICS = [
  {
    "q": "UP Basic Education ka MDM full form kya hai?",
    "a": "Mid Day Meal, ab PM POSHAN",
    "topic": "UP Basic",
    "detail": "Mid Day Meal (MDM) yojana Bharat ki sabse badi school bhojan yojana hai. Iski shuruat 15 August 1995 ko hui thi. 2021 me iska naam badal kar PM POSHAN (Pradhan Mantri Poshan Shakti Nirman) kar diya gaya. Iska mukhya uddeshya bachchon ki poshan sthiti sudharna, enrollment badhana aur school me attendance badhana hai. UP Basic Shiksha Parishad me ye yojana Class 1 se 8 tak lagu hai. Is yojana ka sanchalan Ministry of Education dwara kiya jata hai."
  },
  {
    "q": "Child Development me Piaget ke kitne stages hote hain?",
    "a": "4 stages - Sensorimotor, Preoperational, Concrete Operational, Formal Operational",
    "topic": "CDP",
    "detail": "Jean Piaget ne bachchon ke mansik vikas ke 4 stages bataye. 1) Sensorimotor (0-2 years) - bachcha indriyon se seekhta hai. 2) Preoperational (2-7 years) - kalpanik soch viksit hoti hai. 3) Concrete Operational (7-11 years) - tarkik soch aati hai. 4) Formal Operational (11+ years) - abstract soch viksit hoti hai. CTET, UPTET aur Super TET me is topic se har saal 2-3 prashn aate hain."
  },
  {
    "q": "NEP 2020 me 5+3+3+4 structure kya hai?",
    "a": "NEP 2020 ka naya school structure",
    "topic": "NEP 2020",
    "detail": "National Education Policy 2020 ne 10+2 system ko khatam karke 5+3+3+4 ka naya structure diya hai. 5 saal ka Foundational Stage (3 saal Anganwadi + 2 saal Class 1-2), 3 saal ka Preparatory Stage (Class 3-5), 3 saal ka Middle Stage (Class 6-8) aur 4 saal ka Secondary Stage (Class 9-12). Iska focus rote learning se hatkar conceptual aur skill-based learning par hai."
  },
  {
    "q": "Praxis exam kis country me teacher banne ke liye hota hai?",
    "a": "USA me teacher certification ke liye",
    "topic": "Praxis 5205",
    "detail": "Praxis Exam USA me teacher certification ke liye liya jata hai. ETS (Educational Testing Service) is exam ko conduct karti hai. Praxis 5001, 5205 jaise alag-alag codes hote hain jo alag subjects ke liye hote hain. Isme teaching skills aur subject knowledge dono check kiya jata hai."
  }
]

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    quiz = random.choice(QUIZ_TOPICS)

    os.makedirs("audio", exist_ok=True)
    os.makedirs("blogger/MyBasicEducator", exist_ok=True)

    # AUDIO - Shorts ke liye short hi rahega
    tts = gTTS(text=f"Today's Quiz. {quiz['q']}. Answer is {quiz['a']}.", lang='hi', slow=False)
    tts.save(f"audio/{today}.mp3")

    # BLOGGER HTML - 100% AdSense Friendly
    html = f"""
<article>
<h1>{quiz['q']} - Full Details & Explanation in Hindi</h1>
<p><em>Published: {today} | My Basic Educator | {quiz['topic']} Preparation</em></p>

<p>UP TET, Super TET, CTET aur Praxis 5205 ki taiyari kar rahe abhyarthiyon ke liye aaj ka sabse important question hai: <strong>{quiz['q']}</strong>. Is post me hum iska sahi jawab, detail explanation aur exam trick cover karenge.</p>

<h2>{quiz['q']} - Sahi Jawab</h2>
<p><strong>Correct Answer: {quiz['a']}</strong></p>
<p>{quiz['detail']}</p>

<h2>Exam Point of View Se Important Facts</h2>
<p>{quiz['topic']} category ka ye sawal pichhle 5 saal me kai baar poocha gaya hai. Agar aap UP Assistant Teacher Bharti 2026 ki taiyari kar rahe hain, to aapko is topic ke theoretical aur practical dono aspects samajhne honge. School management aur bachchon ke vikas se jude is tarah ke prashn exam me aapko extra marks dila sakte hain.</p>
<p>Is topic ko yaad rakhne ke liye roz revision karna bahut zaroori hai. Hamara daily quiz isi liye banaya gaya hai taaki aapka concept clear rahe.</p>

<h2>Yaad Karne Ki Best Trick</h2>
<p>{quiz['q']} ko yaad rakhne ke liye {quiz['a']} ko short notes me likh lein. Mnemonics ya kahani bana kar yaad karne se ye lambe samay tak yaad rehta hai. Daily 1 quiz solve karne se aapki accuracy 90% tak badh sakti hai.</p>

<h2>FAQs</h2>
<h3>Q1. {quiz['q']}</h3>
<p>Ans: {quiz['a']} - {quiz['detail'][:150]}...</p>

<h3>Q2. Kya ye topic Super TET 2026 ke liye important hai?</h3>
<p>Ans: Haan, {quiz['topic']} se jude prashn Super TET aur CTET dono me har saal pooche jate hain.</p>

<h3>Q3. Is topic ki taiyari kaise karein?</h3>
<p>Ans: NCERT, UP Basic Shiksha ki books aur My Basic Educator ke daily updates se taiyari karein.</p>

<hr>
<p><strong>Disclaimer:</strong> Ye jankari shiksha uddeshya ke liye di gayi hai. Kisi bhi sarkari yojana ya exam pattern ki antim pushti ke liye official website dekhein. My Basic Educator ka kisi sarkari sanstha se koi sambandh nahi hai.</p>
</article>
"""

    with open(f"blogger/MyBasicEducator/{today}.html", "w", encoding="utf-8") as f:
        f.write(html)

    data = {
        "date": today,
        "title": f"{quiz['q']}",
        "answer": quiz['a'],
        "blog_file": f"blogger/MyBasicEducator/{today}.html"
    }
    with open(f"audio/{today}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"AdSense Friendly Done: {quiz['q']}")

if __name__ == "__main__":
    main()
