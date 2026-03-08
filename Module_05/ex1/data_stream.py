from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, List, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = [a for a in data_batch
                        if isinstance(a, (int, float))]
            if not readings:
                return "Sensor analysis: No valid readings"
            total = 0.0
            for r in readings:
                total += r
            avg = total / len(readings)

            return (f"Sensor analysis: {len(readings)} readings processed, "
                    f"avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Error in SensorStream: {str(e)}"
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        numbers = [x for x in data_batch if isinstance(x, (int, float))]
        if criteria == "high_priority":
            return [x for x in numbers if x > 50]
        return numbers


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            ops = [x for x in data_batch if isinstance(x, tuple)
                   and len(x) == 2]
            count = len(ops)
            net = 0
            for op, amount in ops:
                if op == 'buy':
                    net += amount
                elif op == 'sell':
                    net -= amount
            sign = "+" if net >= 0 else ""
            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {sign}{net} units")
        except Exception as e:
            return f"Error in TransactionStream: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        ops = [x for x in data_batch if isinstance(x, tuple)]
        if criteria == "high_priority":
            return [x for x in ops if x[1] >= 150]
        return ops


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [x for x in data_batch if isinstance(x, str)]
            count = len(events)
            errors = [x for x in events if x == "error"]
            error_count = len(errors)
            return (f"Event analysis: {count} events, "
                    f"{error_count} error detected")
        except Exception as e:
            return f"Error in EventStream: {str(e)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        events = [x for x in data_batch if isinstance(x, str)]
        return events


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_mixed_batch(self, data_batch: List[Any]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("")
        print("Batch 1 Results:")
        for stream in self.streams:
            valid_items = stream.filter_data(data_batch)
            count = len(valid_items)
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {count} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {count} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {count} events processed")

    def run_priority_filter(self, data_batch: List[Any]) -> None:
        print("")
        print("Stream filtering active: High-priority data only")
        results = []
        for stream in self.streams:
            filtered = stream.filter_data(data_batch, "high_priority")
            results.append((stream, filtered))
        parts = []
        for stream, data in results:
            count = len(data)
            if count > 0:
                if isinstance(stream, SensorStream):
                    parts.append(f"{count} critical sensor alerts")
                elif isinstance(stream, TransactionStream):
                    parts.append(f"{count} large transactions")
        print(f"Filtered results: {', '.join(parts)}")
        print("")
        print("All streams processed successfully. Nexus throughput optimal.")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("Initializing Sensor Stream...")
    sensor_s = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_s.stream_id}, Type: {sensor_s.stream_type}")
    sensor_input = [28, 10, 225.9]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor_s.process_batch(sensor_input))
    print("")
    print("Initializing Transaction Stream...")
    trans_s = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_s.stream_id}, Type: {trans_s.stream_type}")
    trans_input = [('buy', 100), ('sell', 150), ('buy', 75)]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans_s.process_batch(trans_input))
    print("")
    print("Initializing Event Stream...")
    event_s = EventStream("EVENT_001")
    print(f"Stream ID: {event_s.stream_id}, Type: {event_s.stream_type}")
    event_input = ['login', 'error', 'logout']
    print("Processing event batch: [login, error, logout]")
    print(event_s.process_batch(event_input))
    print("")
    processor = StreamProcessor()
    processor.add_stream(sensor_s)
    processor.add_stream(trans_s)
    processor.add_stream(event_s)
    mixed_batch = [
        60.5, 101.5,
        ('buy', 100), ('sell', 150), ('buy', 75), ('sell', 140),
        'login', 'error', 'logout'
    ]
    processor.process_mixed_batch(mixed_batch)
    processor.run_priority_filter(mixed_batch)


if __name__ == "__main__":
    main()
