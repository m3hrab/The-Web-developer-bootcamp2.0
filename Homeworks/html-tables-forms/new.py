month_dictionary = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

day_dictionary = {
    0:"Saturday",
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday"
}

#write a function here which will take day,month,year as arguments and returns day of the week (like. Tuesday)



def dayofweek(day, month, year):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    year -= month < 3
    return (( year + int(year / 4) - int(year / 100)
             + int(year / 400) + t[month - 1] + day) % 7)
 
# Driver Code
day = dayofweek(28, 8, 2010)
print(day)
 
#take inputs from console and call the above function from here






