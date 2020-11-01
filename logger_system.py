class Logger:
    """
    Purpose: A logger system that receives a stream of messages along with timestamp,
    each message printed if and only if not printed in the last 10 seconds.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log:
            self.log[message] = timestamp
            return True
        else: 
            if timestamp - self.log[message] < 10:
                return False
            else:
                self.log[message] = timestamp
                return True
                
if __name__ == "__main__":
    logger = Logger()
    
    assert logger.shouldPrintMessage(1, "foo") == True
    assert logger.shouldPrintMessage(2, "bar") == True
    assert logger.shouldPrintMessage(3, "foo") == False
    assert logger.shouldPrintMessage(8, "bar") == False
    assert logger.shouldPrintMessage(11, "foo") == True

    print("Logger test passes")
