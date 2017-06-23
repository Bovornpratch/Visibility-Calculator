#/usr/bin/env python

import datetime
import ephem
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy
import sys

def DateObject(date,time):
    datearr = date.split('-')
    timearr = time.split(':')
    datearr,timearr =numpy.array(datearr,dtype=int),numpy.array(timearr,dtype=int)
    DTOB = datetime.datetime(datearr[0],datearr[1],datearr[2],timearr[0],timearr[1],timearr[2])
    return DTOB

def GetTimeRange(present,rim):  # function to get a time array from an inputed time and +- limit

    edge = datetime.timedelta(hours=rim)
    step = datetime.timedelta(minutes=5)
    start , end =  (present - edge) , (present + edge)

    result = []
    while start < end:

        result.append(start.strftime('%Y-%m-%d %H:%M:%S'))
        start += step

    return result

def Visibility(time,window,SRA,SDEC,latitude,longitude,elev):  #function to calculate the RA/DEC/AZI/ALTITUDE of an object
    Time_arr = GetTimeRange(Now,window)

    observer = ephem.Observer()
    star = ephem.FixedBody()

    star._ra,star._dec = SRA,SDEC
    observer.lat,observer.lon, observer.elevation = latitude,longitude,elev

    T_OUT,CO1_OUT,CO2_OUT = [],[],[]
    for i in range(0,len(Time_arr)):

        observer.date = Time_arr[i]
        star.compute(observer)

        CO1_OUT.append(float(star.az))
        CO2_OUT.append(float(star.alt))

        T_OUT.append(datetime.datetime.strptime(Time_arr[i],'%Y-%m-%d %H:%M:%S'))

    T_OUT = numpy.array(T_OUT)
    CO1_OUT = numpy.array(CO1_OUT)
    CO2_OUT = numpy.array(CO2_OUT)
    return T_OUT,CO1_OUT*180/3.14,CO2_OUT*180/3.14


def MoonVis(time,window,latitude,longitude,elev):
    Time_arr = GetTimeRange(Now,window)

    observer = ephem.Observer()
    moon = ephem.Moon()
    observer.lat,observer.lon ,observer.elevation= latitude,longitude,elev
    T_OUT,CO1_OUT,CO2_OUT = [],[],[]
    for i in range(0,len(Time_arr)):

        observer.date = Time_arr[i]
        moon.compute(observer)

        CO1_OUT.append(float(moon.az))
        CO2_OUT.append(float(moon.alt))

        T_OUT.append(datetime.datetime.strptime(Time_arr[i],'%Y-%m-%d %H:%M:%S'))

    T_OUT = numpy.array(T_OUT)
    CO1_OUT = numpy.array(CO1_OUT)
    CO2_OUT = numpy.array(CO2_OUT)
    return T_OUT,CO1_OUT*180/3.14,CO2_OUT*180/3.14

def Plot_Current():
    UTC = datetime.datetime.utcnow()
    local = datetime.datetime.now()
    TZ = local - UTC

    plt.axvline(matplotlib.dates.date2num(datetime.datetime.now()-TZ),color='red')

def PlotVis(x,y,label,color): #plots visibility
    fig, ax = plt.subplots(1)
    hfmt = matplotlib.dates.DateFormatter('%m/%d %H:%M')
    plt.ylim(-30,95)
    ax.xaxis.set_major_formatter(hfmt)
    plt.gca().set_yticks(numpy.linspace(-30,90,9,endpoint=True))
    plt.axhline(0,color='black')
    fig.autofmt_xdate()
    #plt.ylim(-30,95)
    plt.xlabel('UTC')
    plt.ylabel('Alt (Deg)')

    for i in range(0,len(x)):
        #print x[i]
        x_arr = matplotlib.dates.date2num(x[i])
        ax.plot_date(x_arr,y[i],'b-',color = color[i],label=label[i])
    plt.legend()

def Printer(t,x,y,name):
    head = 'Date'+'\t'+'Time'+'\t'+'Azimuth'+'\t'+'ALTITUDE'
    out=numpy.stack((t,x,y),axis=-1)
    numpy.savetxt(str(name)+'Visibility.txt',out,fmt='%s',header=head)
#########################################################################################################3

# for User input values uncomment this block

Date,Time = str(sys.argv[1]), str(sys.argv[2])
star_RA ,star_DEC = str(sys.argv[3]),str(sys.argv[4])  #test Star Coordinates  (Vega)
Obs_Lat, Obs_Long =  str(sys.argv[5]),str(sys.argv[6]) # Observatory latitude,longitude
elevation = float(sys.argv[7])

if Date == 'SYST' or Time == 'SYST':
    print 'Using System Time and Date'
    Now = datetime.datetime.now()
else:
    print 'Using user determined Time and Date'
    Now = DateObject(Date,Time)
print  Now

'''
#Example/test coordinate

#Now = datetime.datetime.now()
star_RA ,star_DEC = '18:36:56.48','+38:47:07.3'  #test Star Coordinates  (Vega)
star_RA ,star_DEC = '6:00:00','+23:00:00'  #test Star Coordinates  (Sun, summer solstice)

Obs_Lat, Obs_Long = '18:47:25.08' , '98:58:54.11'  # Observatory latitude,longitude
elevation = 0
'''



######## Calcuations



Tarr,CORD1,CORD2 = Visibility(Now,12,star_RA,star_DEC,Obs_Lat,Obs_Long,elevation)
TM,MoonC1,MoonC2 = MoonVis(Now,12,Obs_Lat,Obs_Long,elevation)

for i in range(0,len(Tarr)):
    print Tarr[i] , CORD2[i] , MoonC2[i]
    #pass
