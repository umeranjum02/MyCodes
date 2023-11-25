import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
AmazonUrl= "https://www.amazon.com/Soundcore-Cancelling-Headphones-Comfortable-Bluetooth/dp/B0B5VHRX7F/ref=sxin_16?asc_contentid=amzn1.osa.bc0957bb-263c-40cc-a2bf-c26a24e87fca.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.bc0957bb-263c-40cc-a2bf-c26a24e87fca.ATVPDKIKX0DER.en_US&content-id=amzn1.sym.2501e731-e00e-46aa-97f8-28a8de3ef511%3Aamzn1.sym.2501e731-e00e-46aa-97f8-28a8de3ef511&creativeASIN=B0B5VHRX7F&crid=1U2FMCYZUKXY5&cv_ct_cx=headphones&cv_ct_id=amzn1.osa.bc0957bb-263c-40cc-a2bf-c26a24e87fca.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&keywords=headphones&linkCode=oas&pd_rd_i=B0B5VHRX7F&pd_rd_r=8fb89b2f-3958-40a3-b5d1-2077363fa1f7&pd_rd_w=z3Xkg&pd_rd_wg=2xDrO&pf_rd_p=2501e731-e00e-46aa-97f8-28a8de3ef511&pf_rd_r=K0C910PEH4ZBJQ8SSQ0Q&qid=1680129390&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=headphone%2Caps%2C367&sr=1-1-c26ac7f6-b43f-4741-a772-17cad7536576&tag=onsitertings-20&th=1"
Amazonwebpage=requests.get(AmazonUrl,headers=HEADERS)
soup = BeautifulSoup(Amazonwebpage.content, 'lxml')
name1 = soup.find("span", attrs={"id":'productTitle'}).string.strip()
AmazonPrice = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
print(name1)
print(AmazonPrice)
EbayUrl = "https://www.ebay.com/itm/175645816560?epid=8056684409&hash=item28e54e76f0:g:u~QAAOSwdntkC1yR&amdata=enc%3AAQAHAAABoH2FGeJO6Be5oRGDzVEc6Ep%2FhGPMgKq%2B1lyyv7In4XM1wko9O9pvIkuecuMo7IfeQA98txc0WsEWHaPTDU9OXYuX4Tva7mC5awLn9XN6nkSYIvelel5eAazY6btgEnhDQa6any%2FwxaIX9%2FQ6EbcGOXwxc%2FkC7S1%2FDAYtdJLCcCBgRkRz0Ln1bhztlwfsaJ%2FK6oFmlOkYYfpgHxdPG%2FOCqdLLCd%2BMMt2HD273UDBLxsmY%2BlOJdbY0wPPR%2F0o4lMwm8RYW39gqDTN20gQ5ncduFHCExmqpsZaspdOUb5qcdg1%2FzlTPXuTS9%2F%2FC%2BO5wreLQLFXta5CK21%2FXoOflPVJUlvtVqYWw0h1%2BvHTlGQg7uMVudzWLoKXQoCv7MFEaFFoQPgMQvsyupLEaCyxBXEywHHaEnwf%2B9tpGXLV2QpoNs%2FU%2FHiVTy7rh%2Feth%2B6CPR0zLpdLjvbsjBUSxfwmtdkYv30GvZ%2FOs%2FJEaYuq%2FFVpChQLx07RSO5d1elZdbs8zBAjyUJPBAafZ9mRE5zzlQbQWBqFPaprJmte2cjMUPFHwCzHn%7Ctkp%3ABFBMrNal-OVh"
EbayWebPage = requests.get(EbayUrl)
soup2 = BeautifulSoup(EbayWebPage.text, 'html.parser')
name2 = soup2.find('h1', class_="x-item-title__mainTitle")
EbayPrice=soup2.find('div',class_='x-price-primary')
print(name2.text)
print(EbayPrice.text)
a = 159.99
b = 205.96
if a > b:
    print("Ebay Price is low :"+str(EbayPrice))
elif b > a:
    print("Amazon Price is low :"+str(AmazonPrice))
else:
    print("Both are of same rate") 

fig, ax = plt.subplots()
ax.bar(['Product 1'],a , label = 'AMAZON')
ax.bar(['Product 2'],b,label = 'EBAY')
ax.set_xlabel('Product')
ax.set_ylabel('Prices')
ax.set_title('Comparison of Prices on Amazon and eBay')
ax.legend()
plt.show() 
