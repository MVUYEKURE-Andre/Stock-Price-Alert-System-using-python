import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# today_time=datetime.datetime.today()
# print(today_time)

Alpha_API_key= "K2VTRCGG6SCHN1BA"
parameters={
"function":"TIME_SERIES_INTRADAY",
    "symbol":"IBM",
    "interval":"60min",
    "apikey":Alpha_API_key
}
# Mp part to be improved
# response=requests.get(url=STOCK_ENDPOINT,params=parameters)
# response.raise_for_status()
# data=response.json()["Time Series (60min)"] #["2025-11-21 19:00:00"] #["4. close"]
# print(data)
# closing_point=[float(value["4. close"])  for (key, value) in data.items()]
# print(closing_point)




# today_time=dt.datetime.now()
# print(today_time)
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
json_data = response.json()
# data2=response.json()["2025-11-21 19:00:00"]

if "Time Series (60min)" in json_data:
    data = json_data["Time Series (60min)"]
    closing_point = [float(value["4. close"]) for key, value in data.items()]# if data2(today_time)[-1]]
    print(closing_point[0])
    print(closing_point[1])
else:
    print("API response error or rate limit hit:", json_data[0])
# # morning idea let take yesterday and today by using index in final list



#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

