import time as tm

first=tm.time()

suming=0
for i in range(1,110):
   suming+=i
   print(suming)
   
last=tm.time()
timetaken=last-first
print(timetaken)

#here in this program we are using the time library with one of its many functions called time.here, this time function is used to calculate the time we USED while our program of summing the numbErs in the range 1-110 was performing its task.... to reccord that time spent we setted the start time with "first=tm.time()" minus the ending time  "last=tm.time()" to get that used time spent while performing the task