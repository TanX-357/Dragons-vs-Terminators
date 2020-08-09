import random


def random_or_none(s):
    """Return a random element of sequence S, or return None if S is empty."""
    assert isinstance(s, list), \
        "random_or_none's argument should be a list but was a %s" % type(
            s).__name__
    if s:
        return random.choice(s)


def dragons_win():
    """Signal that Dragons win."""
    raise DragonsWinException()


def terminators_win():
    """Signal that Terminators win."""
    raise TerminatorsWinException()


def make_slow(action,terminator):
    """Return a new action method that calls ACTION every other turn.

    action -- An action method of some Terminator
    """
    def slow_action(colony):
        if colony.time % 2 == 0:
            action(colony)
    return slow_action


def make_scare(action,terminator):
    """Return a new action method that makes the terminator go backwards.

    action -- An action method of some Terminator
    """
    def scared_action(colony):
        if(terminator.is_scared is True):
            return
        terminator.is_scared = True
        action(colony)
        terminator.is_scared = False
    return scared_action




def apply_effect(effect, terminator, duration):

    """Apply a status effect to a TERMINATOR that lasts for DURATION turns."""

    old_action = terminator.action

    def affected_action(colony):
        nonlocal duration
        if duration:
            effect(old_action, terminator)(colony)
            duration -= 1
        else:
            old_action(colony)

    terminator.action = affected_action



class GameOverException(Exception):
    """Base game over Exception."""
    pass


class DragonsWinException(GameOverException):
    """Exception to signal that the dragons win."""
    pass


class TerminatorsWinException(GameOverException):
    """Exception to signal that the terminators win."""
    pass


def class_method_wrapper(method, pre=None, post=None):
    """Given a class METHOD and two wrapper function, a PRE-function and
    POST-function, first calls the pre-wrapper, calls the wrapped class method,
    and then calls the post-wrapper.

    All wrappers should have the parameters (self, rv, *args). However,
    pre-wrappers will always have `None` passed in as `rv`, since a return
    value has not been evaluated yet.

    """

    def wrapped_method(self, *args):
        pre(self, None, *args) if pre else None
        rv = method(self, *args)
        post(self, rv, *args) if post else None
        return rv

    return wrapped_method


def print_expired_fighters(self, rv, *args):
    """Post-wrapper for Fighter.reduce_armor, and will print a message if the
    fighter has expired (armor reduced to 0).

    """
    if self.armor <= args[0]:
        print('{0}({1}) ran out of armor and expired'.format(
            type(self).__name__, self.place))


def print_thrower_target(self, rv, *args):
    """Prints the target of a ThrowerDragon, if the ThrowerDragon found a target.

    """
    if rv is not None:
        print('{0} targeted {1}'.format(self, rv))
