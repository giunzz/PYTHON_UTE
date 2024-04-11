def covert_ordinary(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            result += roman[s[i]] - 2 * roman[s[i-1]]
        else:
            result += roman[s[i]]
    return result

def covert_roman(n):
    v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    s = ['M', 'a', 'D', 'b', 'C', 'e', 'L', 'f', 'X', 'g', 'V', 'h', 'I']
    p = {'a': 'CM', 'b': 'CD', 'e': 'XC', 'f': 'XL', 'g': 'IX', 'h': 'IV'}
    result = ""
    i = 0
    while n != 0:
        while n >= v[i] :
            if s[i] in p:
                result += p.get(s[i])
            else : result += s[i]
            n -= v[i]
        i += 1  
    return result

if __name__ == '__main__':
    Roman = input("Enter a Roman numeral: ")
    print("Converts Roman numerals into ordinary numbers:",covert_ordinary(Roman))
    Ordinary = int(input("Enter a ordinary number: "))
    print("Converts ordinary numbers into Roman numerals: ",covert_roman(Ordinary))