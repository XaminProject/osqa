#################################################################
#!/usr/bin/env python
##   jDate.py  (5/11/1390)
##
##   Copyright (C) 2011 dotpy.ir
##   jelodari iraj (iraj.jelo@gmail.com)
##   
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2, or (at your option)
##   any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
## 
#################################################################
import calendar
import datetime
import time
today =  datetime.date.today()
global iMiladiYear
global iMiladiMonth
global iMiladiDay
iMiladiYear = today.year
iMiladiMonth = today.month
iMiladiDay = today.day
#dayOfYear = time.localtime()[-2]   #  time.strftime("%j")

sumDayMiladiMonth = [0,31,59,90,120,151,181,212,243,273,304,334]
sumDayMiladiMonthLeap=[0,31,60,91,121,152,182,213,244,274,305,335]

def persianDayWeek():
    nameDay =time.strftime("%A")

    if nameDay =='Saturday':
        return u'Shanbeh'
    if nameDay =='Sunday':
        return u'Yekshanbeh'
    if nameDay =='Monday':
        return u'Doshanbeh'
    if nameDay =='Tuesday':
        return u'seshanbe'
    if nameDay =='Wednesday':
        return u'Chaharshanbeh'
    if nameDay =='Thursday':
        return u'Panjshanbeh'
    if nameDay =='Friday':
        return u'Jomeh'
    
def miladi2shamsi(iMiladiMonth,iMiladiDay, iMiladiYear,):
    farvardinDayDiff=79
    if calendar.isleap(iMiladiYear):
        dayCount = sumDayMiladiMonthLeap[iMiladiMonth-1] + iMiladiDay
    else:
        dayCount = sumDayMiladiMonth[iMiladiMonth-1] + iMiladiDay
    if calendar.isleap(iMiladiYear - 1):
        deyDayDiff = 11
    else:
        deyDayDiff = 10
    if (dayCount > farvardinDayDiff):
        dayCount = dayCount - farvardinDayDiff
        if (dayCount <= 186):
            if  dayCount%31 == 0:
                shamsiMonth = dayCount / 31
                shamsiDay = 31
            else:
                shamsiMonth = (dayCount / 31) + 1
                shamsiDay = (dayCount%31)
            shamsiYear = iMiladiYear - 621
        else:
            dayCount = dayCount - 186
            if  dayCount%30 == 0:
                shamsiMonth = (dayCount / 30) + 6
                shamsiDay = 30
            else:
                shamsiMonth = (dayCount / 30) + 7
                shamsiDay = (dayCount%30)
            shamsiYear = iMiladiYear - 621
    else:
        dayCount = dayCount + deyDayDiff
        if dayCount%30 == 0:
            shamsiMonth = (dayCount / 30) + 9
            shamsiDay = 30
        else:
            shamsiMonth = (dayCount / 30) + 10
            shamsiDay = (dayCount%30)
        shamsiYear = iMiladiYear - 622
    return '%d/%d/%d'%(shamsiYear,shamsiMonth,shamsiDay)
def today2shamsi():
    iMiladiMonth
    iMiladiDay
    iMiladiYear
    farvardinDayDiff=79
    if calendar.isleap(iMiladiYear):
        dayCount = sumDayMiladiMonthLeap[iMiladiMonth-1] + iMiladiDay
    else:
        dayCount = sumDayMiladiMonth[iMiladiMonth-1] + iMiladiDay
    if calendar.isleap(iMiladiYear - 1):
        deyDayDiff = 11
    else:
        deyDayDiff = 10
    if (dayCount > farvardinDayDiff):
        dayCount = dayCount - farvardinDayDiff
        if (dayCount <= 186):
            if  dayCount%31 == 0:
                shamsiMonth = dayCount / 31
                shamsiDay = 31
            else:
                shamsiMonth = (dayCount / 31) + 1
                shamsiDay = (dayCount%31)
            shamsiYear = iMiladiYear - 621
        else:
            dayCount = dayCount - 186
            if  dayCount%30 == 0:
                shamsiMonth = (dayCount / 30) + 6
                shamsiDay = 30
            else:
                shamsiMonth = (dayCount / 30) + 7
                shamsiDay = (dayCount%30)
            shamsiYear = iMiladiYear - 621
    else:
        dayCount = dayCount + deyDayDiff
        if dayCount%30 == 0:
            shamsiMonth = (dayCount / 30) + 9
            shamsiDay = 30
        else:
            shamsiMonth = (dayCount / 30) + 10
            shamsiDay = (dayCount%30)
        shamsiYear = iMiladiYear - 622
    return [shamsiMonth,shamsiDay,shamsiYear]
def fullDate():
    return '%s-%s-%s %s'%(today2shamsi()[1],today2shamsi()[0], today2shamsi()[2], persianDayWeek())
def persianNameMonth():
    Month =today2shamsi()[0]
    if Month ==1:
        return u'Farvardin'
    if Month ==2:
        return u'Ordibehesht'
    if Month ==3:
        return u'Khordad'
    if Month ==4:
        return u'Tir'
    if Month ==5:
        return u'Mordad'
    if Month ==6:
        return u'Shahrivar'
    if Month ==7:
        return u'Mehr'
    if Month ==8:
        return u'Aban'
    if Month ==9:
        return u'Azar'
    if Month ==10:
        return u'Dey'
    if Month ==11:
        return u'Bahman'
    if Month ==12:
        return u'Esfand'
def shamsi2miladi( ShamsiMonth, ShamsiDay, ShamsiYear):

    farvardin1st =['iYear','iMonth','iDay']
    miladiDate =['iYear','iMonth','iDay']
    global i
    global dayCount

    miladiMonth  =  [30,31,30,31,31,30,31,30,31,31,28,31]
    
    miladiYear = ShamsiYear + 621;
    # Detemining the Farvardin the First

    if calendar.isleap(miladiYear):
        # this is a Miladi leap year so Shamsi is leap too so the 1st of Farvardin is March 20 (3/20)
        farvardin1st[1] = 3; # iMonth
        farvardin1st[2]= 20; # iDay
        marchDayDiff = 12;
    else:
        # this is not a Miladi leap year so Shamsi is not leap too so the 1st of Farvardin is March 21 (3/21)
        farvardin1st[1] = 3
        farvardin1st[2] =21
        marchDayDiff = 11
    
     #If next year is leap we will add one day to Feb.
    if calendar.isleap(miladiYear+1):
        miladiMonth[10] = miladiMonth[10] + 1; #Adding one day to Feb
    
    #Calculate the day count for input shamsi date from 1st Farvadin

    if ShamsiMonth >= 1 and  ShamsiMonth <= 6 :
        dayCount = ((ShamsiMonth-1) * 31) + ShamsiDay;
    else:
        dayCount =(6 * 31) + ((ShamsiMonth - 7) * 30) + ShamsiDay;

    #Finding the correspond miladi month and day

    if dayCount <= marchDayDiff: # So we are in 20(for leap year) or 21for none leap year) to 31 march
         miladiDate[2] = dayCount + (31 - marchDayDiff);
         miladiDate[1] = 3;
         miladiDate[0] = miladiYear;
    else :
         remainDay = dayCount - marchDayDiff;


    i = 0; #starting from April

    while remainDay > miladiMonth[i]:
        remainDay = remainDay - miladiMonth[i];
        i = i+1

    miladiDate[2] = remainDay;

    if i > 8: # We are in the next Miladi Year

        miladiDate[1] = i - 8;
        miladiDate[0] =  miladiYear + 1;

    else:
        miladiDate[1] = i + 4;
        miladiDate[0] =  miladiYear;

    return miladiDate;
####################### Example  #############################
#print '5/11/1390 ', miladi2shamsi(1,25,2012)
#print '19/11/1386 ', miladi2shamsi(2,8,2008)
#print miladi2shamsi(today.month,today.day,today.year)
#print fullDate()
#print 'brithday jelodari iraj: ', shamsi2miladi(11,21,1367)
#print '29/1/1391 = 2012/17/4 ', shamsi2miladi(1,29,1391)
###################### Example  ###############################
