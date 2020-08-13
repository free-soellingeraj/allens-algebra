"""
This module contains an open-source implementation of
Allen's interval algebra.

Maintainer: Aaron Soellinger
First commit: August 13, 2020
"""


class InvalidInterval(Exception):
    pass


class IntervalRelation:
    """See: Allen's interval algebra."""
    precedes = 'lt'
    follows = 'gt'
    meets = 'm'
    meets_inv = 'mi'
    overlaps = 'o'
    overlaps_inv = 'oi'
    starts = 's'
    starts_inv = 'si'
    during = 'd'
    during_inv = 'di'
    finishes = 'f'
    finishes_inv = 'fi'
    equals = 'eq'


class allen:
    def __calc__(self, X: dict, Y: dict):
        """
        Compute interval relation of a to b.
        
        In:
            X: dict(s: int, c: int) interval with start (s) and close (c)
            Y: dict(s: int, c: int) interval with start (s) and close (c)
            where s < c
        
        Returns:
            tuple(X {?} Y, Y {?} X) where,
            X {?} Y: IntervalRelation "X is to Y" where (x) is allen's interval algebra
            Y {?} X: IntervalRelation "Y is to X" where (x) is allen's interval algebra
        
        https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
        """
        # start validate interval
        if X['s'] >= X['c']:
            raise InvalidInterval('Interval `a` is invalid.')
        if Y['s'] >= Y['c']:
            raise InvalidInterval('Interval `b` is invalid.')
        # end validate interval
        
        # order them
        if X['c'] > Y['c']:
            x_first = False
            first = Y
            second = X
        else:
            x_first = True
            first = X
            second = Y
        
        if first == second:
            out = (IntervalRelation.equals, IntervalRelation.equals)
        
        elif first['c'] < second['s']:
            out = (IntervalRelation.precedes, IntervalRelation.follows)
        
        elif first['c'] == second['s']:
            out = (IntervalRelation.meets, IntervalRelation.meets_inv)
        
        elif first['s'] < second['s'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntervalRelation.overlaps, IntervalRelation.overlaps_inv)
        
        elif first['s'] == second['s'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntervalRelation.starts, IntervalRelation.starts_inv)
        
        elif first['s'] > second['s'] \
        and \
        first['s'] < second['c'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntervalRelation.during, IntervalRelation.during_inv)
        
        elif first['s'] > second['c'] \
        and \
        first['s'] < second['c'] \
        and \
        first['c'] == second['c']:
            out = (IntervalRelation.finishes, IntervalRelation.finishes_inv)
        
        if x_first:
            return (out[0], out[1])
        
        else:
            return (out[1], out[0])
