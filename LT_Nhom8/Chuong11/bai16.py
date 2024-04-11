import csv  
    
with open('File/names.csv')as file:  

    csvFile = csv.reader(file)  
    
    for lines in csvFile:  
        print(lines)  


fields = ['Name', 'Branch', 'Year', 'CGPA']  
filename = "File/t.csv"
rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]
    
with open(filename, 'w') as csvfile:
    

    csvwriter = csv.writer(file)  
    csvwriter.writerow(fields)  
    csvwriter.writerows(rows) 