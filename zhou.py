import requests
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-09-20&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
response=requests.get(url)
print(response.url)
print(response.text)
