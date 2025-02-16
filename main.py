from src.observer import LogObserver, PrintObserver
from src.subject import Subject


def main():
    subject = Subject()
    
    log_observer = LogObserver()
    print_observer = PrintObserver()
    
    
    subject.subscribe(log_observer)
    subject.subscribe(print_observer)
    subject.notify("Haloo semua !")
    subject.unsubscribe(log_observer)
    subject.notify('Ciao!')

if __name__ == '__main__':
    main()