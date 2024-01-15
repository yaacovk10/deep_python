import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = 'data.csv'
gen1 = read_csv(csv_file_path)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1


# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
