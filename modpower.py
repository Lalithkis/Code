if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    
    result1 = (a ** b) ** c
    result2 = a ** (b ** c)
    
    print(result1)
    print(result2)
