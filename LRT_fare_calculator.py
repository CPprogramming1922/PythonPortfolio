East_loop = ["Sengkang", "Compassvale", "Rumbia", "Bakau", "Kangkar", "Ranggung"]
West_loop = ["Sengkang", "Cheng Lim", "Farmway", "Kupang", "Thanggam", "Fernvale", "Layar", "Tongkang", "Renjong"]
main_difference = 0

def basic_distance(start, end, loop):
    stop_difference = 0
    stop_difference += abs(loop.index(end) - loop.index(start))
    if stop_difference > int(len(loop)/2):
        stop_difference = len(loop) - stop_difference
    return stop_difference

#If both stops are in the same loop, only 1 function is needed
def distance_same_loop(start, end, loop):
    stop_difference = basic_distance(start, end, loop)
    return stop_difference
distance_same_loop ("Cheng Lim", "Fernvale", West_loop)

def distance_diff_loop(start, end, start_loop, end_loop):
    #Number of stops accumulated in the first loop travelling to Sengkang to switch loops
    stop_difference = 0
    stop_difference += basic_distance(start, "Sengkang", start_loop)
    stop_difference += basic_distance("Sengkang", end, end_loop)
    return stop_difference

def fare_calculator(start, end):
    Cost = 0
    # Calculates number of stops
    if start in East_loop and end in East_loop:
        main_difference = basic_distance(start, end, East_loop)
    elif start in West_loop and end in West_loop:
        main_difference = basic_distance(start, end, West_loop)
    elif start in East_loop and end in West_loop:
        main_difference = distance_diff_loop(start, end, East_loop, West_loop)
    else:
        main_difference = distance_diff_loop(start, end, West_loop, East_loop)
    
    #Predicts fare using the average cost per stop for the Sengkang LRT system
    Average_cost = 0.18571
    Cost = round(main_difference*Average_cost, 2)
    print (f"The distance between {start} and {end} is {main_difference} stops. The fare for your trip will be ${Cost}" )

fare_calculator("Rumbia", "Fernvale")








