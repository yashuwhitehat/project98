def swapfile():
    f1= input ("enter file name")
    f2= input ("enter file name")
    with open(f1,'r')as a:
        ba=a.read()
    with open(f2,'r')as b:
        bb=b.read()
    with open(f1,'w')as a:
        a.write(ba)
    with open(f2,'w')as b:
        b.write(bb)
swapfile()