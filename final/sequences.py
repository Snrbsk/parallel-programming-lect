
seq = [1,2,3,4,4,5,6,7]
d = {1:2,3:4,5:6}
def remove_duplicates(seq: list)-> list:
    print(list(set(seq))) 


def list_counts(seq: list)-> dict:
    print({num: seq.count(num) for num in seq}) 



def reverse_dict(d: dict) -> dict:
    print({v: k for (k,v) in d.items()})
 
remove_duplicates(seq)
list_counts(seq)
reverse_dict(d)
