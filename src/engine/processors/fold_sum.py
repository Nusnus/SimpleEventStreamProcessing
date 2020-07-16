from engine.event_processor import EventProcessor


class FoldSum(EventProcessor):
    """ sums the value of the events in the array, and passes foward the sum """

    def process_event(self, *args, **kwargs) -> None:
        with self._process():
            self._processing_results = sum(args[0])
