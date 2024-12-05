class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # init connections dictionary, and gardenColors list.
        connections = {path: [] for path in range(1, n + 1)}
        gardenColors = [0] * n

        # handling special case.
        if len(paths) == 0:
            temp = [1] * n
            return temp

        # building the connections dictionary.
        for path in paths:
            connections[path[0]].append(path[1])
            connections[path[1]].append(path[0])

        # coloring gardens.
        for garden in range(1, n + 1):
            # find colors of neighboring gardens. (Set for lookup efficiency)
            usedColors = {gardenColors[neighbor - 1] for neighbor in connections[garden]}
            for color in range(1, 5):
                if color not in usedColors:
                    # once first available color is found, assign and break out to next garden.
                    gardenColors[garden - 1] = color
                    break

        # return answer.
        return gardenColors
