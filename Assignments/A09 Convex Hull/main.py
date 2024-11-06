from typing import List

# 0 -> p, q, r are collinear
# 1 -> Clockwise
# 2 -> Counterclockwise
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Sort the points by x, then by y
        trees = sorted(trees)

        # Special case if there are fewer than 4 points, all points form the hull
        if len(trees) <= 3:
            return trees

        # Build the lower hull
        lower_hull = []
        for p in trees:
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) == 1:
                lower_hull.pop()
            lower_hull.append(p)

        # Build the upper hull
        upper_hull = []
        for p in reversed(trees):
            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) == 1:
                upper_hull.pop()
            upper_hull.append(p)

        # Concatenate lower and upper hull, remove duplicates
        convex_hull = lower_hull[:-1] + upper_hull[:-1]  

        # Convert to set to remove duplicate points, then back to list
        return list(set(map(tuple, convex_hull)))
