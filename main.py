import os, requests, base64, random
import datetime as dt
from PIL import Image, ImageDraw, ImageFont

BLOG_ID=os.environ.get('BLOGGER_ID')
R_TOKEN=os.environ.get('BLOGGER_REFRESH_TOKEN')
C_ID=os.environ.get('CLIENT_ID')
C_SEC=os.environ.get('CLIENT_SECRET')

def get_token():
    d={"client_id":C_ID,"client_secret":C_SEC,"refresh_token":R_TOKEN,"grant_type":"refresh_token"}
    r=requests.post("https://oauth2.googleapis.com/token",data=d,timeout=30)
    r.raise_for_status()
    return r.json()['access_token']

def banner_b64(title_date):
    # Simple attractive banner
    W,H=1280,720
    img=Image.new('RGB',(W,H),color=(11, 37, 105))
    dr=ImageDraw.Draw(img)
    # yellow top bar
    dr.rectangle([0,0,W,160],fill=(255,193,7))
    try:
        # try load default font bigger
        f1=ImageFont.truetype("DejaVuSans-Bold.ttf",70)
        f2=ImageFont.truetype("DejaVuSans.ttf",48)
    except:
        f1=ImageFont.load_default()
        f2=ImageFont.load_default()
    dr.text((60,30),"TET SUPER 30",font=f1,fill=(0,0,0))
    dr.text((60,280),f"Daily Quiz - {title_date}",font=f1,fill=(255,255,255))
    dr.text((60,400),"10 Important Q&A | TET Special",font=f2,fill=(255,235,150))
    img.save("/tmp/b.png")
    with open("/tmp/b.png","rb") as f:
        b64="data:image/png;base64,"+base64.b64encode(f.read()).decode()
    return b64

# Sample Quiz Data - aap chahe to isko badha sakte ho
QUIZ_BANK=[
    ["Child Development me 'Zone of Proximal Development' kisne diya?","Vygotsky","Piaget","Skinner","Vygotsky","ZPD Vygotsky ne diya tha - bachcha guidance me zyada seekhta hai."],
    ["NEP 2020 ke anusar 5+3+3+4 structure me Foundational stage kitna hai?","5 Years","3 Years","4 Years","5 Years","5 saal (3-8 age) Foundational Stage hai."],
    ["'Learning by Doing' ka siddhant kisne diya?","John Dewey","Froebel","Montessori","John Dewey","Dewey ne practical learning par jor diya."],
    ["Bloom's Taxonomy me sabse upar ka level kaunsa hai?","Create","Evaluate","Analyze","Create","Revised Bloom me Create sabse upar hai."],
    ["RTE Act kab lagu hua?","2009","2005","2010","2009","RTE 2009 me pass, 2010 se lagu."],
    ["Sanskrit me 'Shiksha' ka arth hai?","Seekhna","Sikhana","Dono","Dono","Shiksha seekhne-sikhane dono ko kehti hai."],
    ["Kothari Commission ka varsh?","1964-66","1986","1968","1964-66","1964-66 me Kothari Commission aaya tha."],
    ["Multiple Intelligence Theory kisne di?","Gardner","Spearman","Thurstone","Gardner","Howard Gardner ne 8 intelligence batayi."],
    ["TET ka full form?","Teacher Eligibility Test","Teacher Entrance Test","Teaching Efficiency Test","Teacher Eligibility Test","Teacher banne ke liye TET zaruri hai."],
    ["Operant Conditioning kiska hai?","Skinner","Pavlov","Thorndike","Skinner","Skinner ne reinforcement ka concept diya."],
]

def make_html(today_str, b64):
    random.shuffle(QUIZ_BANK)
    selected=QUIZ_BANK[:10]
    
    html=f"""
    <div style="font-family:Arial,sans-serif;max-width:800px;margin:auto">
    <img src="{b64}" style="width:100%;border-radius:16px;margin-bottom:20px" />
    <h1 style="color:#0b2569">Daily TET Quiz - {today_str} | 10 Q&A</h1>
    <p style="background:#fff3cd;padding:12px;border-radius:8px">Rozana 10 Important Questions jo TET / CTET / SuperTET me pooche jate hain. Answer ke sath explanation bhi diya hai.</p>
    """
    for i,(q,o1,o2,o3,ans,exp) in enumerate(selected,1):
        html+=f"""
        <div style="border:1px solid #ddd;border-radius:12px;padding:16px;margin:16px 0">
        <h3 style="margin:0 0 10px 0">Q{i}. {q}</h3>
        <p>A) {o1}<br>B) {o2}<br>C) {o3}</p>
        <details style="background:#e8f5e9;padding:10px;border-radius:8px"><summary style="cursor:pointer;font-weight:bold;color:#2e7d32">✅ Answer Dekhein</summary>
        <p><b>Answer: {ans}</b><br>{exp}</p></details>
        </div>
        """
    html+=f"""
    <div style="background:#0b2569;color:white;padding:20px;border-radius:12px;text-align:center;margin-top:20px">
    <h2>TET SUPER 30 - Daily Practice</h2><p>Kal fir milenge naye 10 sawalon ke sath! Share zarur karein.</p>
    </div></div>
    """
    return html

def do_post(tk):
    url=f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    h={"Authorization":f"Bearer {tk}","Content-Type":"application/json"}
    today=dt.date.today().strftime("%d %b %Y")
    b64=banner_b64(today)
    html=make_html(today,b64)
    body={"kind":"blogger#post","blog":{"id":BLOG_ID},"title":f"Daily Quiz {today} | 10 Q&A | TET Super 30","content":html,"labels":["TET Quiz","Daily Quiz"]}
    r=requests.post(url,headers=h,json=body,timeout=60)
    print("BLOGGER RESPONSE:",r.text[:1000])
    r.raise_for_status()
    return r

def run():
    print("Getting fresh token...")
    tk=get_token()
    print("Posting...")
    do_post(tk)
    print("SUCCESS")

run()
