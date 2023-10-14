import copy


class States:
    GOAL = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]

    def __init__(self, border, cost, path):
        self.border = border
        self.cost = cost
        self.path = path

    def Successor(self):
        childes = []
        hole_x = 0
        hole_y = 0
        for i in range(3):
            for j in range(3):
                if self.border[i][j] == 0:
                    hole_x = i
                    hole_y = j
        # move down
        if hole_x in [0, 1]:
            new_border = copy.deepcopy(self.border)
            new_border[hole_x + 1][hole_y], new_border[hole_x][hole_y] = new_border[hole_x][hole_y], \
                                                                         new_border[hole_x + 1][hole_y]
            childes.append(States(new_border, self.cost + 1, self.path + ",DOWN"))
        # move up
        if hole_x in [1, 2]:
            new_border = copy.deepcopy(self.border)
            new_border[hole_x - 1][hole_y], new_border[hole_x][hole_y] = new_border[hole_x][hole_y], \
                                                                         new_border[hole_x - 1][hole_y]
            childes.append(States(new_border, self.cost + 1, self.path + ",UP"))
        # move right
        if hole_y in [0, 1]:
            new_border = copy.deepcopy(self.border)
            new_border[hole_x][hole_y + 1], new_border[hole_x][hole_y] = new_border[hole_x][hole_y], \
                                                                         new_border[hole_x][hole_y + 1]
            childes.append(States(new_border, self.cost + 1, self.path + ",RIGHT"))
        # move left
        if hole_y in [1, 2]:
            new_border = copy.deepcopy(self.border)
            new_border[hole_x][hole_y - 1], new_border[hole_x][hole_y] = new_border[hole_x][hole_y], \
                                                                         new_border[hole_x][hole_y - 1]
            childes.append(States(new_border, self.cost + 1, self.path + ",LEFT"))

        return childes

    def Goal_test(self):
        for i in range(3):
            for j in range(3):
                if States.GOAL[i][j] != self.border[i][j]:
                    return False
        return True

    def Path_cost(self):
        return self.cost

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, States):
            return False
        for i in range(3):
            for j in range(3):
                if o.border[i][j] != self.border[i][j]:
                    return False
        return True

    def __repr__(self) -> str:
        output = ""
        for i in range(3):
            output = output + str(self.border[i]) + "\n"
        return output


class AI:
    @staticmethod
    def DF(start_state):
        visited = []
        fringe = [start_state]
        visited.append(start_state)
        while len(fringe) > 0:
            state = fringe[len(fringe) - 1]
            del fringe[len(fringe) - 1]
            visited.append(state)
            if state.Goal_test():
                print(state.Path_cost())
                print(state.path)
                return True
            childes = state.Successor()
            for child in childes:
                if child not in visited:
                    fringe.append(child)
        return False

    @staticmethod
    def BF(start_state):
        visited = []
        fringe = [start_state]
        visited.append(start_state)
        while len(fringe) > 0:
            state = fringe[0]
            del fringe[0]
            visited.append(state)
            if state.Goal_test():
                print(state.Path_cost())
                print(state.path)
                return True
            childes = state.Successor()
            for child in childes:
                if child not in visited:
                    fringe.append(child)
        return False


border = [
    [3, 1, 2],
    [4, 7, 5],
    [0, 6, 8],
]
state_game = States(border, 0, "")
## print("DF")
## AI.DF(state_game)
print("BF")
AI.BF(state_game)

