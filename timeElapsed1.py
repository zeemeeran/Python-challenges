beginHours = int(input("Begin Time-Hours : " ))
beginMin = int(input("Begin Time-minutes : "))
beginMeridian = input("Begin time AM/PM : ")
endHours = int(input("End time-hours : "))
endMin = int(input("End tim-min : "))
endMeridian = input("End time AM/PM: ")


if endMeridian.upper() == 'PM' :
    endHours += 12

if beginMeridian.upper() == 'PM' :
    beginHours += 12

endTime = endHours * 60 + endMin
beginTime = beginHours * 60 + beginMin 

timeElapsed = endTime - beginTime    


print(f'Time elapsed between {beginHours}:{beginMin} {beginMeridian} & {endHours}:{endMin} {endMeridian} is : {timeElapsed} minutes!!')