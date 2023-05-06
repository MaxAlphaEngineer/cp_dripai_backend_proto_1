from requests_html import HTMLSession

s = HTMLSession()

user_input = input("Enter city: ")
url = f"https://www.google.co.uz/search?q=weather+{user_input}"

r = s.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

temp = r.html.find('span#twob_tm', first=True).number
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True). find('spanttwob_de', first=True).text


print(user_input, temp, unit, desc)

















