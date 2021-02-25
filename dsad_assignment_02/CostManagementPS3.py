#####################################################################
# CostManagementPS3.py
#####################################################################


#####################################################################
# Sample Input:
# 1 / 30 / 60
# 2 / 17 / 35
# 3 / 20 / 55
# 4 / 10 / 40
# 5 / 13 / 66
# 6 / 10 / 20
# 7 / 16 / 35
# 8 / 25 / 50
# 9 / 15 / 70
# 10 / 18 / 10
#####################################################################


#####################################################################
# Sample Output:
# The projects that should be funded: 1,2,3,4,5,7,8,9
# Total ROI: 411
# Fund remaining: 28
#####################################################################
class CostManagement(object):
    def __init__(self):
        self.dp = []


    def solve_knapsack_top_down(self, profits, weights, capacity):
        self.dp = [[0 for x in range(capacity+1)] for y in range(len(profits))]
        result = self.knapsack_recursive_top_down(self.dp, profits, weights, capacity, 0)
        rev_dp = self.dp[::-1]
        # print("dp:", self.dp)
        # print("rev_dp:", rev_dp)
        # self.print_selected_elements(self.dp, profits, weights, capacity)
        self.print_selected_elements(rev_dp, profits, weights, capacity)
        return result


    def knapsack_recursive_top_down(self, dp, profits, weights, capacity, currentIndex):
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if dp[currentIndex][capacity] != 0:
            return dp[currentIndex][capacity]

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.knapsack_recursive_top_down(dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

        profit2 = self.knapsack_recursive_top_down(dp, profits, weights, capacity, currentIndex + 1)

        dp[currentIndex][capacity] = max(profit1, profit2)
        return dp[currentIndex][capacity]


    def print_selected_elements(self, dp, profits, weights, capacity):
        keep = list()
        n = len(weights)
        totalProfit = dp[n-1][capacity]
        for i in range(n-1, 0, -1):
            if totalProfit != dp[i - 1][capacity]:
                keep.append(weights[i])
                capacity -= weights[i]
                totalProfit -= profits[i]
        if totalProfit != 0:
            keep.append(weights[0])
        return keep


    def solve_knapsack_bottom_up(self, profits, weights, capacity):
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity+1)] for y in range(n)]

        for i in range(0, n):
            dp[i][0] = 0

        for c in range(0, capacity+1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        for i in range(1, n):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]
                    profit2 = dp[i - 1][c]
                    dp[i][c] = max(profit1, profit2)

        solution = self.print_selected_elements(dp, profits, weights, capacity)
        self.print_the_funds_order(solution, weights)
        ROI =  dp[n-1][capacity]
        fundRemaining = sum(weights) - sum(solution)
        print("Total ROI:", ROI)
        print("Fund remaining:", fundRemaining)


    def print_the_funds_order(self, solution, weights):
        tmp_weights = weights.copy()
        preservedIndex = []
        for f in solution:
            for w in tmp_weights:
                if w == f:
                    i = tmp_weights.index(w)
                    tmp_weights[i] = -1
                    preservedIndex.append(i+1)
                    break
        preservedIndex.sort()
        print("The projects that should be funded: ", end="")
        for f in preservedIndex:
            if f == preservedIndex[-1]:
                print(str(f), end="")
            else:
                print(str(f) + ", ", end="")
        print()


    def solve_knapsack_brute_force(self, profits, weights, capacity):
        return self.knapsack_recursive_brute_force(profits, weights, capacity, 0)


    def knapsack_recursive_brute_force(self, profits, weights, capacity, currentIndex):
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.knapsack_recursive_brute_force(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

        profit2 = self.knapsack_recursive_brute_force(profits, weights, capacity, currentIndex + 1)

        return max(profit1, profit2)


####################################################################

####################################################################
if __name__ == "__main__":
    inputfilename = "inputPS3.txt"
    outputfilename = "outputPS3.txt"
    inputfile = None
    cost = []
    roi = []
    capacity = 150
    try:
        inputfile = open(inputfilename, "r")
        if (inputfile != None):
            for line in inputfile:
                line = line.split("/")
                cost.append(int(line[1]))
                roi.append(int(line[2]))
    except FileNotFoundError:
        print("Input File:", inputfile, "is not found.")

    # cost = [1, 3, 4, 5]
    # roi = [1, 4, 5, 7]
    # capacity = 7

    # cost = [1, 2, 3]
    # roi = [2.5, 2, 4.5]
    # capacity = 5

    # cost = [2, 1, 1, 3]
    # roi = [2, 8, 1, 10]
    # capacity = 4

    cm  = CostManagement()
    # print(cm.solve_knapsack_top_down(roi, cost, capacity))
    cm.solve_knapsack_bottom_up(roi, cost, capacity)


