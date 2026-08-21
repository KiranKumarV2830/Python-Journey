import datetime

def get_today():
    return datetime.date.today()

def days_until(year,month,day):
    today = datetime.date.today()
    target = datetime.date(year,month,day)
    difference = target - today
    return difference.days

if __name__ == "__main__" :
    print(datetime.date.today())
