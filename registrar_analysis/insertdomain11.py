

domains = set()

fp = open('srv_domains.txt','r')
for i in fp.readlines():
    domains.add(i.strip())
print len(list(domains))


fp = open('srv_domains1.txt','r')
for i in fp.readlines():
    domains.add(i.strip())
print len(list(domains))


fp = open('srv_domains2.txt','r')
for i in fp.readlines():
    domains.add(i.strip())
print len(list(domains))


fp = open('srv_domains3.txt','r')
for i in fp.readlines():
    domains.add(i.strip())
print len(list(domains))


for i in list(domains):
    print i



fp.close()