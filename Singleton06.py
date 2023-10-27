class EventTracker:
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.api_url = "http://example.com"

    def track(self):
        print(f"TODO track event at {self.api_url}")


tracker = EventTracker()
print(tracker)
print(tracker.track())
tracker2 = EventTracker()
print(tracker2)
print(tracker2.track())
