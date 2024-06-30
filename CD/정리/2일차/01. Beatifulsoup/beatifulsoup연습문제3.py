from bs4 import BeautifulSoup
html = """
<ul>
<li> Apple </li>
<li> Banana </li>
 <li> Grape </li>
</ul>
"""
soup = BeautifulSoup(html, 'html.parser')

result1 = soup.select("ul li")
result2 = soup.select_one("ul li")
result3 = soup.select_one("ul li:nth-child(3)")

print(result1[0].text,result1[2].text)
print(result2.text,result1[2].text)
print(result2.text,result3.text)
