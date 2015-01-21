'''This program converts UTF-32 encoded literals to UTF-16 (supported by Neo4j) by using surrogates
'''

fp2 = open ('LAK-DATASET-DUMP.c','w')
with open('LAK-DATASET-DUMP.cyp','r') as fp:
  for sen in fp.readlines():
    import re
    l = re.findall(r'\\U\w{8}',sen)

    for i in l:
      S = i.replace(r'\U',r'0x')
      S = int(S,16)
    
      H = ((S - 0x10000) // 0x400) + 0xD800;
      L = ((S - 0x10000) % 0x400) + 0xDC00;
      
      Sur = hex(H)+hex(L)
      Sur = Sur.replace(r'0x',r'\u')
      sen = sen.replace(i,Sur)
    fp2.write(sen)
      
fp2.close()
