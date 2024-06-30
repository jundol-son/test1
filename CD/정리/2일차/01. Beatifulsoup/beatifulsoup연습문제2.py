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
soup = BeautifulSoup(html, 'html.parser')
result1 = soup.select("div li")
result2 = soup.select("div li:nth-child(2)")
result3 = soup.select("div")
result4 = soup.select_one("li")
result5 = soup.find("li")
result6 = soup.find_all("li")

print(result1[1].text)
print(result1[1].string)
print(result2[0].text)
print(result3[0].text.split('\n')[3])
print(result4)
print(result5)
print(result6)