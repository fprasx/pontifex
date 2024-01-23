import random

d = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,
    29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54
    ]
random.seed(5318008)
random.shuffle(d)

# golf start
i=lambda x:d.index(x)
p=lambda j:53>(k:=i(j))and d[:k]+[d[k+1],j]+d[k+2:]or[d[0],j]+d[1:k]
def k():global d;d=p(53);d=p(54);d=p(54);lo,hi=sorted([i(53),i(54)]);d=d[hi+1:]+d[lo:hi+1]+d[:lo];b=min(d[-1],53);d=d[b:-1]+d[:b]+[d[-1]];t=min(d[0],53);return 53>d[t]and d[t]or k()
encrypt=lambda s:"".join(chr(97+(ord(c)-97+k())%26)for c in s)
# golf end

expected = "rvwszsylhrnfpkpeetpooeuqenlkhfynbncoohblhadptklqqkliqggoddcwqcfgxsazququpdzjkeqgcsachmjskaxcxqheawtwqymadnibxsxylrtkahsrwwvlcfhf"
plaintext = "mvdpbacxvvlpmeabquboslrcrxdaqfedkywedhybmpanzabutgjdahejnkhrgsbaxczydcdyuinxkptidzwlnocetmjnwxekzzyjyhsgjkuecfsicwprfpgfsmqkzkki"
result = encrypt(plaintext)
assert result == expected, f"{result}"
