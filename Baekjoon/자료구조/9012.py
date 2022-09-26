for _ in range(int(input())):
    b=input()
    while '()' in b:
        b = b.replace("()",'')
    print("no" if b else "YES")