import copy, sys

# Arena File Format:
#
# <Available commands, single string of commands>
# <Maze, 2d grid of tiles>
#
# Commands:
# f - Move forwards
# F - Move forwards x2
# b - Move backwards
# B - Move backwards x2
# r - Rotate clockwise (right)
# l - Rotate counter-clockwise (left)
# p - Rotate 180 degrees (flip)
# h - Hold still (do nothing)
#
# Maze tiles
#
# ^ - Initial position (up)
# > - Initial position (right)
# v - Initial position (down)
# < - Initial position (left)
# . - Floor
# # - Wall
# ! - Goal
# O - Pit
# L - Conveyer belt (left)
# R - Conveyer belt (right)
# U - Conveyer belt (up)
# D - Conveyer belt (down)
# + - Clockwise gear
# x - Counter-clockwise gear

class Vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

class PythonBotGame(object):
    def _set_initial_moves(self, moves):
        self.moves = { 'f' : 0
                     , 'F' : 0
                     , 'b' : 0
                     , 'B' : 0
                     , 'r' : 0
                     , 'l' : 0
                     , 'p' : 0
                     , 'h' : 0 }
        for move in moves:
            self.moves[move] = self.moves[move] + 1

    def _set_initial_pos(self):
        for row in range(0, len(self.arena)):
            for col in range(0, len(self.arena[row])):
                if self.arena[row][col] == '^':
                    self.arena[row][col] = '.'
                    self.pos = Vec(row, col)
                    self.direction = 'up'
                    return
                if self.arena[row][col] == '>':
                    self.arena[row][col] = '.'
                    self.pos = Vec(row, col)
                    self.direction = 'right'
                    return
                if self.arena[row][col] == 'v':
                    self.arena[row][col] = '.'
                    self.pos = Vec(row, col)
                    self.direction = 'down'
                    return
                if self.arena[row][col] == '<':
                    self.arena[row][col] = '.'
                    self.pos = Vec(row, col)
                    self.direction = 'left'
                    return
        raise Exception("Missing Goal.")

    def _char_at_pos(self, pos):
        return self.arena[pos.x][pos.y]

    def _is_in_bounds(self, pos):
        return (pos.x >= 0 and pos.x < len(self.arena) and
                pos.y >= 0 and pos.y < len(self.arena[pos.x]))

    def completed(self):
        return self._char_at_pos(self.pos) == '!'

    ##### ACTIONS #####

    def _do_board_action(self):
        def _die():
            self.alive = False
        def _noop():
            pass

        tile = self._char_at_pos(self.pos)
        actions = { 'O' : lambda : _die()
                  , 'L' : lambda : self._move(1, 'left')
                  , 'R' : lambda : self._move(1, 'right')
                  , 'U' : lambda : self._move(1, 'up')
                  , 'D' : lambda : self._move(1, 'down')
                  , '+' : lambda : self._rotate_clockwise()
                  , 'x' : lambda : self._rotate_counterclockwise()
                  , '.' : lambda : _noop()
                  , '#' : lambda : _noop()
                  , '!' : lambda : _noop() }[tile]()

    def _rotate_clockwise(self):
        self.direction = { 'up'    : 'right'
                         , 'right' : 'down'
                         , 'down'  : 'left'
                         , 'left'  : 'up' }[self.direction]

    def _rotate_counterclockwise(self):
        self.direction = { 'up'    : 'left'
                         , 'right' : 'up'
                         , 'down'  : 'right'
                         , 'left'  : 'down' }[self.direction]

    def _move(self, amt, direction):
        delta = { 'up'    : Vec(-amt, 0)
                , 'right' : Vec(0, amt)
                , 'down'  : Vec(amt, 0)
                , 'left'  : Vec(0, -amt) }[direction]
        new_pos = self.pos + delta
        if not self._is_in_bounds(new_pos):
            self.alive = False
        elif self._char_at_pos(new_pos) == 'O':
            self.alive = False
        elif not self._char_at_pos(new_pos) == '#':
            self.pos = new_pos

    def do_action(self, cmd):
        def _flip():
            self._rotate_clockwise()
            self._rotate_clockwise()

        def _hold():
            pass

        def _move_forwards2(direction):
            self._move(1, direction)
            self._move(1, direction)

        def _move_backwards2(direction):
            self._move(-1, direction)
            self._move(-1, direction)

        if not self.alive or self.completed():
            return
        elif self.moves[cmd] <= 0:
            print 'Error: out of {0} function calls!'.format(self._pp_move(cmd))
        else:
            self.moves[cmd] = self.moves[cmd] - 1
            actions = { 'f' : lambda : self._move(1, self.direction)
                      , 'F' : lambda : _move_forwards2(self.direction)
                      , 'b' : lambda : self._move(-1, self.direction)
                      , 'B' : lambda : _move_backwards2(self.direction)
                      , 'r' : lambda : self._rotate_clockwise()
                      , 'l' : lambda : self._rotate_counterclockwise()
                      , 'p' : lambda : _flip()
                      , 'h' : lambda : _hold()
                      }[cmd]()
            self._do_board_action()

    ##### SUPPORT #####

    def __init__(self, moves, lines):
        self.arena = [[ch for ch in line] for line in lines]
        self._set_initial_moves(moves)
        self._set_initial_pos()
        self.alive = True

    def _pp_move(self, move):
        return { 'f' : 'forwards()'
               , 'F' : 'forwards2()'
               , 'b' : 'backwards()'
               , 'B' : 'backwards2()'
               , 'r' : 'rotate_clockwise()'
               , 'l' : 'rotate_counterclockwise()'
               , 'p' : 'flip()'
               , 'h' : 'hold()' }[move]

    def __str__(self):
        if (not self.alive):
            return 'Destroyed!'
        elif (self.completed()):
            return 'Completed!'
        else:
            board = copy.deepcopy(self.arena)
            board[self.pos.x][self.pos.y] = { 'up'    : '^'
                                            , 'right' : '>'
                                            , 'down'  : 'v'
                                            , 'left'  : '<' }[self.direction]
            moves = [(self._pp_move(move), self.moves[move]) for move in self.moves.keys()]
            return '\n===== Board State =====\n{0}\n\n===== Moves =====\n{1}\n'  \
                   .format('\n'.join([''.join(line) for line in board])
                          ,'\n'.join(['{0}: {1}'.format(move[0], move[1]) for move in moves]))

##### GLOBAL FUNCTIONS #####

state = None

def print_state():
    print state

def forwards():
    state.do_action('f')
    print_state()

def forwards2():
    state.do_action('F')
    print_state()

def backwards():
    state.do_action('b')
    print_state()

def backwards2():
    state.do_action('B')
    print_state()

def rotate_clockwise():
    state.do_action('r')
    print_state()

def rotate_counterclockwise():
    state.do_action('l')
    print_state()

def flip():
    state.do_action('p')
    print_state()

def hold():
    state.do_action('h')
    print_state()

def init_game(filename):
    global state
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        state = PythonBotGame(lines[0], lines[1:])
    print_state()

def main(args):
    if len(args) <> 2:
        print 'Usage: {0} <arena file>'.format(args[0])
    else:
        _init_pythonbotgame_state(args[1])
        print state

#if __name__ == '__main__':
#    main(sys.argv)
