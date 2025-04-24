def yearly_screen_time(avg_hours):
    """
    Function calcultating yearly screentime in days from avg hours of use
    """
    days_per_year = int(avg_hours * 365 / 24)
    months, days = divmod(days_per_year, 30)
    if months != 0:
        print(f"That makes a total of {months} months and {days} days per year")
    else:
        print(f"That makes a total of {days_per_year} days per year")

def life_expectancy():
    """
    Function calculates life expectancy based on current age and gender
    """
    age = int(input("What is your age:"))
    gender = input("What is your gender, 'm' for male, 'f' for female: ").lower()

    if gender == 'm':
        life_exp = 75 - age
        print("According to recent statistics(*) average life expectancy for men is 75")
        print(f"So you are expected to live for another{life_exp} years")
        print("\n")
        return life_exp

    else:
        life_exp = 82 - age
        print("According to recent statistics(*) average life expectancy for women is 82")
        print(f"So you are expected to live for another {life_exp} years")
        print("\n")
        return life_exp

def lifetime_screentime(avg_hours, life_exp):
    """
    Function calculates lifetime screentime based on life expectancy and avg hours of screentime
    """
    life_hours = avg_hours * 365 * life_exp
    life_days = round(life_hours / 24)  # calculating the amount of time on screen in days
    years, d = divmod(life_days, 365)  # amount of screentime in years and days for a lifetime
    months, days = divmod(d, 30)  # calculating the number of months from the

    print(
        f"So based on your age and gender's life expectancy, if you keep using your phone for {avg_hours} hours a day")
    print(
        f"By the time you die you would have looked at your screen for:\n{years} years,{months} months and {days} days")


#Asking average daily screentime
avg_hours = int(input("What is your average screen time in hours:"))

#Providing a yearly usage summary
yearly_screen_time(avg_hours)

#Calculating life expectancy based on age and gender

life_exp = life_expectancy()

#Calculating lifetime use

lifetime_screentime(avg_hours,life_exp)
