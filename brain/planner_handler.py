from planner.planner import plan
from planner.executor import execute_plan


def handle(user):

    steps = plan(user)

    if not steps:
        return None

    return execute_plan(user, steps)