from typing import List

from engine.event_processor import EventProcessor


class FixedEventWindow(EventProcessor):
    """ aggregates events into a fixed size array, pass it forward when full.
    The size of the fixed array is defined during the initialization of the fixed-event-window. """

    def __init__(self, size: int):
        super().__init__()
        self._array: List[int] = []
        self._size = size

    def process_event(self, *args, **kwargs) -> None:
        # we will manually complete this processing
        with self._process(autocomplete=False):
            if len(self._array) < self._size:
                self._array.append(args[0])

            if len(self._array) == self._size:
                self._processing_results = list(self._array)
                self._array.clear()
                self._completed = True
