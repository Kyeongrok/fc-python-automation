import requests

def crawl(url):
    res = requests.get(url)
    print(res)

    pass

url = "https://www.coupang.com/vp/products/131222787?itemId=386242196"
# url = "https://www.google.com/"
crawl(url)