#Expectations:
# 1 - no errors are thrown when unexpected input is entered.
# 2 - Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
# 3 - Docstrings, comments, and variable names enable readability of the code. --> explan
# 4 - Functions are used to reduce repetitive code. --> no repetetive tasks
# 5 - Packages are used to carry out advanced tasks. --> import os
# 6 - Loops and conditional statements are used to process the data correctly. --> while
# 7 - Descriptive statistics are correctly computed and used to answer the questions posed about the data. --> mean, mode, count


import time
import datetime
import pandas as pd
import numpy as np
import os #for convenient path handling

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
    while(42):
        print('\nWould you like to see data for Chicago, New York City, or Washington?')
        city = str(input("\nEnter city name: ")).lower()
        if city in ['chicago', 'new york city', 'washington']:

            # TO DO: get user input for month (all, january, february, ... , june)
            print('\nWould you like to filter the data by month, or not at all? - Please Enter January, February, March, May, April, June, July, or All')
            month = str(input("\nEnter month name: ")).lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:

                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                print('\nWould you like to filter the data by day, or not at all? - Please Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All')
                day = str(input("\nEnter day name: ")).lower()
                if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                    print('\nThanks for entering valid inputs')         
                    break

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
    #CITY_DATA = { 'chicago': 'chicago.csv',
    #          'new york city': 'new_york_city.csv',
    #          'washington': 'washington.csv' }

    # load data file into a dataframe
    while(42):
        try:
            filename=CITY_DATA[city] #get filename with filetype out of the dictionary
            pathname=input('Please enter the path, where the corresponding .csv-files are. \nThey should be named "some-city-name.csv"') #ask user to have him deliver the path, where the corresponding .csv-files are
            file_and_pathname = os.path.join(pathname, filename) #join the filename and pathname
            df = pd.read_csv(file_and_pathname) #load csv file into a panda data frame
            break
        except:
            print('Mhm, the path you entered does not have any valid files in there, please double check your entry.')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1 #since index starts with 0 and month in datetime format starts with 1
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print( 'Most common month: {}'.format( months[df.groupby( ['month'])['month'].count().idxmax() -1]).title() )

    # TO DO: display the most common day of week
    print('Most common day of week: {}'.format(df.groupby(['day_of_week'])['day_of_week'].count().idxmax()))

    # TO DO: display the most common start hour
    df['hour'] =  df['Start Time'].dt.hour
    print('Most common start hour: {}'.format(df.groupby(['hour'])['hour'].count().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: {}'.format(df.groupby('Start Station')['Start Station'].count().idxmax()))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df.groupby('End Station')['End Station'].count().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    df['StartEnd'] = 'From "' + df['Start Station'] + '" to "' + df['End Station'] + '"'

    print('Most frequent combination of start station and end station trip: {}'.format(df.groupby('StartEnd')['StartEnd'].count().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print( 'Total travel time in Days, Hours, Minutes, Seconds: {}'.format( pd.to_timedelta(df['Trip Duration'].sum(), unit='s') ) )

    # TO DO: display mean travel time
    print( 'Mean travel time in Days, Hours, Minutes, Seconds: {}'.format( pd.to_timedelta(df['Trip Duration'].mean(), unit='s') ) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby('User Type')['User Type'].count())
    print("\n")

    # TO DO: Display counts of gender
    if 'Gender' in list(df.columns.values):
        print(df.groupby('Gender')['Gender'].count())
        print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df.columns.values):
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('Most common year of birth: {}'.format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        more = ''
        lines = 0
        while(42):
            user_wants_data = input('\nWould you like to see 5 {}lines of raw data, before getting into statistis of the data? Enter yes or no.'.format(more))
            if user_wants_data.lower().title() == 'Yes':
                more = 'more '
                lines += 5
                print(df.head(lines))
                print('\n')
            elif user_wants_data.lower().title() == 'No':
                more = ''
                lines = 0
                break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you for using this software, see you next time.')
            break

if __name__ == "__main__": #this is being executed, when we execute the script directly, but if we import the script, it is not being executed.
	main() #run the main function, whenever the file bikeshare.py is started, but only do