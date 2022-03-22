
beginHours = int(input("Begin Time-Hours : " ))
beginMin = int(input("Begin Time-minutes : "))
minToAdd = int(input("Time elapsed in minutes : "))

# converting the time elapsed to hours and minutes
hrsAddTime = minToAdd//60
minAddTime = minToAdd % 60

#adding hours and minutes to the begin time
endHours = beginHours + hrsAddTime
endMin = beginMin + minAddTime

#if new time minutes exceeds 60 minutes, add to the hours
if endMin >= 60 :
    endHours += endMin // 60
    endMin = endMin % 60
    if endMin == 0 :
        endMin = "00"

#if end time hours exceeds 24 hrs, then take the remainder as end time hours 
if endHours >= 24 :
    endHours %= 24

if endHours > 12 :
    endHours -= 12
    Meridian = "PM"
else :
    Meridian = "AM"

print(f'Time after {minToAdd} minutes is : [{endHours}:{endMin} {Meridian}]')