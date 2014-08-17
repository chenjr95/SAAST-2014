isbn = [0,1,8,9,4,6,7,8,9,4]

zipped = (sum(x*y for x,y in zip(isbn,range(1,10))))%11 == isbn[9]

print zipped

y = [x*x for x in range(10)]
print y