import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ["chicago","new york city","washington"]  
month_list = ["all","january","february","march","april","may","june"]
day_list = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]         
raw_data_list1 = ["yes"]
raw_data_list2 = ["no"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    #DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
            city = str(input("Do you want to analyze Chicago, New York City, or Washington? ")).lower().strip()
            if city in city_list:
                break
            else:
                print("\nThis is not a valid entry. Please enter an appropriate city - your choices are Chicago, New York City, or Washington \n")
      
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
            month = str(input("\nWhich month do you want to filter for? (Type 'all' if not required) ")).lower().strip()
            if month in month_list:
                break
            else:
                print("\nThis is not a valid entry. Please enter an appropriate month")
     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
            day = str(input("\nWhich day of the week do you want to filter for? (Type 'all' if not required) ")).lower().strip()
            if day in day_list:
                break
            else:
                print("\nThis is not a valid entry. Please enter an appropriate day of the week")
                
    print('-'*40)
    print("\nYou have entered: \n{} \n{} \n{} \n".format(city, month, day))
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
    
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    
    print("Most common month:", common_month)
    
    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    
    print("Most common day of the week:", common_day)
    
    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    
    print("Most common start time:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    
    print("Most common start station:", common_start_station)
    
    
    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    
    print("Most common end station:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Common Combination'] = df['Start Station'] + ' to '  + df['End Station']
    
    common_combination = df['Common Combination'].mode()[0]
    
    print("Most common combination of start and end station:", common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Trip Duration'] = df['Trip Duration'] /60
    
    total_time = df['Trip Duration'].sum()
    
    print("Total travel time:", total_time,"minutes")
    
    # TO DO: display mean travel time

    average_time = df['Trip Duration'].mean()
    
    print("Total travel time:", average_time,"minutes")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("Number of subscribers and one-off customers:")
    print(user_types)
    
    # TO DO: Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender_count:\n ', gender_count)
    except KeyError:
        print('\nGender data is not available')

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest year of birth:\n ', int(earliest_year))
        
        most_recent_year = df['Birth Year'].max()
        print('\nMost recent year of birth:\n ', int(most_recent_year))
        
        most_common_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth:\n ', int(most_common_year))
        
    except KeyError:
        print('\nBirth Year data is not available')
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    while True:
        raw_data = str(input("\nWould you like to view start / continue looking at lines of the raw data? (Yes/No) ")).lower().strip()
        if raw_data in ("yes"):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input("Would you like to see more raw data? (Yes/No) ").lower()
                if more_data not in ("yes"):
                    break 
        elif raw_data in ("no"):                        
            print("\nNo further view of raw data requested")                            
            break
        else:
            print("\nNot a valid entry - please type 'Yes' or 'No'")
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
