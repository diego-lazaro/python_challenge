import os
import csv

#set libraries and variables for place holders

profit_loss = []
month_name = []
changes = []
month_change = []
counter = 0

#open files for specific data

bank_data = os.path.join("pybank", "resources", "budget_data.csv")

with open(bank_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#filter header lines out

    csv_header = next(csvreader)

#start loops for collecting intial values and calculations
#add strings to month list values

    for row in csvreader:

        if counter == 0:            
            
            counter = counter + 1
            
            set_value = int(row[1])
            
            profit_loss.append(int(row[1]))
            
            month_name.append(str(row[0]))

#add values for list and calculations 
        else:
            
            profit_loss.append(int(row[1]))
            
            month_name.append(str(row[0]))
            
            changes.append(int(int(row[1]) - set_value))
            
            month_change.append(str(row[0]))
            
            set_value = int(row[1])

#extract information for calculations

    total_months = len(month_name)
    profit_losses = sum(profit_loss)
    
#record profit_change by correctly adding and rounding to 2 decimal places with , 2

    profit_change = round(sum(changes) / len(month_change), 2)
    greatest_inc = max(changes)
    greatest_increase_profits = changes.index(greatest_inc)
    greatest_dec = min(changes)
    greatest_decrease_profits = changes.index(greatest_dec)

#print results
 
print('Financial Analysis')
print('------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${profit_losses}')
print(f'Average Change: ${profit_change}')
print(f'Greatest Increase in Profits: {month_change[int(greatest_increase_profits)]} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {month_change[int(greatest_decrease_profits)]} (${greatest_dec})')

#save to text file

with open('analysis.txt', 'w') as file:
    file.write('Financial Analysis\n')
    file.write('-----------------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${profit_losses}\n')
    file.write(f'Average Change: ${profit_change}\n')
    file.write(f'Greatest Increase in Profits: {month_change[int(greatest_increase_profits)]} (${greatest_inc})\n')
    file.write(f'Greatest Decrease in Profits: {month_change[int(greatest_decrease_profits)]} (${greatest_dec})\n')
    file.close()
