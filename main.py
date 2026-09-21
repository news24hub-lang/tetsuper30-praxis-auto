import os, json, random, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

BLOG_ID = os.environ['BLOG_ID']
KEY_JSON = json.loads(os.environ['GOOGLE_KEY_JSON'])

topics = ["Praxis Math", "English Vocab", "Reasoning", "GK", "CDP", "Hindi Grammar"]
today_topic = random.choice(topics)
today = datetime.date.today().strftime("%d %B %Y")

qb = [
    ("Average of 1 to 10?", "5", "5.5", "6", "4.5", "B", "Sum 1 to 10 = 55, Avg = 55/10 = 5.5"),
    ("Simple Interest: P=1000, R=10%, T=2 years?", "100", "200", "300", "150", "B", "SI = P*R*T/100 = 1000*10*2/100 = 200"),
    ("If SP=500, Profit=20%, CP=?", "400", "416.66", "450", "500", "B", "CP = SP*100/(100+Profit%) = 500*100/120 = 416.66"),
    ("What is 25% of 400?", "25", "50", "100", "200", "C", "25% means 1/4th. 400/4 = 100"),
    ("A train 150m long crosses a pole in 10 sec. Speed?", "15 m/s", "54 km/h", "Both", "None", "C", "Speed = 150/10=15 m/s = 54 km/h. So both A & B correct"),
    ("What is 12 x 12?", "144", "124", "134", "154", "A", "12*12 = 144 - basic square remember"),
    ("Find LCM of 4 and 6", "12", "6", "24", "8", "A", "LCM 4,6 = 12"),
    ("If 2x=10, x=?", "2", "5", "10", "20", "B", "x=10/2=5"),
    ("Area of square side 5cm?", "10", "20", "25", "15", "C", "Area = side^2 = 5*5=25 sq cm"),
    ("What is 50% of 200?", "50", "100", "150", "200", "B", "50% means half = 100"),
]

banner_top = f"https://dummyimage.com/800x400/0b5ed7/ffffff&text=TET+Super+30+-+{today_topic.replace(' ', '+')}"
study_img = "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800&h=400&fit=crop"
mid_banner = "https://dummyimage.com/800x150/ff6a00/ffffff&text=Daily+10+Q+With+Explanation"

html_content = f'''
<div style="text-align:center;">
<img src="{banner_top}" style="width:100%;max-width:800px;border-radius:12px;" />
</div>
<h2 style="color:#0b5ed7;text-align:center;">TET Super 30 - Daily Praxis Quiz - {today}</h2>
<p>Welcome to <b>My Basic Educator - TET Super 30 Daily Quiz</b>. Today topic is <b>{today_topic}</b>. This quiz is for <b>UPTET, CTET, Super TET, SBI Clerk, SSC</b>.</p>
<div style="text-align:center;margin:15px 0;">
<img src="{study_img}" style="width:100%;max-width:800px;border-radius:12px;" />
</div>
<h3>Topic: {today_topic} - Why Important?</h3>
<p>{today_topic} is scoring in all exams. Regular practice helps crack exam in first attempt.</p>
<div style="text-align:center;margin:15px 0;">
<img src="{mid_banner}" style="width:100%;max-width:800px;border-radius:8px;" />
</div>
<h3>Daily Quiz - 10 Questions with Detailed Explanation</h3>
'''

for i, (q, a,b,c,d, ans, exp) in enumerate(qb, 1):
    html_content += f'<p><b>Q{i}. {q}</b><br/>A) {a} B) {b} C) {c} D) {d}<br/><b>Correct Answer: {ans}</b></p><p><b>Detailed Explanation:</b> {exp}</p>'

html_content += '<h3>Final Tips</h3><ol><li>Practice daily at 5 AM.</li><li>Note down formulas.</li><li>Revise previous quiz.</li><li>1 min per question.</li></ol><p>By <b>TET Super 30 Team - My Basic Educator</b></p>'

def post_to_blogger():
    creds = service_account.Credentials.from_service_account_info(KEY_JSON, scopes=['https://www.googleapis.com/auth/blogger'])
    service = build('blogger', 'v3', credentials=creds)
    body = {"kind": "blogger#post", "title": f"Daily Quiz {today} - {today_topic} - 10 Q with Explanation", "content": html_content, "labels": [today_topic, "Daily Quiz"]}
    result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    print(f"Posted: {result.get('url')}")

if __name__ == "__main__":
    post_to_blogger()
