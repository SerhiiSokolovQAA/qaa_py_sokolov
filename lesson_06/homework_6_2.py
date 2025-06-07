while True:
    data_to_ckeck = input("Enter text with char 'h' or 'H': ")
    if 'h' in data_to_ckeck.lower():
        print("Data contains char 'h'")
        break
    else:
        print("Data does not contains char 'h'.")