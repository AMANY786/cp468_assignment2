# CP468 Assignment #2 Problem 2

## Part A Instructions:

This code plots the customer data points in a 2D scatter plot graph before clustering to visualize how customers are distributed.

Output:
![image](https://github.com/user-attachments/assets/19469f6d-38f1-4345-aeb9-1eb88cd208c6)

### How to run the code:
#### 1. Install the numpy library:
```plaintext
pip install numpy
```
#### 2. Install the pandas library:
```plaintext
pip install pandas
```
#### 3. Install the matplotlib library:
```plaintext
pip install matplotlib
```

#### 4. Download the folder **"group20_a2"**

#### 5. Open **q2_partA.py** and **CustomerProfiles_Q2** in a code editor (Ex. VS Code, Eclipse, etc)

#### 6. Run **q2_partA.py** in the code editor and it should open a window called "Figure 1", which is the scatter plot to visualize how customers are distributed.


## Part B Instructions:
This code implements the K-Means clustering algorithm for k clusters, following these 5 steps:
- **Step 1:** Select the first k data points as initial centroids.
- **Step 2:** Assign each data point to the closest centroid based on Euclidean
distance.
- **Step 3:** Label each data point with its respective cluster.
- **Step 4:** Compute new centroids for each cluster by averaging the data
points in the cluster.
- **Step 5:** Repeat steps (2) to (4) until the centroids stop changing.

Output:

```plaintext
Cluster Labels: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Centroids: [array([29.6, 66.8]), array([43.2, 16.7]), array([55.1, 46.1])]
```

### How to run the code:
#### 1. Install the numpy library:
```plaintext
pip install numpy
```
#### 2. Install the pandas library:
```plaintext
pip install pandas
```

#### 4. Download the folder **"group20_a2"**

#### 5. Open **q2_partB.py** and **CustomerProfiles_Q2** in a code editor (Ex. VS Code, Eclipse, etc)

#### 6. Run **q2_partB.py** in the code editor and it should print the results in the terminal.


## Part C Instructions:

This code plots the final clusters when k = 2, clearly showing how the data points are
grouped.

Output:
<img width="799" alt="scatter_plot_partC" src="https://github.com/user-attachments/assets/1002bf10-6933-4832-ba8a-8f495ffff26a" />

### How to run the code:

#### 1. Install the numpy library:
```plaintext
pip install numpy
```
#### 2. Install the pandas library:
```plaintext
pip install pandas
```
#### 3. Install the matplotlib library:
```plaintext
pip install matplotlib
```

#### 4. Run the script
```plaintext
python kmeans_clustering.py
```


## Part D Instructions:

Report how many data points are in each cluster after finishing the clustering
process.

```plaintext
After executing the K-Means clustering algorithm with k=2, the data points are grouped into two clusters based on their proximity to the computed centroids. The number of data points in each cluster is as follows:

Cluster 0: X points

Cluster 1: Y points

These clusters were determined using Euclidean distance to find the closest centroid for each data point.
```

## Part E Instructions:

Reporting Final Centroids. Provide the final centroid coordinates for each cluster.

```plaintext
The computed centroids represent the central point of each cluster after convergence. The final centroid coordinates for each cluster are:

Cluster 0: (X.XX, Y.XX) (Average Monthly Spending, Total Number of Purchases)

Cluster 1: (X.XX, Y.XX) (Average Monthly Spending, Total Number of Purchases)

These centroids serve as representative points summarizing the characteristics of each cluster. The clustering results may slightly vary if the initial centroid selection changes.
```
