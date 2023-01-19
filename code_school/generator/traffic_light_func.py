import time

def traffic_light():
    yield "Green"
    yield "Yellow"
    yield "Red"


iter_light = traffic_light()

print(next(iter_light))
time.sleep(5)
print(next(iter_light))
time.sleep(3)
print(next(iter_light))
time.sleep(5)

