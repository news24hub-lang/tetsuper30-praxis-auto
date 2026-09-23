import os, datetime as dt, requests, base64, random
from PIL import Image, ImageDraw

BLOG_ID = os.environ.get('BLOGGER_ID')
TOKEN = os.environ.get('BLOGGER_TOKEN')
REFRESH_TOKEN = os.environ.get('BLOGGER_REFRESH_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

def get_new_token():
    url = "https://oauth2.googleapis.com/token"
    data = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "refresh_token": REFRESH_TOKEN, "grant_type": "refresh_token"}
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]

def create_banner_base64(date_str):
    try:
        img = Image.new('RGB', (1280, 720), color=(13, 71, 161))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0,0,1280,140], fill=(255,193,7))
        # Simple text without font file
        draw.text((60, 200), "TET SUPER 30", fill="white", font_size=80)
        draw.text((60, 320), "Praxis Math Quiz", fill=(255,241,118), font_size=60)
        draw.text((60, 420), date_str, fill="white", font_size=50)
        img.save("banner.png")
        with open("banner.png", "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    except:
        return "https://via.placeholder.com/1280x720/0d47a1/ffffff?text=TET+SUPER+30"

qb = [
    ("Average of 1 to 10?", "4.5", "5", "5.5", "6", "5.5", "Sum 55/10=5.5 Trick (n+1)/2"),
    ("SI P=1000 R=10% T=2yr?", "100", "200", "300", "150", "200", "SI=P*R*T/100=200"),
    ("SP=500 Profit 20% CP=?", "400", "416.66", "450", "500", "416.66", "CP=SP*100/120=416.66"),
    ("25% of 400?", "25", "50", "100", "200", "100", "1/4 of 400=100"),
    ("150m pole in 10sec Speed?", "10 m/s", "15 m/s", "54 km/h", "Both B & C", "Both B & C", "Speed=150/10=15m/s=54km/h"),
    ("HCF of 12 and 18?", "6", "12", "18", "3", "6", "Common factors max is 6"),
    ("If x+1/x=2 then x=?", "1", "2", "0", "-1", "1", "1+1=2"),
    ("Area triangle b10 h6?", "30", "60", "15", "20", "30", "Area=1/2*b*h=30"),
    ("Series 2,4,8,16,?", "24", "32", "30", "28", "32", "Double pattern 16*2=32"),
    ("CP400 SP500 Profit%?", "20%", "25%", "30%", "15%", "25%", "Profit 100/400*100=25%"),
]

today = dt.date.today().strftime("%d %b %Y")
banner_b64 = create_banner_base64(today)
html = f'<div style="text-align:center"><img src="{banner_b64}" style="width:100%;border-radius:12px;"/></div><h2>TET Super 30 - Daily Praxis Quiz - {today}</h2><p>Welcome to My Basic Educator. Daily 10 Praxis Math questions for UPTET, CTET, SBI. Detailed explanation with tricks.</p>'

for i,(q,a,b,c,d,ans,exp) in enumerate(qb,1):
    html += f'<div style="border:1px solid #ddd;padding:15px;margin:12px 0;border-radius:10px;"><h3>Q{i}. {q}</h3><p>(a) {a} (b) {b} (c) {c} (d) {d}</p><p style="background:#e3f2fd;padding:8px;"><b>Ans: {ans}</b></p><p><b>Exp:</b> {exp}. This type asked in TET 2022, 2023.</p></div>'

html += '<h2>Tips</h2><ol><li>Daily 5 AM practice</li><li>Note tricks</li><li>Revise</li><li>1 min per Q target</li></ol><h2>FAQs</h2><p><b>Q: Free?</b> Yes daily on blog.</p><p><b>Q: For SBI?</b> Yes same pattern.</p><p><b>Practice daily!</b></p>'

def do_post(tok):
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    data = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": f"Daily Quiz - {today} | 10 Q&A Praxis Math", "content": html, "labels": ["TET Super 30","Praxis Math"]}
    return requests.post(url, headers=headers, json=data)

def post_blog():
    r = do_post(TOKEN)
    print(r.text)
    if r.status_code == 401:
        print("Token expired - getting new token")
        new_tok = get_new_token()
        r = do_post(new_tok)
        print(r.text)
    r.raise_for_status()
    print("Posted:", r.json().get("url"))

post_blog()
