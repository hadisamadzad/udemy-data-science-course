import modules._start as starter

starter.clear_console()

#import modules.logger as logger
from modules.logging import Log

with open('logs.txt') as file:
    for line in file:
        line = line.strip()
        log = Log("Info", line)
        log.log_on_console()

try:
    log2 = Log("", line)
    log2.log_on_console()

    log2.level = "Debug"
    log2.log_on_console()

except RuntimeError as e:
    print(e)