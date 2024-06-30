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
result = soup.select("div")
print(result[0].string)
print(result[0].text)
