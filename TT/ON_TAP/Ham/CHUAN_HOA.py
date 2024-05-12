def chuẩn_hóa_xâu(s):
    # Tách xâu thành các từ
    words = s.split()

    # Chuẩn hóa từng từ
    for i in range(len(words)):
        words[i] = words[i].capitalize()

    # Nối các từ lại với nhau bằng dấu cách
    normalized_s = ' '.join(words)

    return normalized_s

s = "đây là một xâu cần được chuẩn hóa"
print(chuẩn_hóa_xâu(s))