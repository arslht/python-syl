# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
import re,zipfile
import Image
import bz2

def find_nothing():
    findnothing = re.compile(r'Next nothing is (\d+)').match
    seed = '90052'
    while True:
        fname = seed + '.txt'
        text = open('channel/'+fname,'r').read()
        m = findnothing(text)
        if m:
            seed = m.group(1)
            print seed
        else:
            print text
            break
def find_nothing_pro():
    findnothing = re.compile(r"Next nothing is (\d+)").match
    comments = []
    z = zipfile.ZipFile("channel.zip","r")
    seed = '90052'
    while True:
        fname = seed + '.txt'
        comments.append(z.getinfo(fname).comment)
        guts = z.read(fname)
        m = findnothing(guts)
        if m:
            seed = m.group(1)
        else:
            break
    print " ".join(comments)

def image_x():
    img = Image.open('oxygen.png')
    print img.size
    data = [img.getpixel((i,j)) for i in range(0,609) for j in range(43,53)]
    #print data
    row = [chr(img.getpixel((i,43))[0]) for i in range(0,609,7)]
    print "".join(row)
    print "".join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))

def decompress():
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print 'usrname : {}'.format(bz2.decompress(un))
    print 'passwd  : {}'.format(bz2.decompress(pw))

if __name__ == "__main__":
    #find_nothing_pro()
    #image_x()
    decompress()
