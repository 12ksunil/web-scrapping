from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app=Flask(__name__,template_folder='templates')
@app.route('/',methods=["GET","POST"])
def index():
    url="https://www.businesstoday.in/technology/news"
    r=requests.get(url)
    # htmlContent=r.content
    # print(htmlContent)
    soup=BeautifulSoup(r.content,'html.parser')
    outerdata=soup.find_all("div",class_="widget-listing",limit=6)
    finalnews="\n"
    for data in outerdata:
        news=data.div.div.a["title"]
        finalnews += "\u2022 " + news + "\n"
    # print(finalnews)
    return render_template('index.html',News=finalnews)