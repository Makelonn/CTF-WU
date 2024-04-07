# Example usage:
coordinates_list = [[(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2), (2, 0)],
                    [(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2),(0, 0), (2, 0), (1, 0)],
                    [(2, 0), (-1, 2), (-1, -2)]
                    ]

# List 1 should return 2 lists
# List 2 should return 3 lists
# List 3 should return a list

coordinates_list = [[(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2), (2, 0), (-1, -2),(0, 0), (1, 0)] *6]
# Actual list
#coordinates_list = [[(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]]

# Now cleaning the list so each form is in a different list

debug = True
cleaned = []
for i in coordinates_list:
    if debug: print("LIST n°", i)
    if (0,0) not in i :
        cleaned.append(i)
        if debug: print("No (0,0) in the list")
    else:
        # Count the number of (0,0) in the list
        count = i.count((0,0))
        if debug : print(count, "in the list")
        for j in range(count):
            if debug : print("--- Doing n°", j)
            first = i.index((0,0))
            
            cleaned.append(i[:first])
            if debug : print("Append ", i[:first])

            i = i[first+2:]
            if debug : print("New list ", i)
        if len(i) > 0: 
            cleaned.append(i)
if debug:
    for i in cleaned:
        print(i)