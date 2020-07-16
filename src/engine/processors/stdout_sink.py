from engine.event_processor import EventProcessor


class StdoutSink(EventProcessor):
    """ prints the number to stdout and pass forward the number """

    def process_event(self, *args, **kwargs) -> None:
        with self._process():
            print(str(args[0]))
