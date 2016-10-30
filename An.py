print('import numpy as np',sep=' ',end='')
import numpy as np
print(' DONE ')
print('loading arrays',sep=' ',end='')
x=['-', '+', '-', '+', '-', '+', '+', '+', '-', '-', '-', '+', '+', '-', '-', '+', '+', '+', '+', '+', '-', '-', '-', '+', '-', '+', '+', '+', '+', '-', '-', '+', '+', '-', '+', '-', '+', '+', '+', '-', '-', '+', '+', '+', '+', '-', '+', '-', '+', '-']
tta=['10', '10', '17', '17', '21', '21', '27', '27', '30', '30', '34', '34', '37', '37', '40', '40', '43', '43', '46', '46', '49', '49', '52', '52', '55', '55', '58', '58', '62', '62', '65', '65', '68', '68', '71', '71', '75', '75', '77', '77', '83']
PAs=['1', '1', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Ks= ['1', '1', '2', '3', '4', '4', '5', '6', '7', '8', '9']
PKs=['1', '1', '2', '3', '4', '5', '5', '6', '7', '8', '9']
PSs=['1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9']
NEs=['2', '3', '4', '5', '6', '7', '8', '9', '9', '9', '9']
factor1=[1, 2, 11, 12, 21, 22, 31, 32, 41, 42]
factor2=[6, 7, 16, 17, 26, 27, 36, 37, 46, 47]
factor3=[3, 13, 23, 33, 43]
factor4=[8,18,28,38,48]

print(' DONE ')

print('formating arrays',sep=' ',end='')

for i in range(len(PKs)):
	PAs[i]=int(PAs[i])
	Ks[i]=int(Ks[i])
	PKs[i]=int(PKs[i])
	PSs[i]=int(PSs[i])
	NEs[i]=int(NEs[i])
z=np.array(x)
z=z.reshape(10,5)
print(' DONE ')
print('loading functions',sep=' ',end='')

localFactor1=[]
localFactor2=[]
localFactor3=[]
localFactor4=[]

for i in range(len(factor1)):
	localFactor1.append(x[factor1[i]])

for i in range(len(factor2)):
	localFactor2.append(x[factor2[i]])

for i in range(len(factor3)):
	localFactor3.append(x[factor3[i]])

for i in range(len(factor4)):
	localFactor4.append(x[factor4[i]])

def inside():# кладёт в переменную ответы и сортирует их
	e=input('ответы да= нет- : ')
	c=[]
	for i in range(len(e)):
		c.append(e[i])
	for i in range(len(c)):
		if(c[i]=='='):
			c[i]='+'
	return(c)

def inside_auto(ans):# кладёт в переменную ответы и сортирует их(автоматический режим)
	c=[]
	for i in range(len(ans)):
		c.append(ans[i])
	for i in range(len(c)):
		if(c[i]=='='):
			c[i]='+'
	return(c)

def resList(ans):#принимает ответы в виде линейного массива и сравнивает их с правильными
	res=[]
	ans=np.array(ans)
	ans=ans.reshape(10,5)
	res=(ans==z)
	return(res)
	#print(res)

def Pas_int(res):
	counter=0
	for i in range(10):
		if (res[i][0]==True):
			counter=counter+1
	return(counter)


def Ks_int(res):
	counter=0
	for i in range(10):
		if (res[i][1]==True):
			counter=counter+1
	return(counter)

def Pks_int(res):
	counter=0
	for i in range(10):
		if (res[i][2]==True):
			counter=counter+1
	return(counter)

def Pss_int(res):
	counter=0
	for i in range(10):
		if (res[i][3]==True):
			counter=counter+1
	return(counter)

def Nes_int(res):
	counter=0
	for i in range(10):
		if (res[i][4]==True):
			counter=counter+1
	return(counter)

def new():
	b=inside()
	b=resList(b)
	eba(b)

def batching():
	name=input('имя ученика: ')
	b=inside()
	b=resList(b)
	print(name)
	eba(b)

def factoring(string):
	e=[]
	for i in range(len(string)):
		e.append(string[i])
	counter1=0
	counter2=0
	counter3=0
	counter4=0
	for i in range(len(factor1)):
		if(e[factor1[i]]==localFactor1[i]):
			counter1+=1
	for i in range(len(factor2)):
		if(e[factor2[i]]==localFactor2[i]):
			counter2+=1
	for i in range(len(factor3)):
		if(e[factor3[i]]==localFactor3[i]):
			counter3+=1
	for i in range(len(factor4)):
		if(e[factor4[i]]==localFactor4[i]):
			counter4+=1
	result ='\t'+str(counter1)+'\t'+str(counter2)+'\t'+str(counter3)+'\t'+str(counter4)
	return result
#result =Ситуатив. акт.:' Надсит. акт.: ' поступок: ' действие с людьми: '+str(counter4)

def eba(res):
	count=0
	count=count+PAs[Pas_int(res)]
	print('ПА',Pas_int(res),end=' // ')
	count=count+Ks[Ks_int(res)]
	print('K',Ks_int(res),end=' // ')
	count=count+PKs[Pks_int(res)]
	print('ПК',Pks_int(res),end=' // ')
	count=count+PSs[Pss_int(res)]
	print('ПС',Pss_int(res),end=' // ')
	#count=count+NEs[Nes_int(res)]
	print('Нэ',Nes_int(res),end=' // ')
	print('итого',tta[count+1],'(',count+1,')')

def eba_auto(res):
	count=0
	endString=''
	count=count+PAs[Pas_int(res)]
	endString=endString+str(PAs[Pas_int(res)])+'\t'
	count=count+Ks[Ks_int(res)]
	endString=endString+str(Ks[Ks_int(res)])+'\t'
	count=count+PKs[Pks_int(res)]
	endString=endString+str(PKs[Pks_int(res)])+'\t'
	count=count+PSs[Pss_int(res)]
	endString=endString+str(PSs[Pss_int(res)])+'\t'
	#count=count+NEs[Nes_int(res)]
	endString=endString+str(NEs[Nes_int(res)])+'\t'
	endString=endString+str(tta[count])
	return endString

print(' DONE ')

colonTitul='испытуемый'+'\t'+'ПА'+'\t'+'К'+'\t'+'ПК'+'\t'+'ПС'+'\t'+'НЭ'+'\t'+'итого'+'\t'+'ситуат'+'\t'+'наституат'+'\t'+'поступок'+'\t'+'действие с людьми'+'\t'
def set_file(inputFileName,outputFileName):
	f=open(inputFileName,'r')
	a=f.read()
	f.close()
	a=a.split('\n')
	for i in range(len(a)):
		a[i]=a[i].split('%')
	for i in range(len(a)):
		outerVal=inside_auto(a[i][1])
		outerVal=resList(outerVal)
		outerVal=eba_auto(outerVal)
		a[i].append(outerVal)
	del f
	for i in range(len(a)):
		nd = factoring(a[i][1])
		a[i].append(nd)
	f=open(outputFileName,'w')
	f.write(colonTitul)
	f.write('\n')
	for i in range(len(a)):
		f.write(str(a[i][0]))
		f.write(str('\t'))
		f.write(str(a[i][2]))
		f.write(str(a[i][3]))
		f.write('\n')
	f.close()

print('ALL DONE')
print('для нового опросника введите: new()')
print('для пакетной обработки вызовите функцию set_file()')
print('прятного использования')