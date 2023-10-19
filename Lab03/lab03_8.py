import datetime

def date_generator(start_date, end_date):
    while end_date >= start_date:
        yield start_date
        start_date = start_date + datetime.timedelta(days=1)

start_date = datetime.date(2025, 4, 27)   
end_date = datetime.date(2025, 5, 7) 

for date in date_generator(start_date, end_date):
    print(date)