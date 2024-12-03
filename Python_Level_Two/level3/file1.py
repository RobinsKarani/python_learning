# data_processor.py
def process_data(data):
    return [x ** 2 for x in data]

if __name__ == "__main__":
    # Code that runs when the script is executed directly
    sample_data = [1, 2, 3, 4]
    print("Processing sample data...")
    print(process_data(sample_data))
