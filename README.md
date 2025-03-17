# CP468 Assignment #2 Problem 2

## Part A Instructions:

This code plots the customer data points in a 2D scatter plot graph before clustering to visualize how customers are distributed.

Sample output:
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

#### 4. Download **q2_partA.py** in the **"group20_a2"** folder

#### 5. Open **q2_partA.py** in a code editor (Ex. VS Code, Eclipse, etc)

#### 6. Run the code in the code editor and it should open a window called "Figure 1", which is the scatter plot to visualize how customers are distributed.

## Part B Instructions:
This code implements the K-Means clustering algorithm for k clusters, following these 5 steps:
- **Step 1:** Select the first k data points as initial centroids.
- **Step 2:** Assign each data point to the closest centroid based on Euclidean
distance.
- **Step 3:** Label each data point with its respective cluster.
- **Step 4:** Compute new centroids for each cluster by averaging the data
points in the cluster.
- **Step 5:** Repeat steps (2) to (4) until the centroids stop changing.
