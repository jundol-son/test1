from bs4 import BeautifulSoup

html = """
<ul>
<li> 뉴스 </li>
<li> 증권 </li>
</ul>
"""

soup = BeautifulSoup(html, 'html5lib')
result = soup.select('li:nth-child(2)')
print(result)