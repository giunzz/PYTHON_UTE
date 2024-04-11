def verbose(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty',
        30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (num < 20): return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + verbose(num % 100)

    if (num < m):
        if num % k == 0: return verbose(num // k) + ' thousand'
        else: return verbose(num // k) + ' thousand, ' + verbose(num % k)

    if (num < b):
        if (num % m) == 0: return verbose(num // m) + ' million'
        else: return verbose(num // m) + ' million, ' + verbose(num % m)

    if (num < t):
        if (num % b) == 0: return verbose(num // b) + ' billion'
        else: return verbose(num // b) + ' billion, ' + verbose(num % b)

    if (num % t == 0): return verbose(num // t) + ' trillion'
    else: return verbose(num // t) + ' trillion, ' + verbose(num % t)

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(str(n) + ":" +  str(verbose(n)))