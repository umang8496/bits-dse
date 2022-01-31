"""
This is a custom module for doing clustering Algorithm.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MainClass:
    """
    This class is used for finding no of clusters and finding clusters.
    One argument: k_dict --> Dictionary of no of clusters vs  MSE
    k_means function --> finding the no of clusters
    finding_k --> drawing graph bw no of clusters vs MSE
    """

    k_dict: dict[int, float] = {}

    def __init__(self, arr: np.ndarray):
        """Self function :
        First function of the class
        input : dataframe
        """
        self.arr = arr

    def k_means(self, k: int) -> list:
        """
        Function used to find the clusters in the dataframe.
        :param k: no of clusters needed (int)
        :return: multidimensional array of clusters
        """
        arr = self.arr
        np.random.shuffle(arr)
        n = 0
        random_points = []
        for i in range(0, k):
            random_points.append(arr[i : i + 1, :])
            # print(random_points)
        while n < 10:
            # print(random_points)
            groups: list[list] = [[] for i in range(0, k)]
            n = n + 1
            for j in arr:
                smallest = 100000
                ind = 0
                for ij in range(0, len(random_points)):
                    dis0 = np.linalg.norm(j - random_points[ij])
                    if dis0 < smallest:
                        smallest = dis0
                        ind = ij

                groups[ind].append(j)

            random_points = []
            for im in range(0, k):
                random_points.append(np.mean(groups[im], axis=0))
        m = 1
        for ik in groups:
            # print(m," cluster : ",ik)
            m = m + 1
        return groups

    def finding_k(self) -> None:
        """
        Function is used to find the no of clusters.
        Sets k_dict variable with cluster no as keys and MSe as values.
        Also draws the graph between both to find the elbow point , to decide the no of clusters
        :return: none
        """
        for l in range(1, 10):
            groups = self.k_means(l)
            error = 0
            for ik in groups:
                s_sum = 0
                mean_val = np.mean(ik, axis=0)
                for j in ik:
                    err = (np.square(mean_val - j)).mean(axis=0)
                    s_sum = s_sum + err
                error = error + s_sum
            self.k_dict[l] = error
        plt.plot(self.k_dict.keys(), self.k_dict.values())  # Plot the chart
        plt.show()  # display


def preprocessing() -> np.ndarray:
    """
    helper function for prerpocessing the data
    :arguments : nil
    :return: dataframe converted to numpy array for using in algorithm
    """
    data_frame = pd.read_csv("pizza_customers.csv")
    data_frame = pd.get_dummies(data_frame, columns=["Gender"], drop_first=True)
    data_frame = data_frame.drop(["CustomerID"], axis=1)
    arr = data_frame.to_numpy()

    return arr


if __name__ == "__main__":
    input_arr = preprocessing()
    p1 = MainClass(input_arr)
    # print(help(p1.finding_k))
    # p1.finding_k()
    NO = 6
    clusters = p1.k_means(NO)

    clusters_df = []
    for ijk in range(0, NO):
        clusters_df.append(
            pd.DataFrame(
                clusters[ijk],
                columns=["Age", "Annual Income", "Spending", "Gender_Male"],
            )
        )

    for mn in clusters_df:
        print(mn.describe())

    print(clusters_df)
