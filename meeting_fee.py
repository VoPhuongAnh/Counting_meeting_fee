from datetime import datetime, date

# Nhập thời gian start booking

t2 = datetime(year = 2023, month = 10, day = 25, hour = 16, minute = 0, second = 0)

# Nhập thời gian end booking:

t3 = datetime(year= 2023, month= 10, day= 23, hour= 18, minute= 0, second= 0)

# Nhập thời gian báo cancel booking:
t1 = datetime(year= 2023, month= 10, day= 24, hour= 11, minute= 40, second= 0)


print('Enter Start time (yyyy-mm-dd hour:minute:second): ')
print('start time: ', t2)
print('end time: ', t3)
print('cancelled time: ', t1)

# Tính thời gian từ lúc start booking tới lúc cancel booking dùng timedelta

t4 = t2 - t1
print(t4)

# Convert thời gian chênh lệch về ngày:

t = t4.total_seconds() / 3600

# Convert về ngày:

print('Cancel booking within: ', t)

# Tính phần trăm penalty:

def percent_charge(t):
    # while t > 0:
        if (t > 48):
            charge = 0
        elif t > 24:
            charge = 50
        else:
            charge = 100
        return charge

print('Phần trăm Booking fee phải thanh toán: ', percent_charge(t), '%')
