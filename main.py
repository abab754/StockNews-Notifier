import os
from twilio.rest import Client
import requests



COMPANY = input("Enter the company you want to track: ")
STOCK = input("Enter the ticker of the company: ")
stock_api_key = "Enter your stock_api_key"
news_api_key = "Enter your news api key"
account_sid = "enter your account_sid"
auth_tok = "Enter your authentication token"
client = Client(account_sid, auth_tok)

news_api_params = {
    "searchIn": "title",
    "q": COMPANY,
    "apiKey": news_api_key,
}

stock_api_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key,

}
stock_response = requests.get("https://www.alphavantage.co/query?", params= stock_api_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_list = [value for (key,value) in stock_data.items()]
yday_data = stock_data_list[0]
yday_closing_price = float(yday_data["4. close"])

day_b4_yday_data = stock_data_list[1]
day_b4_yday_closing = float(day_b4_yday_data["4. close"])

difference = yday_closing_price - day_b4_yday_closing
sum = yday_closing_price + day_b4_yday_closing
if difference < 0:
    pass
else:
    pass
abs_diff = abs(difference)
percent_diff = (abs_diff/((sum)/2)) * 100
# print(yday_closing_price)
# print(day_b4_yday_closing)
# print(percent_diff)

if percent_diff > 0:
    news_response = requests.get("https://newsapi.org/v2/everything?", params=news_api_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    formatted_list = [f"Title: {article['title']}" for article in three_articles]
    print(len(formatted_list))
    # print(formatted_list[0])
    # for stuff in formatted_list:
    #     print(stuff)
    # str = formatted_list[0]
    for i in formatted_list:
        # print(i)
        message = client.messages.create(
                body= i,
                from_= '+18449191772',
                to='+18482483960'
        )
    print(message.status)


