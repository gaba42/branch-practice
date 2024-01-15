def fiz():
    div3 = ['fizz' if i%5==0 else i for i in range(1, 16)]
    print(div3)


if __name__=="__main__":
    fiz()
