# -*- coding: utf-8 -*-
import sys
import time
import subprocess
from modules.monitoring.monitoring import onCreated
#Importaciones del sistema
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#importaciones desde la carpeta módulo
from modules.monitoring.monitoring import onCreated

if __name__ == "__main__":
    print('monitoreando')
    event_handler = PatternMatchingEventHandler(patterns=["*.msg"])
    event_handler.on_created = onCreated
    observer = Observer()
    observer.schedule(event_handler, path='/opt/zimbra/store/', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()