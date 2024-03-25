def count_heights():
    height_counts = {"4": 0,"5": 0,"6": 0,"7": 0}
    
    while True:
        height_input = input("Enter height in the format feet'inches\" (e.g., 5'11\") or type 'done' to finish: ")
        
        if height_input.lower() == "done":
            break
        
        feet, inches = height_input.split("'")
        
        feet = int(feet)
        if feet >= 4 and feet <= 7:
            height_counts[str(feet)] += 1
        else:
            print("Height must be between 4 and 7 feet.")
    
    print("\nHeight Counts:")
    for height, count in height_counts.items():
        print(f"{height}-footers: {count}")

count_heights()
