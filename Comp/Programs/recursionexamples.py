

def print_stars(n):
    if n==0:
        pass
    else:
        print '*'
        print_stars(n-1)
         
print_stars(5)
