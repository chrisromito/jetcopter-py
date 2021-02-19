"""
    Main event loop runs here for 2 reasons:
    1. So we can use the REPL, since it doesn't get imported into "main.py" EVERY time
    2. main.py checks dependencies that this, and other modules, may require at runtime

    See here for more info regarding asyncio & running async loops forever:
        https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#224-a-typical-firmware-app
"""
import uasyncio as asyncio


class App:

    def __init__(self):
        self.run = True

    def run_forever(self):
        """
        FIXME: Make this do something
        """
        while self.run:
            pass


def set_global_exception():
    def handle_exception(loop, context):
        import sys
        sys.print_exception(context["exception"])
        sys.exit()
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)

async def main():
    set_global_exception()  # Debug aid
    app = App()  # Constructor might create tasks
    # asyncio.create_task(app.foo())  # Or you might do this
    await app.run_forever()  # Non-terminating method


def runtime():
    try:
        asyncio.run(main())
    finally:
        asyncio.new_event_loop()  # Clear retained state
