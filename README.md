Goal
The goal of this project is to provide a simple yet effective example of how multithreading can be implemented in Python to handle concurrent tasks. By drawing shapes concurrently, we can see the benefits of multithreading in action.

Multithreading
Multithreading is a technique where multiple threads are created to perform different tasks concurrently. In this project, we use two threads: one for drawing a circle and another for drawing a rectangle. Each thread independently adds drawing commands to a queue, which are then executed in the main thread to perform the drawing. This allows both shapes to be drawn at the same time, demonstrating the efficiency and usefulness of multithreading.
