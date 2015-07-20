def rotn(wordIn, n):
    newWord=""
    for symbol in wordIn:
        numeric=ord(symbol)
        if ord("A")<=numeric<=ord("Z") or ord("a")<=numeric<=ord("z"):
            numeric+=n
            while numeric>ord("z") and symbol.islower():
                numeric-=26
            while numeric>ord("Z") and symbol.isupper():
                numeric-=26
            while numeric<ord("a") and symbol.islower():
                numeric+=26
            while numeric<ord("A") and symbol.isupper():
                numeric+=26
            newSymbol=chr(numeric)
            newWord+=newSymbol
        else:
            newWord+=symbol
    return newWord
