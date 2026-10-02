from .model import SystemState, Timing, UnresolvedSourceEquation, UserState

class PNE017Environment:
    scientific_ready = False

    def __init__(self, users: int, timing: Timing | None = None):
        if users < 1:
            raise ValueError("users must be positive")
        self.timing = timing or Timing()
        self.state = SystemState(users=[UserState() for _ in range(users)])

    def reset(self):
        self.state = SystemState(users=[UserState() for _ in self.state.users])
        return self.state

    def step(self, action):
        raise UnresolvedSourceEquation("Scientific dynamics disabled until SR01-SR14 are resolved.")

    def run_scientific_experiment(self, *args, **kwargs):
        raise UnresolvedSourceEquation("Fidelity gate not satisfied; scientific execution prohibited.")
