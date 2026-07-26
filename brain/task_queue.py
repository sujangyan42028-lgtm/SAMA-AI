def split_tasks(user):

    user = user.lower()

    separators = [
        " and ",
        " then ",
        ",",
        " after that "
    ]

    tasks = [user]

    for sep in separators:

        new_tasks = []

        for task in tasks:
            new_tasks.extend(task.split(sep))

        tasks = new_tasks

    tasks = [t.strip() for t in tasks if t.strip()]

    return tasks