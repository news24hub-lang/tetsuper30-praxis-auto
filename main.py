import os, random, requests
import datetime as dt

BLOG_ID = os.environ.get('BLOGGER_ID')
TOKEN = os.environ.get('BLOGGER_TOKEN')
REFRESH = os.environ.get('BLOGGER_REFRESH_TOKEN')

topics = ["Praxis Math", "English Vocab", "Reasoning", "GK", "CDP", "Hindi Grammar"]
today_topic = random.choice(topics)
today = dt.date.today().strftime("%d %B %Y")
safe_topic = today_topic.replace(" ", "+")

banner_top = "https://dummyimage.com/800x400/0b5ed7/ffffff&text=TET+Super+30+-+" + safe_topic
study_img = "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800&h=400&fit=crop"
mid_banner = "https://dummyimage.com/800x150/ff6a00/ffffff&text=Daily+10+Q+With+Explanation"

qb = [("Average of 1 to 10?", "5", "5.5", "6", "4.5", "B", "55/10=5.5"),("SI P=1000 R=10% T=2?", "100", "200", "300", "150", "B", "200"),("25% of 400?", "25", "50", "100", "200", "C", "100"),("12 x 12?", "144", "124", "134", "154", "A", "144"),("LCM 4 and 6", "12", "6", "24", "8", "A", "12"),("If 2x=10 x=?", "2", "5", "10", "20", "B", "5"),("Area square side 5?", "10", "20", "25", "15", "C", "25"),("50% of 200?", "50", "100", "150", "200", "B", "100"),("Train 150m in 10s Speed?", "15 m/s", "54 km/h", "Both", "None", "C", "Both"),("SP=500 Profit=20% CP=?", "400", "416.66", "450", "500", "B", "416.66")]

html = f'<div style="text-align:center;"><img src="{banner_top}" style="width:100%;border-radius:12px;"/></div><h2 style="color:#0b5ed7;text-align:center;">TET Super 30 - {today}</h2><p>Today topic <b>{today_topic}</b> for UPTET CTET.</p><div style="text-align:center;"><img src="{study_img}" style="width:100%;border-radius:12px;"/></div><div style="text-align:center;margin:15px 0;"><img src="{mid_banner}" style="width:100%;border-radius:8px;"/></div>'

for i,(q,a,b,c,d,ans,exp) in enumerate(qb,1):
    html += f'<p><b>Q{i}. {q}</b><br/>A) {a} B) {b} C) {c} D) {d}<br/><b>Ans: {ans}</b> - {exp}</p>'

def post_blog():
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    data = {"kind": "blogger#post", "title": f"Daily Quiz {today} - {today_topic}", "content": html}
    r = requests.post(url, headers=headers, json=data)
    print(r.text)
    if r.status_code == 401 and REFRESH:
        print("Token expired - need new access token")
        # try refresh with google
        # user must regenerate BLOGGER_TOKEN from refresh token manually if fails
    r.raise_for_status()
    print("Posted:", r.json().get('url'))

post_blog()
