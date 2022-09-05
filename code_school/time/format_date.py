import time

named_tuple = time.localtime()
time_string = time.strftime("%Y-%m-%d, %H:%M %p %Z", named_tuple)

print(time_string)
