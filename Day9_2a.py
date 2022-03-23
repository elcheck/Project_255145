def get_common_elements(seq1, seq2, seq3):
        return tuple(set(seq1).intersection(set(set(seq2).intersection(set(seq3)))))
print (get_common_elements("abcd", ['a', 'b','d'], ('b', 'c','d')))