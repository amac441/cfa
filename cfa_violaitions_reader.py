#Write a brief program in the language of your choice to summarize a simple dataset. 
#This is a comma-delimited data file representing building code violations: 

#http://forever.codeforamerica.org/fellowship-2015-tech-interview/Violations-2012.csv

#Your program should calculate the number of violations in each category, 
#and the earliest and latest violation date for each category. 
#You can use your preferred programming language, and decide on the presentation format of the resulting data.

import csv
from datetime import datetime
import urllib2


stats={}
file='http://forever.codeforamerica.org/fellowship-2015-tech-interview/Violations-2012.csv'
csvfile = urllib2.urlopen(file)

#with open(response, 'rb') as csvfile:
data = csv.reader(csvfile)
headers = data.next()
#violation_id	inspection_id	violation_category	violation_date	violation_date_closed	violation_type
for row in data:
    vCat=row[2]
    #date format 1/3/2012 0:00
    vDate=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')
    if vCat in stats.keys():
        stats[vCat]['count']+=1
        if stats[vCat]['earliest']>vDate:
            stats[vCat]['earliest']=vDate
            stats[vCat]['earlyData']=row
        if stats[vCat]['latest']<vDate:
            stats[vCat]['latest']=vDate
            stats[vCat]['lateData']=row
    else:
        stats[vCat]={'count':0,'earliest':vDate,'latest':vDate,'earlyData':row,'lateData':row}

dashes='============='
print dashes +' PRINTING VIOLAITON STATISTICS ' + dashes
print '--Column Headers: ' + " ".join(headers)
for cat in stats:
    print dashes + 'Violoation Category: ' + cat + dashes
    print '-Count: '+str(stats[cat]['count'])
    print '-Earliest:'
    print " ".join(stats[cat]['earlyData'])
    print '-Most Recent:'
    print " ".join(stats[cat]['lateData'])

print dashes + dashes
    
