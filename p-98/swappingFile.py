def swapFileData():
    fileName1 = input("Enter The File To Swap ")
    fileName2 = input("Enter The File To Be Swapped With ")

    with open(fileName1, 'r') as a:
        data_a = a.read()

    with open(fileName2, 'r') as b:
        data_b = b.read()

    with open(fileName1, 'w') as a:
        a.write(data_a)

    with open(fileName2, 'w') as b:
        b.write(data_b)

    with open(fileName1, 'r') as swappedData1:
        readData1 = swappedData1.read()

    with open(fileName2, 'r') as swappedData2:
        readData2 = swappedData2.read()


    print("The Files Are Swapped")
    print("the data in ",fileName1,"is : ",readData1)
 
    print("the data in ",fileName2,"is : ",readData2)


swapFileData()