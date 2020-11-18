class History:
    """
    A representation of the action history for a prisoner's dilemma actioner.
    The history contains a "c" for cooperation and a "d" for defection.
    """
    def __init__(self):
        self.history = []

    def get_length(self):
        """Returns the number of actions in the history"""
        return len(self.history)

    def get_most_recent(self):
        """Returns the most recent action"""
        if len(self.history) == 0:
            raise RuntimeError("cannot get the most recent action from an empty history")
        return self.history[-1]

    def get_num_defects(self):
        """Returns the number of defections in the history"""
        return self.history.count('d')

    def get_num_coops(self):
        """Returns the number of cooperations in the history"""
        return self.history.count('c')

    def has_recent_defect(self, n):
        """Returns `True` if there was a defection in the last `n` actions, otherwise returns `False`"""
        return 'd' in self.history[-n:]

    def has_recent_coop(self, n):
        """Returns `True` if there was a cooperation in the last `n` actions, otherwise returns `False`"""
        return 'c' in self.history[-n:]

    def add_action(self, action):
        """Adds `action` to the end of the history"""
        if action != 'c' and action != 'd':
            raise ValueError("action must be either 'c' or 'd', {} given".format(action))
        self.history.append(action)

    def __iter__(self):
        return iter(self.history)
