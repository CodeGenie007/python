y = 2


def paul(x,n = 2):
    global y
    y = y + 1
    return y * x

print y, paul ("z")
print y, paul (2+1)
print y, paul ("z")
print y, paul ("z")
print y, paul ("z")
y = 1
print y, paul ("z")

while y<10:
    print y, paul("z")


               
               
