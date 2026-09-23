import os, requests, base64
import datetime as dt
from PIL import Image, ImageDraw

BLOG_ID=os.environ.get('BLOGGER_ID')
R_TOKEN=os.environ.get('BLOGGER_REFRESH_TOKEN')
C_ID=os.environ.get('CLIENT_ID')
C_SEC=os.environ.get('CLIENT_SECRET')

def get_token():
    d={"client_id":C_ID,"client_secret":C_SEC,"refresh_token":R_TOKEN,"grant_type":"refresh_token"}
    r=requests.post("https://oauth2.googleapis.com/token",data=d)
    r.raise_for_status()
    return r.json()['access_token']

def banner_b64(day):
    img=Image.new('RGB',(1280,720),color=(13,71,161))
    dr=ImageDraw.Draw(img)
    dr.rectangle([0,0,1280,140],fill=(255,193,7))
    dr.text((60,100),"TET SUPER 30",fill="white")
    dr.text((60,400),f"{day} Quiz",fill="white")
    dr.text((60,400),day,fill="white")
    img.save("b.png")
    f=open("b.png","rb")
    b="data:image/png;base64,"+base64.b64encode(f.read()).decode()
    f.close()
    return b

def do_post(tk):
    url=f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    h={"Authorization":f"Bearer {tk}","Content-Type":"application/json"}
    today=dt.date.today().strftime("%d %b %Y")
    b64=banner_b64(today)
    html=f'<img src="{b64}" style="width:100%;border-radius:12px"><h2>Daily Quiz {today}</h2>'
    # aapka baki html yaha rahega
    b={"kind":"blogger#post","blog":{"id":BLOG_ID},"title":f"Daily Quiz {today} | 10 Q&A","content":html}
    return requests.post(url,headers=h,json=b)

def run():
    print("Getting fresh access token...")
    tk=get_token()
    print("Token ok, posting...")
    r=do_post(tk)
    print(r.text)
    r.raise_for_status()
    print("POST SUCCESS")

run()
