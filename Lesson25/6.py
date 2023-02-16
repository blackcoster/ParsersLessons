from datetime import date

def check_date(y,m,d):
    try:
        date(y,m,d)
        return True
    except Exception:
        return False

print(check_date(2023,2,28))
print(check_date(2023,2,45))

