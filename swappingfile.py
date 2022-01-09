def swapping():
    o = open("sample1.txt", "r")
    r = o.read()

    o2 = open("sample2.txt", "r")
    r2 = o2.read()

    o = open("sample1.txt", "w")
    o.write(r2)

    o2 = open("sample2.txt","w")
    o2.write(r)
swapping()