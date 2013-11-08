def dayerizor(day):
    daynum = []
    i = 0
    for x in day:
	x = day[i]
	if x == "monday":
	    daynum.append(0)
	elif x == "tuesday":
	    daynum.append(1)
	elif x == "wednesday":
	    daynum.append(2)
	elif x == "thursday":
	    daynum.append(3)
	elif x == "friday":
	    daynum.append(4)
	elif x == "saturday":
	    daynum.append(5)
	elif x == "sunday":
	    daynum.append(6)
	i = i + 1
    daynum.sort()
    i = 0
    day = []
    for x in daynum:
	x = daynum[i]
	if x == 0:
	    day.append("monday")
	if x == 1:
	    day.append("tuesday")
	if x == 2:
	    day.append("wednesday")
	if x == 3:
	    day.append("thursday")
	if x == 4:
	    day.append("friday")
	if x == 5:
	    day.append("saturday")
	if x == 6:
	    day.append("sunday")
	i = i + 1	

	 
    return day

