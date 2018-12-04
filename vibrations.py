#Problem Statement: Longitudinal vibrations of a spring mass damper system

#import matplotlib.pyplot as plt

#inputs

weightofpan=0.8948

noinp=eval(input("enter the number of masses: "))
readings=list()
timefree=list()
timedamp=list()
totalmass=list()

timef=list()
timed=list()
naturalfreq=list()
dampedfreq=list()
naturalcircfreq=list()
dampedcircfreq=list()

dampingratio=list()

criticaldampcoeff=list()
dampingcoeff=list()

logdec=list()

print("enter",noinp," masses")
for i in range(noinp):
	readings.append(eval(input("")))

print("enter",noinp,"time for 3 free oscillations")
for i in range(noinp):
	timefree.append(eval(input("")))
	
print("enter",noinp,"time for 3 damped oscillations")
for i in range(noinp):
	timedamp.append(eval(input("")))

#total mass calculation
for i in range(noinp):
	totalmass.append(weightofpan+readings[i])

for j in range(noinp):
	a=(timefree[j])/3.0
	timef.append(a)
	b=1/timef[j]
	naturalfreq.append(b)
	d=naturalfreq[j]
	c=2.0*3.142*d
	naturalcircfreq.append(c)
	

for j in range(noinp):
	a=(timedamp[j])/3.0
	timed.append(a)
	b=1/timed[j]
	dampedfreq.append(b)
	d=dampedfreq[j]
	c=2.0*3.142*d
	dampedcircfreq.append(c)
	

for i in range(noinp):
	e=(dampedcircfreq[i]/naturalcircfreq[i])**2
	f=1-e
	g=f**0.5
	dampingratio.append(g)
	

#to calculate critical damping coefficient nAND damping coefficient
for i in range(noinp):
	h=2.0*totalmass[i]*naturalcircfreq[i]
	criticaldampcoeff.append(h)
	k=dampingratio[i]*criticaldampcoeff[i]
	dampingcoeff.append(k)
	

#to calculate logarithmic decreement

for i in range(noinp):
	
	l=(1-(dampingratio[i]**2))**0.5
	m=2.0*3.142*dampingratio[i]/l
	logdec.append(m)

print("Natural frequency\t damped frequency\t damping ratio\t     criticaldampingcoefficient\t dampingcoefficient\t logarithmicdecrement")

for i in range(noinp):
	print(naturalcircfreq[i],"\t",dampedcircfreq[i],"\t",dampingratio[i],"\t",criticaldampcoeff[i],"\t",dampingcoeff[i],"\t",logdec[i])

#graph
#plt.plot(naturalcircfreq,timefree)
#plt.show()
	
