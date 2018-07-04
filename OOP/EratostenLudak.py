class EratostenLudak:	#Ime neoriginalno preuzeto od Ivana Stosica 
    def __init__(self):
        self.Sito(10000);
    
    def next(self):
       self.ind += 1;

    def get(self):
        return self.prosti[self.ind];

    def Sito(self, cnt):
        sito = [True for _ in range(cnt+1)];
        sito[0:1] = [False, False];
        for start in range(2, cnt+1):
            if sito[start]:
                for i in range(2 * start, cnt + 1, start):
                    sito[i] = False;
        prosti = [];
        for i in range(2, cnt + 1):
            if sito[i]:
                prosti.append(i);
        self.prosti = prosti;
        self.ind = 0;

t = EratostenLudak();
print(t.get());

t.next();
print(t.get());

t.next();
print(t.get());
