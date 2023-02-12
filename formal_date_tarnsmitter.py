"""
Year, Month, Day, Hour, Minute, Second will be inserted
create formal date transmitter
"""

year, month, day, hour, minute, second = map(int, input().split())
print(year, month, day, sep='-', end=' T ')
print(hour, minute, second, sep=':')