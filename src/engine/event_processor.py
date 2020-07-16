from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any


class EventProcessor(ABC):
    """ Defines an event unit processor """

    def __init__(self):
        self._processing_results = None
        self._completed = False

    @property
    def is_completed(self) -> bool:
        """ Returns True if the processing was finished or False if not """
        return self._completed

    @property
    def is_filter(self) -> bool:
        """ Filters are special processors which have a boolean result, 
        this checks if the processor is a filter processor """

        # Defaults to false unless overriden
        return False

    @abstractmethod
    def process_event(self, *args, **kwargs) -> None:
        """ Main processing logic of the processor """
        # Implement like this
        # with self._process():
        #     processing logic..

    def on_complete(self) -> Any:
        """ Needs to be called when the processing was completed to get the results """

        if self.is_completed:
            return self._processing_results
        else:
            return None

    def on_error(self, error: Exception = None) -> None:
        """ Defines how errors are handled for this processor """
        self._completed = False

        if not error:
            error = RuntimeError(
                f'Event processor "{self.__class__.__name__}" failed.'
            )

        raise error

    @contextmanager
    def _process(self, autocomplete: bool = True):
        """ Utility context for setting the complete flag accordingly """

        try:
            self._completed = False
            yield

        finally:
            if autocomplete:
                self._completed = True
