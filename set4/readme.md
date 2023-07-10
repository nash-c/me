TODO: Reflect on what you learned this week and what is still unclear.

Data Audit (Data Set 1)
How many rows and columns? "1809 rows, 12 columns"
What does dataset explain? "The number of entries and exits for each station in NSW spanning from 2016-2019, then for February, May and September of 2020"
Why was it collected? "Just to keep track of it I guess"
Who paid for it? "Transport NSW"
Where did you get it from? "opendata.transport.nsw.gov.au"
Does it have a geographical component? "Yes, for sure"
Column stuff:
    Column 1: Year
        Describes the year
        Measured by looking at the year
        Categorical
    Column 2: Station
        Describes the station names --> also indicates station location
        Measured by looking at station names
        Categorical
    Column 3: Entries 6:00 to 10:00
        Describes the number of entries between 6am-10am
        Measured by recording how many people enter between 6am-10am
        Continuous
    Column 4: Exits 6:00 to 10:00
        Describes the number of exits between 6am-10am
        Measured by recording how many people exit between 6am-10am
        Continuous
    Column 5: Entries 10:00 to 15:00
        Describes the number of entries between 10am-3pm
        Measured by recording how many people enter between 10am-3pm
        Continuous
    Column 6: Exits 10:00 to 15:00
        Describes the number of exits between 10am-3pm
        Measured by recording how many people exit between 10am-3pm
        Continuous
    Column 7: Entries 15:00 to 19:00
        Describes the number of entries between 3pm-7pm
        Measured by recording how many people enter between 3pm-7pm
        Continuous
    Column 8: Exits 15:00 to 19:00
        Describes the number of exits between 3pm-7pm
        Measured by recording how many people exit between 3pm-7pm
        Continuous
    Column 9: Entries 19:00 to 6:00
        Describes the number of entries between 7pm-6am
        Measured by recording how many people enter between 7pm-6am
        Continuous
    Column 10: Exits 19:00 to 6:00
        Describes the number of exits between 7pm-6am
        Measured by recording how many people exit between 7pm-6am
        Continuous
    Column 11: Entries 24 hours
        Describes the total entries within the 24 hour period
        Measured by recording the total number of people who entered each respective station
        Continuous
    Column 12: Exits 24 hours
        Describes the total entries within the 24 hour period
        Measured by recording the total number of people who entered each respective station
        Continuous
    

Data Audit (Data Set 2)
How many rows and columns? "52717 rows, 4 columns"
What does dataset explain? "The number of entries and exits for each station in NSW spanning from each month from July 2016 to June 2023"
Why was it collected? "Just to keep track of it I guess"
Who paid for it? "Transport NSW"
Where did you get it from? "opendata.transport.nsw.gov.au"
Does it have a geographical component? "Yes, for sure"
Column stuff:
    Column 1: Month-Year
        Describes the month and year --> format = yyyy-mm
        Measured by looking at year and month
        Categorical
    Column 2: Station
        Describes the station name --> also indicates geographical location of station
        Measured by looking at all the stations
        Categorical
    Column 3: Entry_Exit
        Describes whether the data is a record of entries or exists --> maybe this could be a binary like 1 = entry, and 0 = exit??
        Not measured data --> more like a description for other data
        Categorical (boolean??)
    Column 4: Trip
        Describes the number of people who entered and exited for each station respectively
        Measured by determining how many people entered and exited a train station over a 24 hour period
        Continuous --> however some data is "Less than 50" --> so string??


go to github make repository --> give name --> clone that --> copy data introduction to repo, then pandas