from executeQuery import execute_query 

def runsqlQueries():
    # Open and read the file 
    file_dir = open('C:/Users/ManpreetSingh/Desktop/simple-sql-parser-short/operations.sql', 'r')
    sqlFile = file_dir.read()
    file_dir.close()      
    sqlCommands = sqlFile.split(';')
    i = 0
    for command in sqlCommands:
        if i==4:
            break
        final_query = command
        queryExecution = execute_query(final_query)
        i+= 1

if __name__ == '__main__':
    runsqlQueries()