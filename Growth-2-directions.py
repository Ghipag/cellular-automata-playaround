import cellpylib as cpl

# initial point
cellular_automaton = cpl.init_simple2d(480, 480)
cellular_automaton[:, [240], [240]] = 1

# Rule Table
#(center,north,east,south,west)
ctrbl_rule = cpl.CTRBLRule(rule_table={
    (1, 0, 0, 0, 0): 1,
    (0, 1, 0, 0, 0): 0,
    (0, 0, 1, 0, 0): 0,
    (0, 0, 0, 1, 0): 1,
    (0, 0, 0, 0, 1): 1,
    (0, 0, 0, 0, 0): 0,
    (1, 0, 1, 0, 0): 1,
    (1, 0, 1, 0, 1): 1,
    (1, 0, 0, 0, 1): 1,
    (1, 0, 0, 1, 0): 1,
    (1, 1, 1, 0, 0): 1,
    (1, 1, 1, 0, 1): 1,
    (0, 1, 0, 1, 0): 1,
    (0, 0, 1, 1, 0): 0,
    (1, 1, 1, 1, 1): 0,
    (0, 1, 1, 1, 1): 0,
    (0, 0, 0, 1, 1): 0,
    (0, 1, 1, 0, 0): 0,
    (0, 1, 0, 1, 1): 0,
    (1, 0, 0, 1, 1): 0,
    (0, 0, 1, 0, 1): 0,
    (0, 0, 1, 1, 1): 0,
    (0, 1, 1, 1, 0): 0,
    (0, 1, 0, 0, 1): 0,
    (1, 1, 0, 0, 0): 0,
    (1, 1, 0, 1, 0): 0,
    (1, 1, 0, 1, 1): 0,
    (1, 1, 1, 1, 0): 0,
    (1, 0, 1, 1, 1): 0,
    (1, 0, 1, 1, 0): 0,
    (1, 1, 0, 0, 1): 0,
    (0, 1, 1, 0, 1): 0
    }, add_rotations= False)

# evolve the cellular automaton for 60 time steps
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=2000, neighbourhood='von Neumann',
                                  apply_rule=ctrbl_rule, memoize='recursive')


cpl.plot2d_animate(cellular_automaton)