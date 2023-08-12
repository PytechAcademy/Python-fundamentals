import multiprocessing

def process_data(data):
    print(f"Processing {data}")

def main():
    data = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(process_data, data)

if __name__ == "__main__":
    main()