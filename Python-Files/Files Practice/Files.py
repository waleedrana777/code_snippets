with open ("testcopy.txt", "r") as test_copy:
    chunk_size = 10
    read_data = test_copy.read(chunk_size)
    
    while len(read_data) > 0:
        print(read_data)
        read_data = test_copy.read (chunk_size)