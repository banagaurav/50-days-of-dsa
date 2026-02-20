n = 4

# Upper half of diamond
for i in range(1, n+1):
    # Print leading underscores
    for j in range(n - i):
        print(" ", end=" ")
    
    # Print first star
    print("*", end=" ")
    
    # Print middle underscores (if any)
    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end=" ")
        # Print second star
        print("*", end="")
    
    # New line
    print()

# Lower half of diamond
for i in range(n-1, 0, -1):
    # Print leading underscores
    for j in range(n - i):
        print(" ", end=" ")
    
    # Print first star
    print("*", end=" ")
    
    # Print middle underscores (if any)
    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end=" ")
        # Print second star
        print("*", end="")
    
    # New line
    print()