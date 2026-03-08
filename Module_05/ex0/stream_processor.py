from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")

        total = sum(data)
        avg = total / len(data) if data else 0
        result = (
            f"Processed {len(data)} numeric values, sum={total}, avg={avg}"
        )
        formatted = self.format_output(result)
        return (
            f"Processing data: {data}\n"
            "Validation: Numeric data verified\n"
            f"Output: {formatted}"
        )

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for
                                              x in data)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")

        total = len(data)
        words = len(data.split())
        result = (
            f"Processed text: {total} characters, {words} words"
        )
        formatted = self.format_output(result)
        """ligne 55 inutile pour ce code la mais bien par convention pour
        pouvoir modifier facilement la fonction"""
        return (
            f"""Processing data: "{data}"\n"""
            "Validation: Text data verified\n"
            f"Output: {formatted}"
        )

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(f"""Processing data: "{data}" """)
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        print("Validation: Log entry verified")
        sep = data.split(":", 1)
        level = sep[0]
        message = sep[1].strip() if len(sep) > 1 else ""
        result = f"{level} level detected: {message}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result: str) -> str:
        type = "[INFO]"
        if "ERROR" in result:
            type = "[ALERT]"
        return f"Output: {type} {super().format_output(result)}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    num_process = NumericProcessor()
    num_data = [1, 2, 3, 4, 5]
    try:
        print(f"{num_process.process(num_data)}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nInitializing Text Processor...")
    text_process = TextProcessor()
    text_data = "Hello Nexus World"
    try:
        print(f"{text_process.process(text_data)}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nInitializing Log Processor...")
    log_process = LogProcessor()
    log_data = "ERROR: Connection timeout"
    try:
        print(f"{log_process.process(log_data)}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    tasks = [
        (num_process, [1, 2, 3]),
        (text_process, "Hello Python"),
        (log_process, "INFO: System ready")
    ]
    count = 1
    for proc, data in tasks:
        try:
            result = proc.process(data)
            print(f"Result {count}: {result}")
            count += 1
        except ValueError as e:
            print(f"Skipping invalid data: {e}")


if __name__ == "__main__":
    main()
