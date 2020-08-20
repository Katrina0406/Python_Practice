def main():
    # Open a file for writing and create it if it doesn't exist
    f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    f = open("textfile.txt", "a")

    # Open the file for reading
    f = open("textfile.txt", "r")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line" + str(i) + "\r\n")

    # # Open the file back up and read the contents
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    # close the file when done
    f.close()

if __name__ == "__main__":
    main()