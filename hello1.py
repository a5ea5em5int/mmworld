import json
w = json.load(open('worldl.json'))
for c in w:
	if 'Myanmar'==c['name']:
		print (c)

print (len(w))
for c in w:
	if c['name']=='France':
		print (c['capital'])
	if c['name']=='China':
		print(c['population']//1000000)

c=len([c for c in w if c['continent']=='Asia'])
print (c)
c= [i['population'] for i in w if i['continent']=='Africa']
m = max(c)
print(m)
bp = [cc['name'] for cc in w if cc['population']==m]
print(bp)
afc =[x for x in w if x['continent']=='Africa' ]
afs =sorted(afc,key=lambda c:c['population'])
print(afs[-1]['name'])