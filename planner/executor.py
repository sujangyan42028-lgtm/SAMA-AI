from plugins.manager import run_plugin


def execute_plan(user, steps):

    outputs = []

    for step in steps:

        result = run_plugin(step, user)

        if result:

            outputs.append(result)

    return "\n".join(outputs)