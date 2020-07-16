from engine.event_processor import EventProcessor
from types import FunctionType


class Filter(EventProcessor):
    """ only passes events that match a predicate. 
    The predicate is given during initialization time of the filter """

    def __init__(self, filter_callback: FunctionType):
        super().__init__()
        self._filter_callback = filter_callback

    @property
    def is_filter(self) -> bool:
        return True

    def process_event(self, *args, **kwargs) -> None:
        with self._process():
            self._processing_results = self._filter_callback(args[0])
