import string

#text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
#text = """map"""
text = open('mess.txt').read() #open file and read str
def my_solution(text):
    o = ""
    for each in text:
        if ord(each) >= ord('a') and ord(each) <= ord('z'):
            o += chr((ord(each)+2-ord('a'))%26+ord('a'))
        else:
            o += each
    print o

def std_solution(text):
    table = string.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]
+string.ascii_lowercase[:2])
#    print table
    print string.translate(text,table)

def his_solution(text):
    """find English word from text"""
    s = filter(lambda x: x in string.letters,text)
    print s

def forth_solution():
    s = ''.join([line.rstrip('\n') for line in open('mess.txt').readlines()])
    occ = {}
    for c in s:
        occ[c] = occ.get(c,0) + 1 
        avgOC = len(s)// len(occ)
    print avgOC
    print ''.join([c for c in s if occ[c] < avgOC])

if __name__ == '__main__':
    forth_solution()