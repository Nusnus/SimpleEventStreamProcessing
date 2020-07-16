from engine.event_processor import EventProcessor


class StdinSource(EventProcessor):
    """ reads one number from stdin, prints '> ' and the number afterwards, 
    for example: if the user entered 1, it will print '> 1'. """

    def process_event(self, *args, **kwargs) -> None:
        with self._process():
            while True:
                try:
                    self._processing_results = int(input('> '))
                    break
                except Exception:
                    pass  # try again on error
