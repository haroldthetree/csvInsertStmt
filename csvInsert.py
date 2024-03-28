import csv

####csv must have headers - does not like utf-8, try to save as MS-DOS csv

def iter():
    with open('file.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        #iterates through rows and assigns vars based off header
        for row in reader:
            a_int = row["a_int"]
            b_int = row["b_int"]
            c_int = row["c_int"]
            d_str = row["d_str"]
            e_int = row["e_int"]
            #creates text file and writes text based off above vars, appends every open
            f = open('insertStmt.txt', 'a')
            f.write("INSERT INTO future_order_adjustments (a_int, b_int, c_int, d_str, e_int) VALUES (%s, %s, %s, \"%s\", %s)\n" % (a_int, b_int, c_int, d_str, e_int))
            f.close()

iter()