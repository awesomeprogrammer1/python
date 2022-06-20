victor_speed = 18 # km/h
alex_speed = 24 # km/h

initial_distance = 0.5 # km

for i in range(60):
    victor_location = round(victor_speed * (i/60) + initial_distance,1)
    alex_location = round(alex_speed * (i/60),1)
    distance_between_victor_and_alex = round(victor_location - alex_location,1)
    print(f"after {i} min: Victor's location is {victor_location}, Alex's location is {alex_location}, distance between them is {distance_between_victor_and_alex}")
    if distance_between_victor_and_alex < 0:
        break


