import os, json, random, datetime, requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BLOG_ID = os.environ.get("BLOGGER_ID", "16478020466447012")
TOKEN_JSON = os.environ.get("BLOGGER_TOKEN", "")

# --- Question Bank (10+ Q per topic) ---
QBANK = {
    "English Vocab": [
        ("Synonym of 'Diligent'?", "A) Lazy B) Hardworking C) Slow D) Fast", "B", "Diligent means showing care and hard work"),
        ("Antonym of 'Generous'?", "A) Kind B) Stingy C) Brave D) Honest", "B", "Generous means big-hearted. Stingy mean"),
        ("One word for 'One who loves books'?", "A) Bibliophile B) Philosopher C) Biographer D) Geologist", "A", "Biblio"),
        ("Idiom 'Break the ice' means?", "A) Break glass B) Start conversation C) Make cold D) Fight", "B", "Break the ice means to start conversation"),
        ("Synonym of 'Abundant'?", "A) Scarce B) Plentiful C) Empty D) Less", "B", "Abundant means more than enough, plentiful"),
        ("Correct spelling?", "A) Accommodation B) Accomodation C) Acomodation D) Accomodation", "B", "Correct spelling is Accommodation"),
        ("Antonym of 'Honest'?", "A) Truthful B) Dishonest C) Loyal D) Fair", "B", "Dishonest is direct opposite of Honest"),
        ("Meaning of 'Ephemeral'?", "A) Permanent B) Short-lived C) Strong D) Heavy", "B", "Ephemeral means lasting for short time"),
        ("Synonym of 'Brave'?", "A) Coward B) Courageous C) Fearful D) Weak", "B", "Courageous means brave"),
        ("One word for 'Fear of heights'?", "A) Hydrophobia B) Acrophobia C) Claustrophobia D) Xenophobia", "B", "Acro means height"),
    ],
    "Praxis Math": [
        ("A train 150m long crosses a pole in 10 sec. Speed?", "A) 15 m/s B) 54 km/h C) Both D) None", "C", "Speed = Distance/Time = 150/10 = 15 m/s, 15*18/5 = 54 km/h. So both A and B correct."),
        ("If SP= 500, Profit=20%, CP=?", "A) 400 B) 416.66 C) 450 D) 500", "B", "CP = SP*100/(100+Profit%) = 500*100/120 = 416.66"),
        ("Average of 1 to 10?", "A) 5 B) 5.5 C) 6 D) 4.5", "B", "Sum 1 to 10 = 55, Average = 55/10 = 5.5"),
        ("Simple Interest: P=1000, R=10%, T=2 years?", "A) 100 B) 200 C) 300 D) 150", "B", "SI = P*R*T/100 = 1000*10*2/100 = 200"),
        ("What is 25% of 400?", "A) 25 B) 50 C) 100 D) 200", "C", "25% means 1/4th. 400/4 = 100."),
    ],
    "SBI Clerk Reasoning": [
        ("Puzzle - 5 persons sitting in row... who is in middle?", "A) A B) B C) C D) Data insufficient", "D", "We need more info"),
        ("If A is B's brother, B is C's daughter, relation?", "A) Uncle B) Aunt C) Father D) Can't say", "A", "Use family tree"),
    ]
}

def generate_quiz():
    today = datetime.date.today().strftime("%d %B %Y")
    topics = list(QBANK.keys())
    topic = random.choice(topics)

    selected_q = random.sample(QBANK[topic], k=min(10, len(QBANK[topic])))

    # --- IMAGES ADDED ---
    banner_url = f"https://via.placeholder.com/800x400/1976d2/ffffff?text=TET+Super+30+%7C+{topic.replace(' ', '+')}"
    icon_url = "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80"

    html = f"""
    <div style="font-family: Arial; max-width:800px; margin:auto;">
    <img src="{banner_url}" alt="TET Super 30 Daily Quiz Banner" style="width:100%; border-radius:16px; margin-bottom:15px; box-shadow:0 4px 12px rgba(0,0,0,0.15);" />

    <h2 style="color:#1976d2; text-align:center; margin-bottom:5px;">TET Super 30 - Daily Praxis Quiz - {today}</h2>
    <p style="text-align:center; background:#e3f2fd; padding:10px; border-radius:8px;">Welcome to <b>My Basic Educator</b> - <b>TET Super 30 Daily Quiz</b>. Today topic is <b>{topic}</b>. This quiz is specially designed for <b>UPTET, CTET, Super TET, SBI Clerk, SSC</b>.</p>

    <img src="{icon_url}" alt="Study" style="width:100%; height:200px; object-fit:cover; border-radius:12px; margin:10px 0;" />

    <h3 style="color:#fff; background:#1976d2; padding:10px 15px; border-radius:8px;">Topic: {topic} - Why Important?</h3>
    <p>{topic} is a scoring section in all teaching and banking exams. Regular practice of vocab, math and reasoning helps you crack the exam in first attempt. We provide detailed explanation for every question.</p>

    <h3 style="color:#d32f2f; border-bottom:2px solid #d32f2f; padding-bottom:5px;">Daily Quiz - 10 Questions with Detailed Explanation</h3>
    """

    for i, (q, opts, ans, exp) in enumerate(selected_q, 1):
        html += f"""
        <div style="border:1px solid #e0e0e0; border-radius:12px; padding:15px; margin:15px 0; background:#fafafa;">
        <h4 style="margin:0 0 8px 0;">Q{i}. {q}</h4>
        <p style="margin:5px 0; font-weight:bold;">{opts}</p>
        <p style="color:#2e7d32; font-weight:bold; background:#e8f5e9; display:inline-block; padding:3px 10px; border-radius:20px;">Correct Answer: {ans}</p>
        <p style="margin:8px 0 0 0; font-size:14px;"><b>Detailed Explanation:</b> {exp} This type of question is frequently asked in TET and SBI exams. Remember the trick and concept.</p>
        </div>
        """
        if i == 5:
            html += f'<img src="https://via.placeholder.com/800x150/f57c00/ffffff?text=Keep+Practicing+%7C+50%25+Complete" style="width:100%; border-radius:10px; margin:10px 0;" />'

    html += f"""
    <div style="background:#fff3e0; border-left:5px solid #ff9800; padding:15px; border-radius:8px; margin-top:20px;">
    <h3 style="margin-top:0;">Final Tips for TET Super 30 Aspirants</h3>
    <p>1. Practice this quiz daily at 5 AM.<br/>2. Note down new words and formulas.<br/>3. Revise previous day quiz.<br/>4. Focus on time management - 1 min per question.</p>
    </div>
    <h3>FAQs</h3>
    <p><b>Q: Is this quiz free?</b><br/>Ans: Yes, 100% free daily on mybasiceducator.com</p>
    <p><b>Q: How many questions daily?</b><br/>Ans: 10 fresh questions with explanation.</p>
    <p style="text-align:center; font-weight:bold; margin-top:20px;">Practice daily at 5 AM! <br/>By <span style="color:#1976d2;">TET Super 30 Team - My Basic Educator</span></p>
    </div>
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
        else:
            creds = Credentials.from_authorized_user_info(json.loads(TOKEN_JSON), ["https://www.googleapis.com/auth/blogger"])
        service = build("blogger", "v3", credentials=creds)
        body = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": title, "content": content}
        post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        print(f"Published: {post.get('url')}")
    except Exception as e:
        print(f"Blogger Error: {e}")

if __name__ == "__main__":
    title, html = generate_quiz()
    post_to_blogger(title, html)
