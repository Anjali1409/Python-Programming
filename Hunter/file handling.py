fh=open("c:/documents",w+)
fh.write("hai")
fh.seek(0)
print(fh.read())
