from typing import List

from engine.event_processor import EventProcessor


class Pipeline:
    """ Manages a pipeline of events processors """

    def __init__(self, pipeline: List[EventProcessor] = None):
        if not pipeline:
            pipeline = []

        self._event_processors = pipeline
        self._reset_active_pipeline()

    def run_indefinitely(self):
        """ We assume this pipeline runs forever (for the sake of simplicity) """
        while True:
            if self._active_pipeline:  # make sure we have at least one processor

                # Take the top processor from the pipeline
                active_processor: EventProcessor = self._active_pipeline.pop(0)

                # Process it
                try:
                    active_processor.process_event(self._last_result)
                except Exception as error:
                    active_processor.on_error(error)

                # If processing was completed successfully, pass the result forward to the next processor
                # or if it is still being processed, reset the pipeline and start again

                if active_processor.is_completed:
                    active_processor_result = active_processor.on_complete()
                    if active_processor.is_filter:
                        if not active_processor_result:
                            self._reset_active_pipeline()
                        # else -> if the event unit passed the filter, pass the event unit to the next processor
                    else:  # pass the processor result to the next processor
                        self._last_result = active_processor_result
                else:
                    self._reset_active_pipeline()
            else:
                self._reset_active_pipeline()

    def _reset_active_pipeline(self):
        """ Resets the active pipeline to the defined pipeline (during initialization) """
        self._active_pipeline = list(self._event_processors)
        self._last_result = None
