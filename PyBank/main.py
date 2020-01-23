import os
import csv

#store contents of monthscount and total_PL
total_months = []
total_revenue = [] 
monthly_changes_revenue = []
totalmonths = 0
totalrevenue = 0

#path to collect data from Resource folder
budgetdata_csv = os.path.join(".", "Resources", "budget_data.csv")

#open the csv file in reader mode
with open(budgetdata_csv, "r") as inputcsvfile:

    #split data with comma delimiter
    csv_reader = csv.reader(inputcsvfile, delimiter=",")

    #skip through header row
    csv_header = next(csv_reader)


    #loop through months row with a list comprehension 
    #list comprehension: monthscount = [months for months in monthscount if ]
    for row in csv_reader:

        #count number of months
        totalmonths = totalmonths + 1
        #totalmonths += 1

        #count total revenue
        totalrevenue = totalrevenue + int(row[1])
        
        #add to bucket
        total_months.append(row[0])
        total_revenue.append(row[1])

    #calculate changes in revenue month to month and find average of revenue
    for i in range(1, len(total_revenue)):
        monthly_changes_revenue.append(float(total_revenue[i]) - float(total_revenue[i-1]))
        average_revenue = round(sum(monthly_changes_revenue)/ len(monthly_changes_revenue), 2)

        #The greatest increase in profits (date and amount) over the entire period
        max_revenue = int(max(monthly_changes_revenue))

        #The greatest decrease in losses (date and amount) over the entire period
        min_revenue = int(min(monthly_changes_revenue))

        #use index to find position and month in correlation
        max_month_revenue = str(total_months[monthly_changes_revenue.index(max(monthly_changes_revenue))])
        min_month_revenue = str(total_months[monthly_changes_revenue.index(min(monthly_changes_revenue))])

        

    #print output
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f'Total Months: {totalmonths}') 
    print(f'Total Revenue: ${totalrevenue}')
    print(f'Average change in revenue: $ {average_revenue}')
    print(f'Greatest increase in revenue: {max_month_revenue} (${max_revenue})')
    print(f'Greatest decrease in revenue: {min_month_revenue} (${min_revenue})')
    print("----------------------------------------------------------")

    #print output to text file
    output_text = os.path.join(".", "PyBank_Analysis.txt")
    
    with open(output_text, "w") as textfile:
        textfile.write("Financial Analysis" + "\n")
        textfile.write("----------------------------------------------------------" + "\n")
        textfile.write(f'Total Months: {totalmonths}\n')
        textfile.write(f'Total Revenue: ${totalrevenue}\n')
        textfile.write(f'Average change in revenue: $ {average_revenue}\n')
        textfile.write(f'Greatest increase in revenue: {max_month_revenue} (${max_revenue})\n')
        textfile.write(f'Greatest decrease in revenue: {min_month_revenue} (${min_revenue})\n')
        textfile.write("----------------------------------------------------------" + "\n")

