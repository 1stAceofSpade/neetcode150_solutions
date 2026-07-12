class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        running_fuel = 0
        size = len(gas)
        if sum(gas)<sum(cost):
            return -1
        for start in range(size):
            running_fuel = gas[(start)%size]
            print(running_fuel)
            j=(start+1+size)%size
            print(j)
            while j!=(start%size):
                running_fuel=running_fuel-cost[(j-1+size)%size]
                if running_fuel<=0:
                    break
                running_fuel+=gas[(j+size)%size]
                j=(j+1)%size
            if j==start:
                return j
        return -1