def search(search_criteria,sequence):
    for element in sequence:
        if search_criteria(element):
            print("Found")
            found = True
            break  # Exit the loop since we already found the friend

    if not found:
        print("Not found")