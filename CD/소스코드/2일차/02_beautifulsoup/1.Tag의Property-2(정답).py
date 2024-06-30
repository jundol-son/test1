from bs4 import BeautifulSoup

html = """<div id="intro" style='background:red'> 
    Hello World 
</div> 
"""
soup = BeautifulSoup(html, 'html5lib')
result = soup.select("div")
print(result[0].name)
