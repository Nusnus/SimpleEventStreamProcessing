from engine.pipeline import Pipeline
from engine.processors.stdin_source import StdinSource
from engine.processors.filter import Filter
from engine.processors.fixed_event_window import FixedEventWindow
from engine.processors.fold_sum import FoldSum
from engine.processors.fold_median import FoldMedian
from engine.processors.stdout_sink import StdoutSink

if __name__ == '__main__':
    example_pipeline = Pipeline([
        StdinSource(),
        Filter(lambda event_unit: event_unit > 0),
        FixedEventWindow(2),
        FoldSum(),
        FixedEventWindow(3),
        FoldMedian(),
        StdoutSink()
    ])

    example_pipeline.run_indefinitely()
