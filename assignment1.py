class DataStream:
    def __init__(self):
        self.last_seen = {}
        
    def should_output_data_str(self, timestamp: int, data_str:  str) -> bool:
        if data_str in self.last_seen:
            last_timestamp = self.last_seen[data_str]
            time_since_last_seen = timestamp - last_timestamp
            self.last_seen[data_str] = self.last_seen[data_str] + timestamp
            if time_since_last_seen < 5:
                return False
        
        self.last_seen[data_str] = timestamp
        return True
        
data_stream = DataStream()

print(data_stream.should_output_data_str(0, "hello"))
print(data_stream.should_output_data_str(1, "world"))
print(data_stream.should_output_data_str(6, "hello"))
print(data_stream.should_output_data_str(7, "hello"))
print(data_stream.should_output_data_str(8, "world"))
