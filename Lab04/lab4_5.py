class dna_strand:

    def __init__(self, keys):
        self.keys = keys

    def is_valid(self):
        valid_keys = ['A', 'T', 'C', 'G']
        validation = [i in valid_keys for i in self.keys]
        # if all(validation): 
        if all(validation) and len(self.keys) > 0:
            return True
        else:
            return False
    
    def complement_wc(self):
        copy = self.keys
        for i in range(len(copy)):
            match copy[i]:
                case 'A':
                    copy[i] = 'T'
                case 'T':
                    copy[i] = 'A'
                case 'C':
                    copy[i] = 'G'
                case 'G':
                    copy[i] = 'C'
        return copy
    
    def palindrome_wc(self):
        l = self.complement_wc()
        l.reverse()
        return l

    def contains_seq(self, seq):
        if seq in self.keys:
            return True
        else:
            return False

    def __str__(self):
        return str(self.keys)
    
    @staticmethod
    def summarise(dna):
        print("Original DNA Sequence: " , dna)
        if dna.is_valid():
            print("Is valid")
            print("Complement: " , dna.complement_wc())
            print("WC Palindrome: " , dna.palindrome_wc())
        else:
            print("Not Valid DNA") 

a = dna_strand(['A','T', 'C', 'G'])
b = dna_strand(['A', 'B'])
# print(b.is_valid())
# print(a.complement_wc())
# print(a.palindrome_wc())
dna_strand.summarise(a)
dna_strand.summarise(b)