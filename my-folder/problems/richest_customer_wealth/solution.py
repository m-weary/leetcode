class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_wealth = []
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            total_wealth.append(wealth)
        return max(total_wealth)
        