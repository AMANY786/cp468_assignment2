import numpy as np
import matplotlib.pyplot as plt

# Data from the document
data = np.array([
    [25,79], [34,51], [22,53], [27,78], [33,59], [33,74], [31,73], [22,57],
    [35,69], [34,75], [67,51], [54,32], [57,40], [43,47], [50,53], [57,36],
    [59,35], [52,58], [65,59], [47,50], [49,25], [48,20], [35,14], [33,12],
    [44,20], [45,5], [38,29], [43,27], [51,8], [46,7]
])

# A) Plot initial data points
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c='blue', alpha=0.5)
plt.xlabel("Average Monthly Spending")
plt.ylabel("Total Number of Purchases")
plt.title("Customer Data Before Clustering")
plt.grid(True)
plt.show()

# B) K-means implementation
def k_means(data, k):
    # Step 1: Select first k points as initial centroids
    centroids = data[:k].copy()
    old_centroids = np.zeros(centroids.shape)
    labels = np.zeros(len(data))
    
    # Continue until centroids stop changing
    while not np.allclose(centroids, old_centroids):
        old_centroids = centroids.copy()
        
        # Step 2 & 3: Assign points to nearest centroid
        for i, point in enumerate(data):
            distances = [np.sqrt(np.sum((point - centroid) ** 2)) 
                        for centroid in centroids]
            labels[i] = np.argmin(distances)
        
        # Step 4: Compute new centroids
        for j in range(k):
            if len(data[labels == j]) > 0:  # Avoid division by zero
                centroids[j] = np.mean(data[labels == j], axis=0)
    
    return labels, centroids

# Run K-means with k=2
k = 2
labels, final_centroids = k_means(data, k)

# C) Plot final clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'blue']
for i in range(k):
    cluster_points = data[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                c=colors[i], alpha=0.5, label=f'Cluster {i}')
    plt.scatter(final_centroids[i, 0], final_centroids[i, 1], 
                c=colors[i], marker='x', s=200, linewidths=3)

plt.xlabel("Average Monthly Spending")
plt.ylabel("Total Number of Purchases")
plt.title("Customer Clusters (k=2)")
plt.legend()
plt.grid(True)
plt.show()

# D) Count points in each cluster
cluster_counts = [np.sum(labels == i) for i in range(k)]
print("\nD) Number of data points in each cluster:")
for i, count in enumerate(cluster_counts):
    print(f"Cluster {i}: {count} points")

# E) Report final centroids
print("\nE) Final Centroids:")
for i, centroid in enumerate(final_centroids):
    print(f"Cluster {i}: ({centroid[0]:.2f}, {centroid[1]:.2f})")