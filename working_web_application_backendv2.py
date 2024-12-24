import requests
from flask import Flask,render_template,request
app=Flask(__name__)

s1=""

def extract_url1(url):
    a=0
    for i in range(0,len(url)):
        if url[i]=='@':
            break
        a+=1
    a+=1
    s=url[a:]
    s=s[:s.index('.')]
    return s

def output(flag):
    if flag==0:
        return "The URL is predicted to be a legitimate URL"
    elif flag==1:
        return "The URL is predicted to be a phishing URL."
    elif flag==2:
        return "The URL is predicted to be a phishing URL"
    

def extract_url3(url):
    flag=2
    return flag

def extract_url2(url):
    s=url[4:]
    s=s[:s1.index('.')]
    return s

def extract_url4(url):
    s=url[8:]
    c=s.count('.')
    if c >= 2:
        s=s[s.index('.')+1:]
        s=s[:s.index('.')]
    elif c == 1:
        s=s[:s.index('.')]
    return s

def unshorten_url(url):
    try:
        response = requests.head("https://"+url, allow_redirects=True)
        return response.url
    except requests.exceptions.RequestException:
        return None

def check_domain(domain,flag):
    trueDomains = ['facebook', "messenger", "instagram", "google", "microsoft", "netflix", "paypal", "steampowered",
                   "twitter", "tiktok", "playstation", "twitch", "pinterest", "linkedin", "snapchat", "quora", "ebay",
                   "spotify", "proton", "reddit", "adobe", "badoo", "deviantart", "supercell", "ajio", "garena", "jio",
                   "pubg", "telegram", "youtube", "airtel", "rockstargames", "live", "olacabs", "origin", "amazon",
                   "mozilla", "amazon", "dropbox", "yahoo", "wordpress", "yandex", "vk", "stackoverflow", "mediafire",
                   "xbox", "gitlab", "github", "apple", "icloud", "myspace", "vimeo", "coinmarketcap", "verizon",
                   "roblox", "discord", "ubereats", "zomato", "whatsapp", "hotstar", "paytm", "mobikwik", "phonepe",
                   "teachable", "flipkart", "tracxn", "aminoapps", "bitcoin","ccn","t","youtube","sanji","zoro",
                   "baidu","wikipedia","instagram","facebook","similarweb","tiktok","live","openai" ,"linkedin",
                   "prime","docomo","dzen","naver","samsung","turbopages","mail","microsoftonline","weather",
                   "pininterest","qq","zoom","quora","duckduckgo","aajtak","globo","ebay","msn","bing",
                   "instructure","walmart","zillow","etsy","indeed","accuweather","aol","imdb","craigslist","t-mobile",
                   "canva","realtor","wellsfargo","lowes","ticketmaster","fedex","tumbir","homedepot","biospot","patreon",
                   "rbi","radiogarden","justwatch","buzzfeed","photopea","forvo","futureme","fotoforensics","ligthningmaps",
                   "pointerpointer","nullschools","naturalreaders","all8","futuretimeline","archive","redmi"]
    if flag == 1:
        for i in trueDomains:
            if domain == i:
                flag=0
                return flag
    return flag

def verify(url):
    domain=""
    flag=1

    if '@' in url:
        domain = extract_url1(url)
        flag=check_domain(domain,flag)
    elif url[0:3]=='www':
        url="https://"+url
        domain = extract_url4(url)
        flag=check_domain(domain,flag)
    elif url[0:5] == 'http:':
        flag = extract_url3(url)
    elif url[0:5]=='https':
        domain = extract_url4(url)
        flag=check_domain(domain,flag)
    else:
        do=unshorten_url(url)
        if do[:5]=="https":
            domain=extract_url4(do)
            flag=check_domain(domain,flag)
        elif do[:5]=="http:":
            domain=extract_url3(do)
            flag=check_domain(domain,flag)
        else:
            print("failed")

    s1=output(flag)
    return s1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_input():
    url = request.form['user_input']
    s1=verify(url)
    return render_template('index.html',Result=s1)

if __name__=="__main__":
    app.run(debug=True)