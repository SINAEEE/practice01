
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""


#print(s.splitlines())
#print(s.replace('<','').replace('>','').replace('/',''))
print(s.replace(s[1:49],''))


