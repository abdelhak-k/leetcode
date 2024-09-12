class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # I will define a map: map[pos]=speed, positions are all unique
        n = len(position)
        
        
        # array of tuples and then we will turn it into a dict
        pos_speed = [None] * n
        for i in range(n):
            pos_speed[i]= (position[i],speed[i])
        
        
        pos_speed.sort(reverse= True)
        pos_speed = dict(pos_speed)
        # now pos_speed is a decreasing sorted dict
        
        # we will use the stack to store the last car fleet
        stack = []
        
        # car fleet: if the current car reaches the distination in lower time then the other car
        
        for car in pos_speed:
            if len(stack) == 0:
                stack.append(car)
            else:
                last_car= stack[-1] # only the key to it(position)
                last_car_time_rem= (target-last_car)/pos_speed[last_car]
                curr_car_time_rem= (target-car)/pos_speed[car]
                
                if(curr_car_time_rem> last_car_time_rem):
                    stack.append(car)
            
            
        return len(stack)