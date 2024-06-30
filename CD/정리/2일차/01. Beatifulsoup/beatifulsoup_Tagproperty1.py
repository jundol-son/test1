from bs4 import BeautifulSoup
html = """
<div id="intro" style='background:red'> 
Hello World 
</div> 
"""
soup = BeautifulSoup(html, 'html.parser')
result = soup.select("div")
print(result)
print(len(result))
print(result[0].attrs)
print(result[0].name)
print(result[0].string)
print(result[0].text)



