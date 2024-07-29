# Initialize a dictionary of stations with the states they cover
stations = dict()
stations['s1'] = set(['id', 'nv', 'ut'])
stations['s2'] = set(['wa', 'id', 'mt'])
stations['s3'] = set(['or', 'nv', 'ca'])
stations['s4'] = set(['nv', 'ut'])
stations['s5'] = set(['ca', 'az'])

# Define the set of states that need to be covered
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# Initialize an empty set to hold the final list of stations
final_stations = set()

# Loop until all states are covered
while states_needed:
    best_station = None  # Initialize the best station variable
    states_covered = set()  # Initialize the set of states covered by the best station

    # Iterate over each station and its covered states
    for station, states in stations.items():
        # Find the intersection of states_needed and states covered by the current station
        covered = states_needed & states
        # If the current station covers more states than the best station found so far, update best_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    # Remove the states covered by the best station from states_needed
    states_needed -= states_covered
    # Add the best station to the final list of stations
    final_stations.add(best_station)

# Print the final set of stations that cover all states
print(final_stations)
