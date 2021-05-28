import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    check = True
    while check:
        city = input("Please Enter one of these Cities (chicago, new york, washington): ")
        print()
        if city == "chicago":
            check = False
        elif city == "new york":
            city = "new york city"
            check = False
        elif city == "new york city":
            check = False
        elif city == "washington":
            check = False

    # TO DO: get user input for month (all, january, february, ... , june)
    check = True
    while check:
        month = input("Please Enter The Month(january, february, ... , june): ")
        print()
        if month == "january":
            check = False
        elif month == "all":
            check = False
        elif month == "february":
            check = False
        elif month == "march":
            check = False
        elif month == "april":
            check = False
        elif month == "may":
            check = False
        elif month == "june":
            check = False

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    check = True
    while check:
            day = input("Please Enter The Day(monday, tuesday, ... sunday): ")
            print()
            if day == "monday":
                check = False
            elif day == "all":
                check = False
            elif day == "tuesday":
                check = False
            elif day == "Wednesday":
                check = False
            elif day == "Thursday":
                check = False
            elif day == "Friday":
                check = False
            elif day == "Saturday":
                check = False
            elif day == "sunday":
                check = False
           

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    
    months = ['indexPLUS', 'january', 'february', 'march', 'april', 'may', 'june']
    # check what he was his choice
    # the if statement here to know that he is not put all and we want to filter
    if month != "all": 
        month = months.index(month)
        print(month)
        df = df[df['Month'] == month]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
            
    return df

    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month: {}\n'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most Common Day: {}\n'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common Start Hour: {}\n'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station: {}\n'.format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most common End Station: {}\n'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' -> ' + df['End Station']
    most_common_combination_station = df['combination'].mode()[0]
    print('Most common Combination Station: {}\n'.format(most_common_combination_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
   
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {}\n'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count = df['User Type'].value_counts()
    print('the counts of User Type:\n{}\n'.format(count))
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('the counts of Gender:\n{}\n'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    min_birth = int(df['Birth Year'].min())
    max_birth = int(df['Birth Year'].max())
    most_common_year_birth = int(df['Birth Year'].mode()[0])
    print('earliest, most recent, and most common year of birth:-\nearliest: {}\nmost recent: {}\nmost common: {}\n'.format(min_birth, max_birth, most_common_year_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        head = input('\nWould you like to see the first five rows? Enter yes or no.\n')
        if head.lower() == 'yes':
            print(df.head())
            nextHead = input('\nWould you like to see the next five rows? Enter yes or no.\n')
            if nextHead == 'yes':
                for i in range(4,len(df.index),5):
                    print(i)
                    print(df.iloc[i:(i+5)])
                    nextHeadd = input('\nWould you like to see the next five rows? Enter yes or no.\n')
                    if nextHeadd.lower() != 'yes':
                        break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
