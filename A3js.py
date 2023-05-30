n = int(input("Enter number of jobs: "))
jobs = []
print("Enter Id, deadline and profit respectively for each job:")
for i in range(n):
    job = input("Job " + str(i+1) + ": ").split()
    jobs.append(job)

sorter = lambda job: int(job[2]) 
jobs = sorted(jobs, key=sorter, reverse=True)

scheduled = []
time = 0

for i in jobs:
    if time <= int(i[1]):
        scheduled.append(i[0])
        time += 1

print("Jobs are scheduled as: ", scheduled)

#end--------------------------------------------------------------------------------------------------

'''
n = int(input("Enter number of jobs: "))
This line prompts the user to enter the number of jobs and assigns the input value to the variable n. 
The int() function is used to convert the user's input, which is initially a string, into an integer.

jobs = []
This line initializes an empty list called jobs to store the job details.

print("Enter Id, deadline and profit respectively for each job:")
This line displays a message to instruct the user to enter the job details.

for i in range(n):
This line starts a loop that iterates n times, where n is the number of jobs entered by the user.

job = input("Job " + str(i+1) + ": ").split()
This line prompts the user to enter the details for each job. The input is split into separate values at each space, 
creating a list of input values for a job. The str(i+1) converts the loop index i into a string and adds 1 to display a user-friendly job number.

jobs.append(job)
This line adds the list of job details (job) to the jobs list.

sorter = lambda job: int(job[2])
This line defines a lambda function (anonymous function) called sorter. 
It takes a job as input and returns the integer value of the third element (job[2]) in the job list. 
This lambda function will be used as the key for sorting the jobs based on their profits in descending order.

jobs = sorted(jobs, key=sorter, reverse=True)
This line sorts the jobs list using the sorted() function. 
It takes the jobs list as input, uses the sorter lambda function as the key for sorting, 
and sets reverse=True to sort the jobs in descending order based on their profits.

scheduled = []
This line initializes an empty list called scheduled to store the IDs of the jobs that will be scheduled.

time = 0
This line initializes the time variable to 0. It will be used to track the current time while scheduling the jobs.

for i in jobs:
This line starts a loop that iterates over each job in the jobs list, which is now sorted based on profits.

if time <= int(i[1]):
This line checks if the current time is less than or equal to the integer value of the job's deadline (i[1]). 
If the condition is true, it means the job can be scheduled within its deadline.

scheduled.append(i[0])
This line adds the ID of the job (i[0]) to the scheduled list since it can be scheduled within the deadline.

time += 1
This line increments the time variable by 1, indicating that one unit of time has been consumed by scheduling a job.

print("Jobs are scheduled as: ", scheduled)
This line displays a message indicating that the scheduled jobs will be printed next.
and prints the list of scheduled job IDs.
....
That's a detailed explanation of each line in the given code. 
It takes user input for job details, sorts the jobs based on their profits in descending order, 
and schedules the jobs within their deadlines. Finally, it displays the list of scheduled job IDs.'''