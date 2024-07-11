def naqsh(colors):
    if not colors:
        return 0
    time = 2 
    for i in range(1, len(colors)):
        if colors[i] != colors[i - 1]:
            time += 1  
        time += 2  
    return time


lst_colors = []
n = int(input("nechta rang kiritmoqchisiz: "))
for i in range(n):
    rang = input("rang>>> ")
    lst_colors.append(rang)
        
total_time = naqsh(lst_colors)
print(total_time)