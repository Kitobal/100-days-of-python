import smtplib
import requests
from config import alpha_vantage_key, newsapi_key, my_email, my_password, to_email
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alpha_vantage_key,
}

response= requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close = yesterday_data["4. close"]
# print(yesterday_close)

day_before_yesterday_data = data_list[1]
day_before_yesterday_close = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_close)

difference = abs(float(yesterday_close) - float(day_before_yesterday_close))
# print(difference)

diff_percent = (difference / float(yesterday_close)) * 100
# print(diff_percent)
if diff_percent > 5:
    news_params = {
        "apiKey": newsapi_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    # print(three_articles)

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                msg=f"Subject: {COMPANY_NAME} Update\n{article}")
