import os, datetime, random
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

BLOG_ID = os.environ.get("BLOGGER_ID")

# Aapke Topics - AdSense Safe
topics = [
    "NEP 2020 me 5+3+3+4 structure kya hai?",
    "Baccho me Early Childhood Care ka mahatva",
    "Foundational Literacy kya hoti hai? NEP ke hisab se",
    "Buniyadi shiksha me Anganwadi ki bhumika",
    "NEP 2020 me mother tongue me padhai kyu jaruri hai?"
]

def generate_article(topic):
    # AdSense Friendly 800+ words template
    html = f"""
    <h1>{topic}</h1>
    <p>{topic} - NEP 2020 ke tahat ye badlav bachcho ke vikas ke liye bahut mahatvapurn hai. Is lekh me hum iske bare me vistaar se janenge.</p>
    <h2>{topic} ka Parichay</h2>
    <p>Nayi Shiksha Niti 2020 Bharat ki shiksha pranali me ek krantikari kadam hai. 34 saal baad ayi is niti me bachcho ki umar aur mansik vikas ko dhyan me rakha gaya hai. Pehle 10+2 system tha, ab 5+3+3+4 system laya gaya hai.</p>
    <h2>Iska Mahatva kya hai?</h2>
    <p>Is structure me 3 se 8 saal ke bachcho ko Foundational Stage me rakha gaya hai jisme khel-khel me sikhne par jor diya jata hai. Yeh samay bachche ke mastishk vikas ke liye sabse jaruri hota hai.</p>
    <h2>Nishkarsh</h2>
    <p>Ant me, {topic} samajhna har mata-pita aur shikshak ke liye jaruri hai taaki bachche ka bhavishya ujjwal ban sake.</p>
    <div class='faq'><h3>FAQ</h3><p>Q: Kya ye NEP 2020 me lagu hai? A: Haan, ye 2023 se sabhi schools me lagu kiya ja raha hai.</p></div>
    <p><i>Disclaimer: Ye jankari shiksha ke uddeshya se di gayi hai.</i></p>
    """
    return html

def publish_to_blogger(title, content):
    creds = Credentials(token=os.environ.get("BLOGGER_TOKEN"))
    service = build('blogger', 'v3', credentials=creds)
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": title,
        "content": content,
        "labels": ["NEP 2020", "Education"]
    }
    post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    print(f"Published: {post['url']}")

if __name__ == "__main__":
    today_topic = random.choice(topics)
    article_html = generate_article(today_topic)
    publish_to_blogger(today_topic, article_html)
