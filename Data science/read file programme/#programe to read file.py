#programe to read file

def read_data(file_name):

    #open file
    try: 
        file = open(file_name, 'r')

        print("File : {file_name} opened successfully")

        lines = file.readlines()

        file.close()

    except fileNotFoundError:
        print(f"Error: {file_name} not found.")

    except IOError:
        print(f"unable to read file")

    user_input_file =("Enter the file you would like to open: ")

    read_date(user_input_file)
        



