#スクレイピング
import urllib.request as req
from bs4 import BeautifulSoup
#LINEBot
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

#LINEBot チャネル
line_bot_api = LineBotApi("3dSzUytSAnRrwm5UZVJrQ927Jr9Zr18ZiEAPvJO1O+Ujq4ojGV4++Gx4cjBt6gk4kP7uFfwzdhzP/VXAhM/n6ecxhq6Tc+BolVnZAem6/H74mK/UDLLSFAY6LXu1TJeH6ocOM3I1K3TP2M+rReFE1wdB04t89/1O/w1cDnyilFU=")
LINE_USER_ID_TO = "U3adcd002fefaef0ace51869b69215e70"

#スクレイピング
url = 'https://transit.yahoo.co.jp/traininfo/area/4/'
res = req.urlopen(url)
soup = BeautifulSoup(res, "lxml")
result = []

#LINEBot
def message():
	try:
         bot_message = str(row).strip("[]")
         bot_message = ''.join(row)
         line_bot_api.push_message(LINE_USER_ID_TO,TextSendMessage(bot_message))
	except LineBotApiError as e:
		print(e)
  
def message2():
    try:
        line_bot_api.push_message(LINE_USER_ID_TO, TextSendMessage(url))
    except LineBotApiError as e:
        print(e)

#電車情報取得
table = soup.select("table")
for table_list in table:
    tr_list = table_list.find_all("tr")
    for tr in tr_list:
        result_row = []
        td_list = tr.find_all(["td", "th"])
        for td in td_list:
            cell = td.get_text()
            result_row.append(cell)
        result.append(result_row)
for i, row in enumerate(result):
    if i == 3 or i == 4 or i == 37 or i == 77 or i == 78 or i == 79 or i == 80 or i == 81 or i == 82 or i == 95 or i == 98:
        print(str(i) + ":" + ",".join(row))
        message()
message2()
    
    
    






