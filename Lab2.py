"""
 Charlie Ang
 CSC 4800 Python Applications Programming
 Lab # 2
 Dr. Tindall
 January 12, 2017

 This program prompts the user to enter a 4-digit calendar year value and creates to an output
 file the calendar for the entire year in the for 'calendaryear.txt'
"""

def day_of_week(year):
    """
    This function takes in an input for year and it returns what day of the week the year starts in Jan
    :param year:
    :return dayOfWeek: 0 - 6 to correlate to Sunday - Saturday
    """

    dayOfWeek = 0   # 0(Sunday), 1(Monday), 2(Tuesday), 3(Wednesday), 4(Thursday), 5(Friday), 6(Saturday)
    dayOfWeek = ((year + int((year - 1) / 4) - int((year - 1) / 100) + int((year - 1) / 400)) % 7)  # January 1 in year begins on day
    return dayOfWeek


def is_leap_year(year):
    """
    This function takes in an input for year and it returns whether that year is a leap year or not.
    :param year:
    :return leapYear: true if leap year, false otherwise
    """

    leapYear = True                                                            # boolean variable to see if leap year or not
    # leap year if year is divisible by 4 and not by 100 or year is divisible by 400
    if (((year % 4) == 0) & ((year % 100) != 0)) | ((year % 400) == 0):
        return leapYear
    else:
        leapYear = False
        return leapYear


def main():
    """
    Prompts user to enter a 4-digit year value. It then determines the start day of week for month of January
    as well as whether the year is a leap year or not. The calendar for that year is then outputted to an output
    file with one month per line.
    :return:
    """

    print('Welcome to the Calendar for a Year generator.')
    try:
        year = int(input('Please enter a 4-digit year: '))                      # stores user input for year in 'year' variable
        if not (999 < year < 10000):                                            # year must be 4 digit value
            print('Invalid range! Please enter a valid 4-digit-value year.')
            return None
    except:
        print('Invalid input! Please try again.')                               # not an integer input
        return None

    startDayOfWeek = day_of_week(year)                                          # day of week year starts
    leapYear = is_leap_year(year)                                               # true if leap year, false otherwise

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    daysEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]            # days of each month if not leap year
    daysEachMonthLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # days of each month in leap year

    outputFileName = "calendar{}.txt".format(year)
    with open(outputFileName, "w") as myfile:                                   # open output file to write to; automatically closes file at end
        if leapYear == False:                                                       # use daysEachMonth list instead of daysEachMontLeapYear list
            curDayOfWeek = startDayOfWeek                                           # variable to keep track of current day of week
            for i in range(0, 12):                                                  # outer loop to increment through all the months
                print('       {0} {1}'.format(months[i], year), file=myfile)
                print(' Sun Mon Tue Wed Thu Fri Sat', file=myfile)

                for h in range(0, curDayOfWeek):                                    # print correct number of spaces to account for start day in Jan                                                     # only print spaces for Jan
                    print('    ', end='', file=myfile)

                for j in range(1, daysEachMonth[i] + 1):                            # outputting number of days in the month
                    if(curDayOfWeek <= 5):
                        print('{0:4d}'.format(j), end='', file=myfile)
                        curDayOfWeek = curDayOfWeek + 1
                    else: # day 6
                        curDayOfWeek = 0                                            # next date should be on new row
                        print('{0:4d}'.format(j), file=myfile)
                print('', file=myfile)
                print('', file=myfile)
        else:                                                                       # this is a leap year so there should be Feb. 29
            curDayOfWeek = startDayOfWeek                                           # variable to keep track of current day of week
            for i in range(0, 12):                                                  # outer loop to increment through all the months
                print('       {0} {1}'.format(months[i], year), file=myfile)
                print(' Sun Mon Tue Wed Thu Fri Sat', file=myfile)

                for h in range(0, curDayOfWeek):                                    # print correct number of spaces to account for start day in Jan                                                     # only print spaces for Jan
                    print('    ', end='', file=myfile)

                for j in range(1, daysEachMonthLeapYear[i] + 1):                    # outputting number of days in the month
                    if(curDayOfWeek <= 5):
                        print('{0:4d}'.format(j), end='', file=myfile)
                        curDayOfWeek = curDayOfWeek + 1
                    else: # day 6
                        curDayOfWeek = 0
                        print('{0:4d}'.format(j), file=myfile)
                print('', file=myfile)
                print('', file=myfile)


if __name__ == '__main__':
        main()