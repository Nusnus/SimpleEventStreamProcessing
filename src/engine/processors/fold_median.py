from statistics import median

from engine.event_processor import EventProcessor


class FoldMedian(EventProcessor):
    """ calculate the median value of the events in the array, and pass forward the median. """

    def process_event(self, *args, **kwargs) -> None:
        with self._process():
            self._processing_results = median(args[0])
