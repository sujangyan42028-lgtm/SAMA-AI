import threading

def run_background(function, *args):
    thread = threading.Thread(
        target=function,
        args=args,
        daemon=True
    )
    thread.start()
    return thread