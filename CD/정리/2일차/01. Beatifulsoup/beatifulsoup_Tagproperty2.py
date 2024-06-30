from bs4 import BeautifulSoup
html = """
<div> 
 <ul> 
 <li> apple </li>
 <li> banana </li>
 </ul>
 <span> grape </span>
 kiwi
</div> 
"""
soup = BeautifulSoup(html, 'html.parser')
result = soup.select("div")
print(result)
print(len(result))
print(result[0].attrs)
print(result[0].name)
print(result[0].string)
#div에 문자열이 없어서 none 반환
print(result[0].text)



