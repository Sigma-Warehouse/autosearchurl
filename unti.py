def hoge(x):
    if x < 10:
        x += 1
        hoge(x)
    else:
        return x
    
print(hoge(1))
