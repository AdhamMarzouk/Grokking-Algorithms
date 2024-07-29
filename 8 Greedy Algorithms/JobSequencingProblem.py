# Initialize the total hours available for jobs
hours_available = 5

# Create a dictionary of jobs with their respective values and required hours
jobs = dict()
jobs['j1'] = [100, 2]  # Job 'j1' has a value of 100 and requires 2 hours
jobs['j2'] = [19, 1]   # Job 'j2' has a value of 19 and requires 1 hour
jobs['j3'] = [27, 2]   # Job 'j3' has a value of 27 and requires 2 hours
jobs['j4'] = [25, 1]   # Job 'j4' has a value of 25 and requires 1 hour
jobs['j5'] = [15, 3]   # Job 'j5' has a value of 15 and requires 3 hours

# Initialize an empty set to keep track of the jobs taken
jobs_taken = set()
total_profit = 0

# Loop until there are no more hours available
while hours_available > 0:
    best_job = None  # Initialize the variable to hold the best job
    highest_value = float('-inf')  # Initialize the highest value to negative infinity

    # Iterate over each job and its values
    for job, values in jobs.items():
        # Check if the job has not been taken, has the highest value so far, and can be completed within the available hours
        if job not in jobs_taken and values[0] > highest_value and values[1] <= hours_available:
            highest_value = values[0]  # Update the highest value
            best_job = job  # Update the best job

    # Deduct the hours required for the best job from the available hours
    hours_available -= jobs[best_job][1]
    # Add the best job to the set of jobs taken
    jobs_taken.add(best_job)
    #Accumelate the total profit value
    total_profit += jobs[best_job][0]

# Print the set of jobs taken
print(jobs_taken)
print(f"Total profit is {total_profit}")
