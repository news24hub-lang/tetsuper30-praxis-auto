import os, requests, base64
import datetime as dt
from PIL import Image, ImageDraw
BLOG_ID=os.environ.get('BLOGGER_ID')
TOKEN=os.environ.get('BLOGGER_TOKEN')
R_TOKEN=os.environ.get('BLOGGER_REFRESH_TOKEN')
C_ID=os.environ.get('CLIENT_ID')
C_SEC=os.environ.get('CLIENT_SECRET')
def get_token():
 d={"client_id":C_ID,"client_secret":C_SEC,"refresh_token":R_TOKEN,"grant_type":"refresh_token"}
 r=requests.post("https://oauth2.googleapis.com/token",data=d)
 r.raise_for_status()
 return r.json()["access_token"]
def banner_b64(day):
 img=Image.new('RGB',(1280,720),color=(13,71,161))
 dr=ImageDraw.Draw(img)
 dr.rectangle([0,0,1280,140],fill=(255,193,7))
 dr.text((60,200),"TET SUPER 30",fill="white")
 dr.text((60,300),"Praxis Quiz",fill="white")
 dr.text((60,400),day,fill="white")
 img.save("b.png")
 f=open("b.png","rb")
 b="data:image/png;base64,"+base64.b64encode(f.read()).decode()
 f.close()
 return b
today=dt.date.today().strftime("%d %b %Y")
b64=banner_b64(today)
html=f'<img src="{b64}" style="width:100%;border-radius:12px"/><h2>Daily Quiz {today}</h2>'
qs=[("Avg 1-10?","5.5","55/10"),("SI 1000 10% 2y?","200","P*R*T/100"),("SP500 P20% CP?","416","*100/120"),("25% of 400?","100","/4"),("150m 10s Speed?","15","150/10"),("HCF 12 18?","6","6"),("x+1/x=2 x?","1","1"),("Tri b10 h6?","30","0.5*b*h"),("2,4,8,16,?","32","*2"),("CP400 SP500 P%?","25%","25%")]
for i,(q,a,e) in enumerate(qs,1):
 html+=f'<div style="border:1px solid #ddd;padding:10px;margin:8px 0;border-radius:8px"><h3>Q{i}. {q}</h3><p><b>{a}</b> - {e}</p></div>'
def do_post(tk):
 url=f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
 h={"Authorization":f"Bearer {tk}","Content-Type":"application/json"}
 b={"kind":"blogger#post","blog":{"id":BLOG_ID},"title":f"Daily Quiz {today} | 10 Q&A","content":html}
 return requests.post(url,headers=h,json=b)
def run():
 r=do_post(TOKEN)
 if r.status_code==401:
  r=do_post(get_token())
 print(r.text)
 r.raise_for_status()
run()
