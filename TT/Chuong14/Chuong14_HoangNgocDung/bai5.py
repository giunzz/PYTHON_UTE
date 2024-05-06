class Wordplay:
    def __init__(self,wordplay):
        self.word = wordplay
        self.lenght = []
        self.s = []
        self.e = []
        self.pal = []
        self.on = []
        self.avo = []
    def words_with_length(self, lenght):
        for i in self.word:
            if len(i) == lenght: self.lenght.append(i)
        return self.lenght
    def start_with(self):
        for i in self.word:
            if i.startswith('s'): self.s.append(i)
        return self.s
    def end_with(self):
        for i in self.word:
            if i.endswith('s'): self.e.append(i)
        return self.e
    def palidrome(self):
        for i in self.word:
            self.pal.append(i[::-1])
        return self.pal
    def only(self,L):
        for i in self.word:
            if L in i: self.on.append(i)
        return self.on
    def avoids(self,L):
        for i in self.word:
            if L not in i: self.avo.append(i)
        return self.avo

word = ['abc', 'def', 'bdef', 'hkk', 'sse','ss']
t = Wordplay(word)
print(t.only('abc'))
print(t.avoids('abc'))
print(t.palidrome())
print(t.words_with_length(3))
