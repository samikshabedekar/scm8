install.packages("party")

#ctree(formula, data)
library(party)
# Print some records from data set readingSkills.
print(head(readingSkills))

# Create the input data frame.
input.dat <- readingSkills[c(1:105),]

# Create the tree.
output.tree <- ctree( nativeSpeaker ~ age + shoeSize + score, data = input.dat)
# Plot the tree.
plot(output.tree)

