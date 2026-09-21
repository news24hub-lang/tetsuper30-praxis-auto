import os, json, random, datetime, requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BLOG_ID = os.environ.get("BLOGGER_ID", "1647802080466447812")
TOKEN_JSON = os.environ.get("BLOGGER_TOKEN", "")

def generate_quiz():
    today = datetime.date.today().strftime("%d %B %Y")
    topics = ["SBI Clerk Reasoning", "Praxis Math", "English Vocab", "GA"]
    topic = random.choice(topics)
    html = f"""
    <h2>TET Super 30 - Daily Praxis Quiz - {today}</h2>
    <p><b>Topic:</b> {topic}</p>
    <h3>Q1. A train 150m long crosses a pole in 10 sec. Speed?</h3>
    <p>A) 15 m/s B) 54 km/h C) Both D) None - <b>Ans: C</b></p>
    <h3>Q2. Synonym of 'Diligent'?</h3>
    <p>A) Lazy B) Hardworking C) Slow D) Fast - <b>Ans: B</b></p>
    <h3>Q3. Puzzle - 5 persons... </h3>
    <p>Practice daily at 5 AM!</p>
    <p>By TET Super 30</p>
    """
    return f"Daily Quiz {today} - {topic}", html

def post_to_blogger(title, content):
    if not TOKEN_JSON:
        print("BLOGGER_TOKEN missing, skipping publish")
        return
    try:
        # Token can be JSON string or direct access_token
        if TOKEN_JSON.strip().startswith("{"):
            info = json.loads(TOKEN_JSON)
            creds = Credentials.from_authorized_user_info(info, ["https://www.googleapis.com/auth/blogger"])
            service = build("blogger", "v3", credentials=creds)
            body = {"kind": "blogger#post", "blog": {"id": BLOG_ID}, "title": title, "content": content}
            post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
            print(f"Published: {post['url']}")
        else:
            # Direct access token
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
    # also save local
    os.makedirs("posts", exist_ok=True)
    with open(f"posts/{datetime.date.today()}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Done")
