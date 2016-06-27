import string
import re
import urllib
import urllib2
import pickle,pprint
import Image,ImageDraw
#text = open('equality.txt').read()

def first_solution(text):
    s = "".join(re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',text))
    print s
    ch = ''.join(re.findall('[A-Z]{3}[a-z][A-Z]{3}',s))
    print ch
    ans = 'answer:'
    for c in ch:
        if c.islower():
            ans += c
    print ans

def second_solution(text):
    s = text
    lwr = string.lowercase
    upr = string.uppercase
    print lwr,upr
    for n in range(1,len(s)-1):
        if (s[n-1] in lwr) and (s[n] in upr) and (s[n+1] in upr)\
        and (s[n+2] in upr) and (s[n+3] in lwr)\
        and (s[n+4] in upr) and (s[n+5] in upr)\
        and (s[n+6] in upr) and (s[n+7] in lwr):
            print '\r',s[n+3]

def third_solution(state,c):
    if not c.isalpha():
        #print 'if not {0}, state is {1}'.format(c,state)
        return state
    if state:
        chars_found, state_lower, upper_count = state
    else:
        state_lower = ""
        upper_count = 0
        chars_found = ""
    if c.islower():
        if upper_count == 3:
            if state_lower:
                chars_found += state_lower
            state_lower = c
        else:
            state_lower = ""
        upper_count = 0
    else:
        upper_count +=1
    return chars_found, state_lower, upper_count

def next_nothing():
    data = {}
    number = '12345'
    for i in range(400):
        data['nothing'] = number
        url_values = urllib.urlencode(data)
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
        full_url = url + '?' + url_values

        foo = urllib2.urlopen(full_url)
        foo = foo.read()
        print foo
        foo = foo.split(" ")
        number = [i for i in foo if i.isdigit()][0]

def next_nothing_pro():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    nothing = '12345'
    search = re.compile(" (\d*)$")
    search_html = re.compile("\.html$")

    for i in xrange(400):
        print "%s: " % nothing,

        line = urllib.urlopen("%s%s"%(url,nothing)).read()
        print line

        if search_html.findall(line):
            break
        match = search.findall(line)
        if match:
            nothing = match[0]
        else:
            nothing = str(int(nothing)/2)

def peakhell_solution():
    data = pickle.load(open('banner.p','rb'))
    for each in data:
        print "".join([i[1] * i[0] for i in each])
        #for i in each:
        #    print i[0],i[1]

def write_file():
    im = Image.new("RGB", (95,24),"white")
    draw = ImageDraw.Draw(im)
    data = pickle.load(open('banner.p','rb'))
    line = 0
    for i in data:
        xpos = 0
        for j in i:
            if j[0] == " ":
                draw.line([(xpos,line),(xpos+j[1],line)],255)
            xpos += j[1]
        line += 1
    im.save("banner.bmp")

if __name__ == '__main__':
    #second_solution(text)
    
    #"""linked list"""
    #with open('equality.txt') as f:
    #    s = f.read()
    #s += "x"
    #print reduce(third_solution, s, ())[0]
    
    #"""next nothing"""
    #next_nothing_pro()
    #peakhell_solution()
    write_file()
