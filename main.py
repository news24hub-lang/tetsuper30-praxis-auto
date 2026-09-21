import os, random, requests
import datetime as dt

BLOG_ID = os.environ.get('BLOGGER_ID')
TOKEN = os.environ.get('BLOGGER_TOKEN')
REFRESH_TOKEN = os.environ.get('BLOGGER_REFRESH_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

topics = ["Praxis Math", "English Vocab", "Reasoning", "GK", "CDP", "Hindi Grammar"]
today_topic = random.choice(topics)
today = dt.date.today().strftime("%d %b %Y")
safe_topic = today_topic.replace(" ", "-")

banner_top = f"https://dummyimage.com/800x400/0B5ed7/ffffff&text=TET+Super+30+Q+-+{safe_topic}"
study_img = "https://images.unsplash.com/photo-1523240795612-9a054b0d44a8?w=800&h=400&fit=crop"
mid_banner = "https://dummyimage.com/800x150/ff6a00/ffffff&text=Daily+10+Q+with+Explanation"

qb = [("Average of 1 to 10?", "5", "5.5", "6", "4.5", "B", "55/10=5.5"), ("SI P=1000 R=10% T=2?", "100", "200", "300", "400", "A", "SI=PRT/100")]

html = f"<div style='text-align:center;'><img src='{banner_top}' style='width:100%;border-radius:12px;'/></div><h2 style='color:#0B5ed7;'>Daily {today_topic} Quiz - {today}</h2><img src='{study_img}' style='width:100%;border-radius:10px;'/><br/><img src='{mid_banner}' style='width:100%;margin:10px 0;'/><hr/>"

for i,(q,a,b,c,d,ans,exp) in enumerate(qb,1):
    html += f"<p><b>Q{i}. {q}</b><br/>A) {a} B) {b} C) {c} D) {d}<br/><b>Ans: {ans}</b> - {exp}</p>"

html += "<hr/><p><b>TET Super 30 - Praxis Auto</b> | Daily Quiz</p>"

def get_new_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    r = requests.post(url, data=data)
    print("Refresh response:", r.text)
    r.raise_for_status()
    return r.json()["access_token"]

def post_blog():
    global TOKEN
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    
    def do_post(tok):
        headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
        data = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": f"Daily Quiz - {today_topic} - {today}", "content": html, "labels": [today_topic, "TET", "Daily Quiz"]}
        return requests.post(url, headers=headers, json=data)

    r = do_post(TOKEN)
    print(r.text)
    
    if r.status_code == 401:
        print("Token expired - getting new token via refresh...")
        TOKEN = get_new_token()
        r = do_post(TOKEN)
        print(r.text)

    r.raise_for_status()
    print("Posted:", r.json().get("url"))

post_blog()
