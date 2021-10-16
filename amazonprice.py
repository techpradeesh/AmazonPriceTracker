from bs4 import BeautifulSoup
import requests
import smtplib

headers = {
    'User-Agent': "header",
    'Accept-Language': 'en-US,en;q=0.9'
}
url = "url of the amazon.in product, fire stick"
response = requests.get(url,headers=headers)
amazon_response = response.text

soup = BeautifulSoup(amazon_response,'html.parser')
price = soup.find(name="span",class_="a-size-medium a-color-price priceBlockDealPriceString")
title_ds = soup.find(name="title")
title = title_ds.getText()
price_text = float(price.text[1:].replace(",",''))

def send_newmail():
    my_email = "sendingemail"
    password = "password"
    to_email = "tosendingemail"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                         to_addrs=to_email,
                         msg=f"Subject:Amazon Price Alert\n\n{title}\nPrice is now {price_text}\n{url}")
    connection.close()
status = True
while status == True:
    try:
        desired_price = float(input("Enter your desired price : "))
    except ValueError:
        print("Please Enter a valid price!")
    else:
        status = False
        if price_text <= desired_price:
            send_newmail()
        else:
            print(f"Price is higher than your desired price {desired_price}")
            
