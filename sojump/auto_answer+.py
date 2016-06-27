#-*- coding:utf8 -*-
import urllib, urllib2, random, re
from time import localtime, strftime, time

def gen_uri_param(curID, rn):
    uri_param = {}
    uri_param['submittype'] = '1'
    uri_param['t'] = str(int(time()*1000))
    uri_param['starttime'] = strftime("%Y/%m/%d %H:%M:%S", localtime())
    uri_param['rn'] = rn
    uri_param['curID'] = curID
    return uri_param

def gen_post_string(answer):
    def concat_pair(pair):
        return '$'.join([str(pair[0]), str(pair[1])])

    tmp_list = []
    for x in answer:
        tmp_list.append(concat_pair(x))
    return '}'.join(tmp_list)


jq_url = "http://www.sojump.com/jq/183859.aspx"
jq_base = "http://www.sojump.com/jq/{}.aspx"
uri_base = "http://www.sojump.com/handler/processjq.ashx?{}"


response = urllib2.urlopen(jq_url)
text = response.read();
#print text
rndnum = re.search('rndnum="(\d+\.\d+)"',text).group(1);
curID = re.search('(\d+).aspx',response.geturl()).group(1)
jq_sum = int(re.findall('div(\d+)',text)[-1])


answer_list = [1,1,1,1,1,1,1,1]
answer = zip(range(1,jq_sum+1),answer_list)

post_data = urllib.urlencode({'submitdata':gen_post_string(answer)})
get_data = urllib.urlencode(gen_uri_param(curID, rndnum))

request_url = uri_base.format(get_data)
request = urllib2.Request(request_url, post_data)
result = urllib2.urlopen(request)
print result.read()
