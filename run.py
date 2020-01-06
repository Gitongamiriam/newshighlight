from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.ruote('/')
def index():
    newsapi =NewsApiClient(api_key='6e766d66ef3d492ca4ffe25ebfbfa61e')
    topheadlines=newsapi.get_top_headlines(sources='bbc-news')
    articles=topheadlines['articles']
    
    des=[]
    image=[]
    news[]
    
    for i in range(len(articles)): 
        myarticles=articles[i]
        
        news.append(myarticles['title'])
        image.append(myarticles['urlToImage'])
        
    


if __name__=='__main__':
    app.run(debug =True)