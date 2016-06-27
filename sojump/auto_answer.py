# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib,urllib2,random
from time import localtime,strftime,time

#return uri param dict
def gen_uri_param():
    curID = '183859'
    submittype = '1'
    t = str(int(time()*1000))
    starttime = strftime("%Y/%m/%d %H:%M:%S", localtime())
    rn = '1925827705.52812198'#'3065862882'
    return locals()

#return submitdata str
#([(1,2),(2,4),(3,1)]) => '1$2}2$4}3$1'
def gen_post_string(answer):
    def concat_pair(pair):
        return '$'.join([str(pair[0]),str(pair[1])])
    
    tmp_list = []
    for x in answer:
        tmp_list.append(concat_pair(x))
    return '}'.join(tmp_list)

jq_base = "http://www.sojump.com/jq/{}.aspx"
uri_base = "http://www.sojump.com/handler/processjq.ashx?{}"

#answer is in this form:[(1,2),(2,1),(3,5)...],these answer is generated randomly
#answer_list = [1,2,3,4,1,2,3,4,1,2]
#answer = zip(range(1,11),answer_list)
answer = zip(range(1,11),[random.randint(1,4) for x in range(11)])

#post传参与get传参的区别（开头的链接）
post_data = urllib.urlencode({'submitdata':gen_post_string(answer)})
get_data = urllib.urlencode(gen_uri_param())

request_url = uri_base.format(get_data)
request = urllib2.Request(request_url,post_data)
result = urllib2.urlopen(request)
print result.read()

# <codecell>
