import os
import requests
import base64
import datetime as dt
from PIL import Image, ImageDraw

BLOG_ID = os.environ.get('BLOGGER_ID')
TOKEN = os.environ.get('BLOGGER_TOKEN')
R_TOKEN = os.environ.get('BLOGGER_REFRESH_TOKEN')
C_ID = os.environ.get('CLIENT_ID')
C_SEC = os.environ.get('CLIENT_SECRET')

def get_token():
    data = {
        "client_id": C_ID,
        "client_secret": C_SEC,
        "refresh_token": R_TOKEN,
        "grant_type": "refresh_token"
    }
    r = requests.post("https://oauth2.googleapis.com/token", data=data)
    r.raise_for_status()
    return r.json()["access_token"]

def banner_b64(day):
    img = Image.new('RGB', (1280, 720), color=(13, 71, 161))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1280, 140], fill=(255, 193, 7))
    draw.text((60, 200), "TET SUPER 30", fill="white")
    draw.text((60, 300), "Praxis Math Quiz", fill="white")
    draw.text((60, 400), day, fill="white")
    img.save("b.png")
    with open("b.png", "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return "data:image/png;base64," + b64

qb = [
    ("Average of 1 to 10?", "5.5", "Sum 55/10=5.5"),
    ("SI P=1000 R=10% T=2yr?", "200", "P*R*T/100=200"),
    ("SP=500 Profit 20% CP?", "416", "SP*100/120=416"),
    ("25% of 400?", "100", "400/4=100"),
    ("150m in 10s Speed?", "15 m/s", "150/10=15"),
    ("HCF of 12 and 18?", "6", "Max common is 6"),
    ("If x+1/x=2 then x=?", "1", "1+1=2"),
    ("Triangle b=10 h=6 Area?", "30", "0.5*b*h=30"),
    ("2,4,8,16,?", "32", "Pattern *2"),
    ("CP400 SP500 Profit%?", "25%", "100/400*100=25%")
]

today = dt.date.today().strftime("%d %b %Y")
b64 = banner_b64(today)

html = f'<img src="{b64}" style="width:100%;border-radius:12px"/>'
html += f'<h2>Daily Quiz {today} - 10 Q&A for TET SBI SSC</h2>'
html += '<p>Welcome to My Basic Educator. Daily 10 Praxis Math questions with tricks for UPTET, CTET, SBI, SSC. Practice daily 5 AM.</p>'

for i, (q, a, e) in enumerate(qb, 1):
    html += f'<div style="border:1px solid #ddd;padding:12px;margin:10px 0;border-radius:8px"><h3>Q{i}. {q}</h3><p><b>Ans: {a}</b></p><p>Exp: {e}</p></div>'

html += '<h3>Tips</h3><p>1. Daily 5 AM practice 2. Note tricks 3. 1 min per Q</p><h3>FAQs</h3><p>Q: Free? Yes daily on blog. Q: For SBI? Yes same pattern.</p>'

def do_post(tk):
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {"Authorization": f"Bearer {tk}", "Content-Type": "application/json"}
    body = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": f"Daily Quiz {today} | 10 Q&A Praxis Math", "content": html}
    return requests.post(url, headers=headers, json=body)

def run():
    r = do_post(TOKEN)
    if r.status_code == 401:
        r = do_post(get_token())
    print(r.text)
    r.raise_for_status()
    print("POSTED SUCCESS")

run()
