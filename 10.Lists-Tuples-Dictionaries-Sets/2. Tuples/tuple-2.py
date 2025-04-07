bag = ("maths_notebook", 12, 34, 56, "handwriting_notebook")
print("All bag contents :: {}".format(bag))

print(len(bag))

print(bag[4])

# Immutable

# Delete entire tuple
#del bag[1]
#del bag
print(bag[4])

bag_extended = ("EVS", 22, "Telugu")

all_bags = bag + bag_extended
print(all_bags[0])