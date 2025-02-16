# Python Observer Pattern

This project demonstrates a simple implementation of the Observer pattern in Python.

## Overview

The Observer pattern is used to create a one-to-many dependency between objects so that when one object (the Subject) changes state, all its dependents (Observers) are notified automatically.

## Project Structure

- **src/base.py**  
  Defines abstract base classes for the observer and subject. Any concrete implementations must extend these classes.

- **src/subject.py**  
  Contains the `Subject` class which maintains a list of observers. It provides methods to subscribe, unsubscribe, and notify observers when a message is published.

- **src/observer.py**  
  Provides concrete implementations of `BaseObserver` with `PrintObserver` and `LogObserver` that implement the `update` method to handle notifications.

- **main.py**  
  Demonstrates the usage of the observer implementation by creating a `Subject`, subscribing observers to it, and then publishing a message.

## How It Works

1. **Subscription:**  
   Observers subscribe to the subject using the `subscribe()` method in `Subject`. The `Subject` stores these observers in an internal list.

2. **Notification:**  
   When the state or value changes, the `Subject` calls its `notify()` method. This method iterates over the list of observers and calls the `update()` method on each.

3. **Observer Update:**  
   The concrete observer classes (`PrintObserver` and `LogObserver`) implement the `update()` method to define custom behavior upon receiving a notification.

## Running the Example

To see the observer implementation in action:

1. Ensure you have Python installed.
2. Navigate to the project directory.
3. Run the `main.py` file:

```bash
python main.py