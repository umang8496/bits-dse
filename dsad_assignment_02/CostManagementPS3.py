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
# Total profits: 411
# Fund remaining: 28
#####################################################################
class CostManagement(object):
    def __init__(self, outputfile):
        self.dp = []
        self.fw = outputfile


    def solve_knapsack_problem(self, profits, weights, capacity):
        dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
        result = self.recursive_knapsack(dp, profits, weights, capacity, 0)
        self.dp = self.construct_table(profits, weights, capacity)
        solution = self.get_optimal_solution_for_knapsack(self.dp, profits, weights, capacity)
        self.print_the_funds_order(solution, weights)
        fundRemaining = sum(weights) - sum(solution)
        # print("Total profits:", result)
        self.fw.write(str("Total profits: " + str(result)))
        self.fw.write(str("\n"))
        # print("Fund remaining:", fundRemaining)
        self.fw.write(str("Fund remaining: " + str(fundRemaining)))
        self.fw.write(str("\n"))
        

    def recursive_knapsack(self, dp, profits, weights, capacity, currentIndex):
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if dp[currentIndex][capacity] != -1:
            return dp[currentIndex][capacity]

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + self.recursive_knapsack(dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

        profit2 = self.recursive_knapsack(dp, profits, weights, capacity, currentIndex + 1)

        dp[currentIndex][capacity] = max(profit1, profit2)
        return dp[currentIndex][capacity]


    def get_optimal_solution_for_knapsack(self, dp, profits, weights, capacity):
        keep = list()
        n = len(weights)
        totalProfit = dp[n-1][capacity]
        for i in range(n-1, 0, -1):
            tmp = dp[i - 1][capacity]
            if totalProfit != tmp:
                keep.append(weights[i])
                capacity -= weights[i]
                totalProfit -= profits[i]
        if totalProfit != 0:
            keep.append(weights[0])
        return keep


    def construct_table(self, profits, weights, capacity):
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

        return dp


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
        # print("The projects that should be funded: ", end="")
        self.fw.write(str("The projects that should be funded: "))
        for f in preservedIndex:
            if f == preservedIndex[-1]:
                # print(str(f), end="")
                self.fw.write(str(f))
            else:
                # print(str(f) + ", ", end="")
                self.fw.write(str(f) + ", ")
        # print()
        self.fw.write(str("\n"))


    # def solve_knapsack_brute_force(self, profits, weights, capacity):
    #     return self.knapsack_recursive_brute_force(profits, weights, capacity, 0)


    # def knapsack_recursive_brute_force(self, profits, weights, capacity, currentIndex):
    #     if capacity <= 0 or currentIndex >= len(profits):
    #         return 0

    #     profit1 = 0
    #     if weights[currentIndex] <= capacity:
    #         profit1 = profits[currentIndex] + self.knapsack_recursive_brute_force(profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    #     profit2 = self.knapsack_recursive_brute_force(profits, weights, capacity, currentIndex + 1)

    #     return max(profit1, profit2)


####################################################################

####################################################################
if __name__ == "__main__":
    inputfilename = "inputPS3.txt"
    outputfilename = "outputPS3.txt"
    inputfile = None
    outputfile = None
    weights = []
    profits = []
    capacity = 150
    try:
        inputfile = open(inputfilename, "r")
        outputfile = open(outputfilename, "w")
        if (inputfile != None) and (outputfile != None):
            for line in inputfile:
                line = line.split("/")
                weights.append(int(line[1]))
                profits.append(int(line[2]))
            cm  = CostManagement(outputfile)
            if (cm != None):
                cm.solve_knapsack_problem(profits, weights, capacity)
            inputfile.close()
            outputfile.close()
        else:
            print("Unable to read the prompt file.")
    except FileNotFoundError:
        print("Input File:", inputfile, "is not found.")

    # weights = [1, 3, 4, 5]
    # profits = [1, 4, 5, 7]
    # capacity = 7

    # weights = [2, 1, 1, 3]
    # profits = [2, 8, 1, 10]
    # capacity = 4

    # weights = [1, 2, 3]
    # profits = [2.5, 2, 4.5]
    # capacity = 5

    # weights = [23, 21, 12, 18, 16, 17, 17, 8, 12, 7]
    # profits = [10, 12, 60, 45, 23, 46, 46, 31, 43, 20]
    # capacity = 60

    # weights=[23, 21, 12, 18, 16, 17, 18, 8, 12, 7]
    # profits=[10, 12, 60, 45, 23, 46, 47, 31, 43, 14]
    # capacity = 90

    # weights=[19, 11, 16, 22, 21, 16, 5, 8, 15, 13]
    # profits=[31, 54, 11, 42, -27, 17, 23, -11, 21, 29]
    # capacity = 100

    # weights=[30, 17, 20, 10, 13, 10, 16, 25, 15, 18]
    # profits=[60, 35, 55, 40, 66, 20, 35, 50, 70, 10]
    # capacity = 150

    # weights = [2, 4, 3, 5, 5]
    # profits = [3, 4, 1, 2, 6]
    # capacity = 12

    # print("weights:", weights)
    # print("profits:", profits)
    # print("capacity:", capacity)
    # print()
    # print()
    # cm  = CostManagement()
    # cm.solve_knapsack_problem(profits, weights, capacity)
    # cm.construct_table(profits, weights, capacity)


