# 时间戳转换
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    utc_dt =  datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^UTC([+-]\d+):(\d+)$',tz_str)
    h= int(tz.group(1))
    m = int(tz.group(2))
    utc_dt = utc_dt.replace(tzinfo=timezone(timedelta(hours=h,minutes=m)))
    return utc_dt.timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')