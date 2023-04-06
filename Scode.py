def get_data(query):
    try:
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup
        from flask import Flask,request,jsonify
        print("packages are imported..!")
        url = f"https://www.allrecipes.com/search?{query}={query}&offset=0&q={query}"
        req = requests.get(url)
        print(req)
        soup = BeautifulSoup(req.content,"html.parser")
        aurl = []
        tit = []
        imgs = []
        for a in soup.findAll("div",{"class":"comp search-results__content mntl-block"}):
            for b in a.findAll("div",{"class":"comp card-list mntl-document-card-list mntl-card-list mntl-block"}):
                for c in b.findAll("a",{"class":"comp mntl-card-list-items mntl-document-card mntl-card card card--no-image"}):
                    aurl.append(c.get("href"))
        for d in soup.findAll("span",{"class":"card__title"}):
            for e in d.findAll("span",{"class":"card__title-text"}):
                tit.append(e.text.strip())
        
        for f in soup.findAll("div",{"class":"card__media mntl-universal-image card__media universal-image__container"}): 
            for g in f.findAll("div",{"class":"img-placeholder"}):
                for h in g.findAll("img"):
                    if h.get("src") == None:
                        continue
                    # print(h.get("src"))
                    imgs.append(h.get("src"))
    except Exception as e:
        raise e
    # !pip install bs4 pandas Flask requests
    df = pd.DataFrame([aurl,tit,imgs])
    df = df.T
    df.columns = ['Article_url',"Dish_name","Image_url"]
    D = {}
    for i in range(len(df)):
        D[i] = df.iloc[i].to_dict()
    return D