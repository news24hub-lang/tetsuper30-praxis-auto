import os, requests, random
import datetime as dt

BLOG_ID=os.environ.get('BLOGGER_ID')
R_TOKEN=os.environ.get('BLOGGER_REFRESH_TOKEN')
C_ID=os.environ.get('CLIENT_ID')
C_SEC=os.environ.get('CLIENT_SECRET')

def get_token():
    d={"client_id":C_ID,"client_secret":C_SEC,"refresh_token":R_TOKEN,"grant_type":"refresh_token"}
    r=requests.post("https://oauth2.googleapis.com/token",data=d,timeout=30)
    r.raise_for_status()
    return r.json()["access_token"]

def make_banner_html(today_str):
    return f"""
    <div style="background:linear-gradient(135deg,#0b2569 0%,#1e40af 100%);border-radius:20px;padding:35px 20px;color:white;text-align:center;margin-bottom:25px;border:5px solid #facc15">
      <div style="background:#facc15;color:black;display:inline-block;padding:7px 20px;border-radius:20px;font-weight:bold;font-size:15px;margin-bottom:15px">TET SUPER 30</div>
      <h1 style="margin:10px 0;font-size:32px;color:white;line-height:1.2">Daily Quiz - {today_str}</h1>
      <p style="font-size:18px;color:#fde68a;margin:0">10 महत्वपूर्ण प्रश्न | CTET / SuperTET स्पेशल</p>
    </div>
    """

# PURE HINDI QUIZ BANK
QUIZ_BANK=[
["ब्लूम टैक्सोनॉमी में सबसे उच्च स्तर कौन सा है?","सृजन करना","मूल्यांकन करना","विश्लेषण करना","सृजन करना","ब्लूम के अनुसार सबसे ऊपर सृजन (Create) होता है।"],
["शिक्षा का अधिकार अधिनियम (RTE) कब लागू हुआ था?","2009","2010","2005","2010 में लागू हुआ","RTE 2009 में बना पर 1 अप्रैल 2010 से लागू हुआ।"],
["संस्कृत में 'शिक्षा' का क्या अर्थ है?","सीखना","सिखाना","सीखना-सिखाना दोनों","सीखना-सिखाना दोनों","शिक्षा शब्द शिक्ष् धातु से बना है जिसका अर्थ दोनों है।"],
["NEP 2020 के अनुसार 5+3+3+4 में फाउंडेशनल स्टेज कितने वर्ष का है?","5 वर्ष","3 वर्ष","4 वर्ष","5 वर्ष","3 साल आंगनवाड़ी + 2 साल कक्षा 1-2 = 5 साल।"],
["'करके सीखना' के सिद्धांत के जनक कौन हैं?","जॉन डीवी","फ्रोबेल","मोंटेसरी","जॉन डीवी","जॉन डीवी ने Learning by Doing दिया।"],
["कोठारी आयोग का कार्यकाल क्या था?","1964-66","1960-64","1966-68","1964-66","कोठारी आयोग 1964-66 में आया था।"],
["बहुबुद्धि सिद्धांत किसने दिया?","गार्डनर","थार्नडाइक","स्पीयरमैन","हॉवर्ड गार्डनर","गार्डनर ने 8 प्रकार की बुद्धि बताई।"],
["टीईटी (TET) का पूरा नाम क्या है?","शिक्षक पात्रता परीक्षा","शिक्षक प्रवेश परीक्षा","शिक्षक दक्षता परीक्षा","शिक्षक पात्रता परीक्षा","TET = Teacher Eligibility Test।"],
["क्रियाप्रसूत अनुबंधन किसने दिया?","स्किनर","पावलव","थार्नडाइक","स्किनर","स्किनर ने पुनर्बलन का सिद्धांत दिया।"],
["बालक के विकास में सबसे महत्वपूर्ण कारक है?","वंशानुक्रम","वातावरण","दोनों","दोनों","विकास = वंशानुक्रम x वातावरण।"],
["समावेशी शिक्षा का अर्थ है?","सभी को एक साथ शिक्षा","विशेष बच्चों को अलग शिक्षा","केवल प्रतिभाशाली बच्चों की शिक्षा","सभी को एक साथ शिक्षा","समावेशी शिक्षा में सभी बच्चे साथ पढ़ते हैं।"],
["पियाजे के अनुसार संज्ञानात्मक विकास की कितनी अवस्थाएं हैं?","4","3","5","4 अवस्थाएं","सेंसरिमोटर, प्री-ऑपरेशनल, कॉन्क्रीट, फॉर्मल।"]
]

def make_html(today_str, b64=None):
    random.shuffle(QUIZ_BANK)
    selected=QUIZ_BANK[:10]
    banner=make_banner_html(today_str)
    
    html=f"""
    <div style="font-family:Arial,sans-serif;max-width:800px;margin:auto">
    {banner}
    <p style="background:#fff3cd;padding:12px;border-radius:8px;">रोजाना 10 महत्वपूर्ण प्रश्न जो TET / CTET / SuperTET में पूछे जाते हैं। उत्तर के साथ व्याख्या भी दी गई है।</p>
    """

    for i,(q,o1,o2,o3,ans,exp) in enumerate(selected,1):
        html+=f"""
        <div style="border:1px solid #ddd;border-radius:12px;padding:16px;margin:16px 0">
        <h3 style="margin:0 0 8px 0">Q{i}. {q}</h3>
        <p>A) {o1}<br>B) {o2}<br>C) {o3}</p>
        <details style="background:#e8f5e9;padding:10px;border-radius:8px"><summary style="cursor:pointer;font-weight:bold;color:green">▶ Answer Dekhein</summary>
        <p><b>उत्तर: {ans}</b><br>{exp}</p></details>
        </div>
        """
    html+=f"""
    <div style="background:#0b2569;color:white;padding:20px;border-radius:12px;text-align:center;margin-top:20px">
    <h2>TET SUPER 30 - Daily Practice</h2><p>कल फिर मिलेंगे नये 10 सवालों के साथ! Share जरूर करें।</p>
    </div></div>
    """
    return html

def do_post(tk):
    from datetime import datetime
    today=datetime.now().strftime("%d %b %Y")
    html=make_html(today)
    url=f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    data={"kind":"blogger#post","title":f"Daily TET Quiz - {today} | 10 Q&A","content":html}
    r=requests.post(url,json=data,headers={"Authorization":f"Bearer {tk}"},timeout=30)
    r.raise_for_status()
    print("Posted:",r.json().get("url"))

if __name__=="__main__":
    tk=get_token()
    do_post(tk)
