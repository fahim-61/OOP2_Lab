import numpy as np

# 1. Create a NumPy array
scores = np.array([70, 85, 90, 95, 80])

# a) Convert data type to float
scores_float = scores.astype(float)
print("Scores (float):", scores_float)

# b) Create a copy and add 10 points
updated_scores = scores.copy() + 10
print("Updated Scores:", updated_scores)

# c) Array properties
print("Shape:", scores.shape)
print("Dimensions:", scores.ndim)
print("Size:", scores.size)
print("Item size:", scores.itemsize)
print("Data type:", scores.dtype)
print("Sorted Scores:", np.sort(scores))

# d) Indices where scores >= 85
indices = np.where(scores >= 85)
print("Indices with scores >= 85:", indices)

# e) Statistical operations
print("Min:", np.min(scores))
print("Max:", np.max(scores))
print("Standard deviation:", np.std(scores))
print("Variance:", np.var(scores))
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))

# f) Access specific elements and slices
print("Score[1]:", scores[1])
print("Last 3 scores:", scores[-3:])
print("Scores from index 1 to 3:", scores[1:4])
