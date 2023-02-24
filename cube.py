x = {'0', '1'}
y = {'-1'}
z = set()


class Cube:

    def __init__(self, string=''):
        self.string = string

    # update some symbol in cube
    def update(self, val):
        if type(val) is type(str()):
            self.string += val
        elif type(val) is type(set()):
            self.string += Cube.set_to_char(val)

    # convert symbol in set
    @staticmethod
    def char_to_set(char):
        char = str(char)
        try:
            if char != '1' and char != '0' and char != 'set()':
                if char != 'x' and char != 'y' and char != 'z':
                    raise ValueError
                return eval(char)
        except ValueError:
            print(f"Incorrect input of cube. Unknown char [{el}]")
            exit()
        return set(char)

    # convert set in symbol
    @staticmethod
    def set_to_char(set_el):
        if set_el == x:
            return 'x'
        elif set_el == y:
            return 'y'
        elif set_el == z:
            return 'z'
        elif set_el == {'1'}:
            return '1'
        elif set_el == {'0'}:
            return '0'

    # is el1 and el2 opposite or not
    @staticmethod
    def res_y(el1, el2):
        return (el1 == '1' and el2 == '0') or (el1 == '0' and el2 == '1')

    def find_all(self, a):
        res = set()
        start = 0
        while str(self).find(a, start) != -1:
            start = str(self).find(a, start) + 1
            res.add(start - 1)
        return res

    def difference(self, b):
        # is diffrence void or not
        def res_void(cube):
            for el in cube.string:
                if Cube.char_to_set(el) != z:
                    return False
            return True

        # get middle cube
        c = Cube()
        if len(self) != len(b):
            return set()
        for i in range(len(self)):
            if Cube.res_y(self.string[i], b.string[i]):
                c.update(y)
                return {self}
            res = Cube.char_to_set(self.string[i]) - Cube.char_to_set(b.string[i])
            c.update(res)
        if res_void(c):
            return set()
        # gets all cubes
        cubes_set = set()
        for i in set(set(range(len(c))) - c.find_all('z')):
            cube_to_add = Cube()

            for j in range(len(self)):
                if i == j and c.string[j] != 'z':
                    cube_to_add.update(c.string[j])
                    continue
                cube_to_add.update(self.string[j])
            cubes_set.add(cube_to_add)
        return cubes_set

    def multi(self, b):
        y_count = 0

        c = Cube()
        if len(self) != len(b):
            return None
        for i in range(len(self)):
            if Cube.res_y(self.string[i], b.string[i]):
                c.update(y)
                y_count += 1
                if y_count > 1:
                    return None
                continue
            res = Cube.char_to_set(self.string[i]) & Cube.char_to_set(b.string[i])
            c.update(res)

        res = Cube()
        for el in c.string:
            if Cube.char_to_set(el) == y:
                res.update(x)
                continue
            res.update(el)

        return res

    def intersection(self, b):
        c = Cube()
        if len(self) != len(b):
            return None
        for i in range(len(self)):
            if Cube.res_y(self.string[i], b.string[i]):
                c.update(y)
                return None
            res = Cube.char_to_set(self.string[i]) & Cube.char_to_set(b.string[i])
            c.update(res)

        res = Cube()
        for el in c.string:
            if Cube.char_to_set(el) == y:
                res.update(x)
                continue
            res.update(el)

        return res

    def __repr__(self):
        return self.string

    def __eq__(self, other):
        return self.string == other.string

    def __len__(self):
        return len(self.string)

    def __hash__(self):
        return hash(self.string)