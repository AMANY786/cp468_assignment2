import pandas as pd
import numpy as np

# Problem 2 Part B
def k_means(data, k):
    # step 1
    centroids = data[:k]
    
    while True:
        # step 2
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [np.linalg.norm(point - centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)
    
        # step 3
        labels = np.zeros(len(data))
        for i, cluster in enumerate(clusters):
            for point in cluster:
                labels[np.where((data == point).all(axis=1))[0][0]] = i
        
        # step 4
        new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]
        
        # step 5
        if np.all([np.array_equal(centroid, new_centroid) for centroid, new_centroid in zip(centroids, new_centroids)]):
            break
        centroids = new_centroids
    return labels, centroids

data = pd.read_csv('CustomerProfiles_Q2.csv').values
k = 3
labels, centroids = k_means(data, k)

print("Cluster Labels:", labels)
print("Centroids:", centroids)
