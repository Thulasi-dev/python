// Count collisions on a Road

// There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

// You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, 
// towards the right, or staying at its current point respectively. Each moving car has the same speed.

// The number of collisions can be calculated as follows:

// When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
// When a moving car collides with a stationary car, the number of collisions increases by 1.
// After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

// Return the total number of collisions that will happen on the road.


def countCollisions(directions: str) -> int:
    directions = list(directions)

    # Step 1: Remove all leading 'L'
    i = 0
    while i < len(directions) and directions[i] == 'L':
        i += 1

    # Step 2: Remove all trailing 'R'
    j = len(directions) - 1
    while j >= 0 and directions[j] == 'R':
        j -= 1

    collisions = 0

    # Step 3: Count moving cars in the middle portion
    for k in range(i, j + 1):
        if directions[k] in ("L", "R"):
            collisions += 1

    return collisions


// Input: directions = "RLRSLL"
// Output: 5

""" Count all moving cars (L or R):

R → 1

L → 1

R → 1

S → 0

L → 1

L → 1

Total collisions = 5 """

// Input: directions = "LLRR"
// Output: 0

"""
Step 1: Remove leading 'L'

"LL" → removed

Remaining: "RR"

Step 2: Remove trailing 'R'

All Rs removed

Remaining: empty

No cars inside → no collision
Output:0
"""




