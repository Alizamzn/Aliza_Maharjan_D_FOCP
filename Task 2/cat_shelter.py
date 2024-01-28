import sys

#Function to analyze the log file of a cat shelter
def analyze_cat_shelter(file_path):
    try:
        # Open the log file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Handle file not found error
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

    # Initialize variables to track statistics
    cat_entries = 0
    intruder_doused = 0
    total_time_in_house = 0
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_name = parts[0]
        entry_time = int(parts[1])
        exit_time = int(parts[2])
        
        # Check if the cat is a shelter cat (OURS) or an intruder
        if cat_name == 'OURS':
            cat_entries += 1
            total_time_in_house += exit_time - entry_time
            visit_lengths.append(exit_time - entry_time)
        else:
            intruder_doused += 1

    avg_visit_length = sum(visit_lengths) // len(visit_lengths) if visit_lengths else 0
    longest_visit = max(visit_lengths) if visit_lengths else 0
    shortest_visit = min(visit_lengths) if visit_lengths else 0

    print("\nLog File Analysis\n==================")
    print(f'Cat Visits: {cat_entries}')
    print(f'Other Cats: {intruder_doused}')
    print(f'Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes')
    print(f'Average Visit Length: {avg_visit_length} Minutes')
    print(f'Longest Visit: {longest_visit} Minutes')
    print(f'Shortest Visit: {shortest_visit} Minutes')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        sys.exit(1)

    # Get the path to the log file from the command-line arguments
    log_file_path = sys.argv[1]
    analyze_cat_shelter(log_file_path) 
