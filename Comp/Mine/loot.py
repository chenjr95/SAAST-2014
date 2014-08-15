import random


def main():
	m=pick_mon()
	trea=look_treasure(m[len(m)-1])
	base=comput_base(trea)
	print "Fighting {0} (Level {1} {2})".format(m[0],m[2],m[1])
	print "You have slain {0} !".format(m[0])
	print "{0} dropped: \n".format(m[0])
	kl=gen()
	print "{0} {1} {2}".format(kl[0][0],trea,kl[1][0])
	print "Defense: {0}".format(base)
	if len(kl[0])>1:
		print "{0} {1}".format(random.randint(int(kl[0][2]),int(kl[0][3])),kl[0][1])
	if len(kl[1])>1:
		print "{0} {1}".format(random.randint(int(kl[1][2]),int(kl[1][3])),kl[1][1])

def pick_mon():
	with open('large/monstats.txt','r') as f:
		glist=f.readlines()
	return glist[random.randint(0,len(glist)-1)].replace('\n','').split(',')


'''-----------------------------------treasure------------------------------------------'''
def look_treasure(mon):
	with open('large/TreasureClassEx.txt','r') as f:
		glist=f.readlines()
	return generate(make_dic(glist),mon)

def make_dic(l):
	l1=[i.replace('\n','').split(',') for i in l]
	d = {}
	for m in l1:
		d[m[0]] = m[1:]
	return d

def generate(gram,tok):
	if tok not in gram:
		return tok
	else:
		rules = gram[tok]
		return generate(gram,rules[random.randint(0,len(rules)-1)])

'''-----------------------------------base stats------------------------------------------'''
def comput_base(weap):
	with open('large/armor.txt','r') as f:
		glist=f.readlines()
	return stat(make_dic(glist),weap)

def stat(gram,tok):
	return random.randint(int(gram[tok][0]),int(gram[tok][1]))
'''-----------------------------------prefix------------------------------------------'''
def gen():
	return [pre(),suf()]  

def pre():
	with open('large/MagicPrefix.txt','r') as f:
		glist1=f.readlines()
	if random.randint(0,1):
		return glist1[random.randint(0,len(glist1))].replace('\n','').split(',')
	else:
		return ['']
def suf():
	with open('large/MagicSuffix.txt','r') as g:
		glist2=g.readlines()
	if random.randint(0,1):
		return glist2[random.randint(0,len(glist2))].replace('\n','').split(',')
	else:
		return ['']



main()