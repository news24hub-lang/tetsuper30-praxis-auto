import os, json, random, datetime, requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BLOG_ID = os.environ.get("BLOGGER_ID", "164780200466447812")
TOKEN_JSON = os.environ.get("BLOGGER_TOKEN", "")

# --- Question Bank (10+ Q per topic) ---
QBANK = {
    "English Vocab": [
        ("Synonym of 'Diligent'?", "A) Lazy B) Hardworking C) Slow D) Fast", "B", "Diligent means showing care and hard work. Hardworking is its direct synonym. Lazy is opposite."),
        ("Antonym of 'Generous'?", "A) Kind B) Stingy C) Brave D) Honest", "B", "Generous means big-hearted. Stingy means kanjoos, so it is antonym."),
        ("One word for 'One who loves books'?", "A) Bibliophile B) Philosopher C) Biographer D) Geologist", "A", "Biblio means books, Philia means love. So Bibliophile."),
        ("Idiom 'Break the ice' means?", "A) Break glass B) Start conversation C) Make cold D) Fight", "B", "Break the ice means to start a conversation in a social setting to make people comfortable."),
        ("Synonym of 'Abundant'?", "A) Scarce B) Plentiful C) Empty D) Less", "B", "Abundant means more than enough, plentiful is same."),
        ("Correct spelling?", "A) Accomodation B) Accommodation C) Acomodation D) Accomodasion", "B", "Correct spelling is Accommodation with double c and double m."),
        ("Antonym of 'Honest'?", "A) Truthful B) Dishonest C) Loyal D) Fair", "B", "Dishonest is direct opposite of Honest."),
        ("Meaning of 'Ephemeral'?", "A) Permanent B) Short-lived C) Strong D) Heavy", "B", "Ephemeral means lasting for a very short time."),
        ("Synonym of 'Brave'?", "A) Coward B) Courageous C) Fearful D) Weak", "B", "Courageous means brave."),
        ("One word for 'Fear of heights'?", "A) Hydrophobia B) Acrophobia C) Claustrophobia D) Xenophobia", "B", "Acro means height, phobia means fear."),
    ],
    "Praxis Math": [
        ("A train 150m long crosses a pole in 10 sec. Speed?", "A) 15 m/s B) 54 km/h C) Both D) None", "C", "Speed = Distance/Time = 150/10 = 15 m/s. 15*18/5 = 54 km/h. So both A and B correct."),
        ("If SP= 500, Profit=20%, CP=?", "A) 400 B) 416.66 C) 450 D) 500", "B", "CP = SP*100/(100+Profit%) = 500*100/120 = 416.66"),
        ("Average of 1 to 10?", "A) 5 B) 5.5 C) 6 D) 4.5", "B", "Sum 1 to 10 = 55, Average = 55/10 = 5.5"),
        ("Simple Interest: P=1000, R=10%, T=2 years?", "A) 100 B) 200 C) 300 D) 150", "B", "SI = P*R*T/100 = 1000*10*2/100 = 200"),
        ("What is 25% of 400?", "A) 25 B) 50 C) 100 D) 200", "C", "25% means 1/4th. 400/4 = 100."),
    ],
    "SBI Clerk Reasoning": [
        ("Puzzle - 5 persons sitting in row... Who is in middle?", "A) A B) B C) C D) Data insufficient", "D", "We need to apply left-right logic. Without full seating info, data is insufficient. This teaches you to not assume."),
        ("If A is B's brother, B is C's daughter, relation?", "A) Uncle B) Aunt C) Father D) Can't say", "A", "Use family tree diagram to solve blood relation quickly."),
    ]
}

def generate_quiz():
    today = datetime.date.today().strftime("%d %B %Y")
    topics = list(QBANK.keys())
    topic = random.choice(topics)

    selected_q = random.sample(QBANK[topic], k=min(10, len(QBANK[topic])))

    html = f"""
<h2>TET Super 30 - Daily Praxis Quiz - {today}</h2>
<p>Welcome to <b>My Basic Educator - TET Super 30 Daily Quiz</b>. Today topic is <b>{topic}</b>. This quiz is specially designed for <b>UPTET, CTET, Super TET, SBI Clerk, SSC</b> and other competitive exams. Practicing daily improves your speed and accuracy.</p>
<h3>Topic: {topic} - Why Important?</h3>
<p>{topic} is a scoring section in all teaching and banking exams. Regular practice of vocab, math and reasoning helps you crack the exam in first attempt. We provide detailed explanation for every question.</p>
<h3>Daily Quiz - 10 Questions with Detailed Explanation</h3>
"""
    for i, (q, opts, ans, exp) in enumerate(selected_q, 1):
        html += f"""
<h4>Q{i}. {q}</h4>
<p>{opts}</p>
<p><b>Correct Answer: {ans}</b></p>
<p><b>Detailed Explanation:</b> {exp} This type of question is frequently asked in TET and SBI exams. Remember the trick and concept.</p>
<hr/>
"""

    html += f"""
<h3>Final Tips for TET Super 30 Aspirants</h3>
<p>1. Practice this quiz daily at 5 AM.<br/>2. Note down new words and formulas.<br/>3. Revise previous day quiz.<br/>4. Focus on time management - 1 min per question.</p>
<h3>FAQs</h3>
<p><b>Q: Is this quiz free?</b><br/>Ans: Yes, 100% free daily on mybasiceducator.com</p>
<p><b>Q: How many questions daily?</b><br/>Ans: 10 fresh questions with explanation.</p>
<p>Practice daily at 5 AM! <br/>By <b>TET Super 30 Team - My Basic Educator</b></p>
"""
    return f"Daily Quiz {today} - {topic} - 10 Q with Explanation", html

def post_to_blogger(title, content):
    if not TOKEN_JSON:
        print("BLOGGER_TOKEN missing, skipping publish")
        return
    try:
        if TOKEN_JSON.strip().startswith("{"):
            info = json.loads(TOKEN_JSON)
            creds = Credentials.from_authorized_user_info(info, ["https://www.googleapis.com/auth/blogger"])
            service = build("blogger", "v3", credentials=creds)
            body = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": title, "content": content}
            post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
            print(f"Published: {post['url']}")
        else:
            url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
            headers = {"Authorization": f"Bearer {TOKEN_JSON.strip()}", "Content-Type": "application/json"}
            data = {"kind": "blogger#post", "title": title, "content": content}
            r = requests.post(url, headers=headers, json=data)
            print(r.text)
            print(f"Status: {r.status_code}")
    except Exception as e:
        print(f"Publish failed: {e}")

if __name__ == "__main__":
    title, html = generate_quiz()
    post_to_blogger(title, html)
    os.makedirs("posts", exist_ok=True)
    with open(f"posts/{datetime.date.today()}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Done")
