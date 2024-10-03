#Thai Nguyen, ParkPhotos.txt

Input = input("Enter the file: ")
if Input == "":
    print()
else:
    #Open the file that I already downloaded
    f = open("ParkPhotos.txt")
    
    #Search for text
    search_text = "_photo.jpg"
    
    #Replace the text file
    replace_text = "_info.txt"

    #Read the file and use the replace function
    f1 = f.read()
    f1 = f1.replace(search_text, replace_text)
    print(f1)


