import console_gfx as gfx



#Translates data (RLE or raw) to a hexadecimal string (without delimiters)
def to_hex_string(data):
    hexString = ''
    for item in data:
        hexString = hexString + hex(int(item))[2:]
    return hexString

#Returns number of runs of data in an image data set 
def count_runs(flat_data):
    runs = 0
    conseq = 0
    for count,number in enumerate(flat_data):
        if len(flat_data) == count + 1:
            runs = runs + 1
            break

        elif flat_data[count] != flat_data[count+1]:
            runs = runs + 1
            conseq = 0
        else:
            if conseq == 15:
                runs = runs + 1
                conseq = 0
            else:
                conseq = conseq + 1
    return runs
            
#Returns encoding (in RLE) of the raw data passed in            
def encode_rle(flat_data):
    conseq = 1
    rleList = []
    for count,item in enumerate(flat_data):
        if len(flat_data) == count + 1:
            rleList.extend([conseq, item])
            conseq = 1
            break
        if flat_data[count] == flat_data[count+1]:
            if conseq < 15:
                conseq += 1
            elif conseq == 15:
                rleList.extend([conseq, item])
                conseq = 1
        elif flat_data[count] != flat_data[count+1]:
            rleList.extend([conseq, item])
            conseq = 1
    return rleList

#Returns decompressed size RLE data
def get_decoded_length(rle_data):
    length = 0
    for count, item in enumerate(rle_data,2):
        if count % 2 == 0:
            length = length + item
    return length

#Returns the decoded data set from RLE encoded data
def decode_rle(rle_data):
    data = []
    for count, item in enumerate(rle_data,2):
        if count % 2 == 0:
            for x in range(0, item):
                data.append(rle_data[count-1])
    return data

#Translates a string in hexadecimal format into byte data (can be raw or RLE). 
def string_to_data(data_string):
    data = []
    for char in data_string:
        data.append(int(char,16))
    return data

#Translates  RLE  data  into  a  human-readable  representation. display  the  run 
#length in decimal (1-2 digits); the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs. 
def to_rle_string(rle_data):
    data = ''

    for count, item in enumerate(rle_data,2):
        if count % 2 == 0:
            data = data + str(item) 
        elif count % 2 != 0:
            data = data + hex(int(item)) + ':'
        
    data = data.replace('0x','')
    data = data.rstrip(data[-1])
    return data

#Translates a string in human-readable RLE format (with delimiters) into RLE byte data
def string_to_rle(rle_string):
    rle = []
    for count,char in enumerate(rle_string):
        if char == ':':
            if rle_string[count-3] != ':' and count - 2 != 0:
                rle.append(int(rle_string[count-3]+rle_string[count-2]))
                rle.append(int(rle_string[count-1],16))
            else :
                rle.append(int(rle_string[count-2]))
                rle.append(int(rle_string[count-1],16))

    rle.append(int(rle_string[-2]))
    rle.append(int(rle_string[-1]))
    return rle
    


# function creating user menu
def printMenu():
    print()
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print()

        

#function prints menu, and test image then waits for user selection. from there, calls appropiate functions
def main():
    # establish vars
    menuInput = ""
    end = 0
    imgData = []
    

    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image:")
    gfx.ConsoleGfx.display_image(gfx.ConsoleGfx.test_rainbow)
    print()
    printMenu()

    #asks for user input till exit option is selected
    while end == 0:
        menuInput = input("Select a Menu Option: ")

        if menuInput == "0":
            end = 1
            
        #functions from consolegfx program
        elif menuInput == "1": 
            imgData = gfx.ConsoleGfx.load_file(input("Enter name of file to load: "))

        elif menuInput == "2":
            imgData = gfx.ConsoleGfx.test_image
            print("Test image data loaded.")

        #user inputs data, stored as flat byte data
        elif menuInput == "3":
            imgData = decode_rle(string_to_rle(input("Enter an RLE string to be decoded: ")))

        elif menuInput == "4":
            imgData = decode_rle(string_to_data(input("Enter the hex string holding RLE data: ")))

        elif menuInput == "5":
            imgData = decode_rle(string_to_data(input('Enter the hex string holding flat data: '))) 

        # display using gfx method    
        elif menuInput == "6":
            print('Displaying image...')
            if imgData == []:
                print('(no data)')
            else:
                gfx.ConsoleGfx.display_image(imgData)
                print()
        
        #momentarily displays data as desired output, but still stored as byte
        elif menuInput == "7":
            if imgData == []:
                print('RLE representation: (no data)')
            else :
                print('RLE representation:', to_rle_string(encode_rle(imgData)))

        elif menuInput == "8":
            if imgData == []:
                print('RLE hex values: (no data)')
            else:
                print('RLE hex values:', to_hex_string(encode_rle(imgData)))

        elif menuInput == "9":
            if imgData == []:
                print('Flat hex values: (no data)')
            else:
                print('Flat hex values:', to_hex_string(imgData))
        else: 
            print("Error! Invalid input.")

        #prints menu after every command besides exit
        if end == 0:    
            printMenu()

if __name__ == "__main__":
    main()