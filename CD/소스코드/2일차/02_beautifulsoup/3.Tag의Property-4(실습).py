from bs4 import BeautifulSoup

html = """
<div> 
    <ul> 
        <li> apple </li>
        <li> banana </li>
    </ul>
    <span> grape </span>
</div> 
"""
soup = BeautifulSoup(html, 'html5lib')
result = soup.select("li:nth-child(1)")
print(result[0])