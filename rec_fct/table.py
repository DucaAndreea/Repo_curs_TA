from tabulate import tabulate
# Tabel - clasic
# table_data = [['Name', 'Age', 'Job'],
#               ['Mike', 22, 'Programmer'],
#               ['John', 18, 'Teacher']]
#print(table_data)
#print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
# format: psql, plain, fancy_grid


# Tabel - dictionar
data = {
    'Name': ['Mike', 'John', 'Jane', 'Jack', 'SomeLongName'],
    'Age':[22, 18, 23, 10, 40],
    'Job': ['Programmer', 'Teacher', 'Designer', 'Student', 'Manager']
    }
print(tabulate(data, headers="keys", tablefmt="psql", showindex="always"))




# for row in table_data:
#     for col in row:
#         print(col, end=' ' )
#     print()


