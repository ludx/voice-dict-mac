# 处理不规则单词（待完善）
# 设置用户语音库路径

import sys, os, re

wds = sys.argv[1]

rule_tuple = (
('[ml]ice$', '([ml])ice$', '\\1ice'), 
('booths$', 'booths$', 'booth'), 
('feet$', 'feet$', 'foot'), 
('eeth$', 'eeth$', 'ooth'), 
# ('l[eo]aves$', 'l([eo])aves$', 'l\\1af'), 
('ses$', 'ses$', 'sis'), 
# ('men$', 'men$', 'man'), 
('ives$', 'ives$', 'ife'), 
('eaux$', 'eaux$', 'eau'), 
('lves$', 'lves$', 'lf'), 
('[sxz]es$', 'es$', ''), 
('[^aeioudgkprt]hes$', 'es$', ''), 
('(qu|[^aeiou])ies$', 'ies$', 'y'), 
('s$', 's$', ''),
(',$', ',$', ''),
('.$', '.$', ''),
('ed$', 'ed$', ''),
#('ing$', 'ing$', 'e')
('ing$', 'ing$', '')
)
 
def regex_rules(rules=rule_tuple):
    for line in rules:
        pattern, search, replace = line
        yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)
 
def danshu(noun):
    for rule in regex_rules():
        result = rule(noun)
        if result: 
            return result


try:
    path = "/Users/lispython/workspace/dict/voice/"+wds[0]+"/"+wds+".wav"
    if not os.path.exists(path):
        wd = danshu(wds)
        path = "/Users/lispython/workspace/dict/voice/"+wd[0]+"/"+wd+".wav"
    print path
except:
    pass
