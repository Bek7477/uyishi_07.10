def find_best_department(file_path):
    departments = {}
    
    with open(file_path) as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            position = parts[1]
            salary = int(parts[2])
            bonus = int(parts[3])
            department = parts[4]
            
            if bonus > 0:
                if department in departments:
                    departments[department] += 1
                else:
                    departments[department] = 1
    
    max_count = max(departments.values())
    best_departments = [dept for dept, count in departments.items() if count == max_count]
    
    for dept in best_departments:
        print(dept)

file_path = input("Fayl nomini kiriting: ")

find_best_department(file_path)