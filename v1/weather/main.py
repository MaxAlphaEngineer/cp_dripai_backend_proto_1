from requests_html import HTMLSession

s = HTMLSession()

user_input = input("Enter city: ")
url = f"https://www.google.co.uz/search?q=weather+{user_input}"

r = s.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True). find('span#wob_dc', first=True).text


print(temp, unit, desc, user_input)

















