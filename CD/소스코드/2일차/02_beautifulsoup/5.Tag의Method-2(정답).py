from bs4 import BeautifulSoup

html = """<div id="intro" style='background:red'> 
    Hello World 
</div> 
"""
soup = BeautifulSoup(html, 'html5lib')
result = soup.select_one("div")
print(result)