import sys
#Secret 6: vigilant}
# Check if at least one argument (after the script name) is provided
if len(sys.argv) > 1:
    # Get the first argument
    name = sys.argv[1]
    print(f"Hello, {name}!") # Using an f-string for easy variable embedding
else:
    print("Hello, world!")