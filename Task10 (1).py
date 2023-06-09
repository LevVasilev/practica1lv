class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def crack(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'F'
            return 3
        elif self.state == 'D':
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            return 8
        else:
            raise (MealyError('crack'))

    def build(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'F':
            self.state = 'D'
            return 7
        else:
            raise (MealyError('build'))


def main():
    return StateMachine()


def test():
    test_exceptions = [
        ('A', 'build'),
        ('B', 'build'),
        ('E', 'build'),
        ('', 'crack')
    ]
    test_result = [
        ('A', 'crack', 0, 'B'),
        ('B', 'crack', 1, 'C'),
        ('C', 'build', 2, 'D'),
        ('C', 'crack', 3, 'F'),
        ('D', 'build', 4, 'E'),
        ('D', 'crack', 5, 'D'),
        ('E', 'crack', 6, 'F'),
        ('F', 'build', 7, 'D'),
        ('F', 'crack', 8, 'F'),
    ]
    sm = main()
    for start_state, action in test_exceptions:
        sm.state = start_state
        try:
            if action == 'crack':
                sm.crack()
            else:
                sm.build()
        except MealyError:
            pass
    for start_state, action, expected_return, expected_state in test_result:
        sm.state = start_state
        if action == 'crack':
            assert sm.crack() == expected_return
            assert sm.state == expected_state
        else:
            assert sm.build() == expected_return
            assert sm.state == expected_state
