from bs4 import BeautifulSoup
html = """
<ul>
<li> 뉴스 </li>
<li> 증권 </li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
result1 = soup.select("ul li")
result2 = soup.select("ul li:nth-child(2)")
print(type(result1[0]))
print(result1[1].contents)
print(result2)
