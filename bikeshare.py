"""
Created on Fri Nov 15 12:50:20 2019

@author: duaalkhiary
"""
import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months=['all','january','february','march','april','may','june']

Days=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """ 
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Choose a city to explore : Chicago , New York City, or Washington:\n')
        if city.lower() not in CITY_DATA.keys():
            print('You should enter a valid city')
        else:
            city=city.lower()
            break
    print("You chose {}".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Which month do you want to filter by? January, February, March, April, May, June, or All?\n')
        if month.lower() not in Months:
            print("you should enter a valid month")
        else: 
            month=month.lower()
            break
    print("Filtering by {}".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =input('Which day of the week do you want to filter by? please type the day:\n')
        if day.lower() not in Days:
            print ("You should enter a valid day")
        else:
            break
    print("Filtering by {}".format(day.title()))
    print ('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
    if month!='all':
        month=Months.index(month)
        df=df[df['month']==month]

    if day!='all':
        df=df[df['day_of_week']==day.title()]
              
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is:\n", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day is:\n", df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    print("The most common hour is:\n", df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most popular start station is:\n", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most popular end station is:\n", df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    # freq_trip=df.groupby(['Start Station','End Station'])
    # s=freq_trip['Start Station']
    # e=freq_trip['End Station']
    # print("Most frequent combination of start station and end station trip is:\n Start station:{}\n End station:{}".format(s,e))
    print("Most frequent combination of start station and end station trip is:\n",
          df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:\n", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time is:\n", df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts=df['User Type'].value_counts()
    print("Counts of user types :\n{}".format(counts))

    if city == 'washington':
        print("\nThere's no Gender or Birth data for the city you selected.")
    else:
        # TO DO: Display counts of gender
        gender=df['Gender'].value_counts()
        print("\nCounts of gender:\n{}".format(gender))
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earliest birth year is:\n", df['Birth Year'].min())
        
        print("\nThe most recent birth year is:\n", df['Birth Year'].max())
        
        print("\nThe most common birth year is :\n", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """
    Show raw data as requested by user.
    """
    s, e = 0, 5

    display = input("Do you want to see the raw data?: ").lower()

    if display == 'yes':
        while e <= df.shape[0] - 1:
            print(df.iloc[s:e,:])
            s += 5
            e += 5
            end = input("Do you wish to continue? ").lower()
            if end == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()