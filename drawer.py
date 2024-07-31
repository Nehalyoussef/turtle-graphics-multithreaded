import queue
import threading
import turtle

RECTANGLE_WIDTH = 100
RECTANGLE_HEIGHT = 200


class Drawer():
    def __init__(self,width,height):
        self.threads_queue = queue.Queue(1)  
        self.circle_drawer = turtle.Turtle(visible=False)
        self.rectangle_drawer = turtle.Turtle(visible=False)
        self._create_threads(width,height)

    def _draw_circle(self):
        for _ in range(360):
            self.threads_queue.put(self.circle_drawer.fd)
            self.threads_queue.put(self.circle_drawer.lt)

    def _draw_rectangle_edge(self,length):
        for _ in range(length):
            self.threads_queue.put(self.rectangle_drawer.fd)
        for _ in range(90):
            self.threads_queue.put(self.rectangle_drawer.rt)

    def _draw_rectangle(self,width,height):
        for _ in range(2):
            self._draw_rectangle_edge(width)
            self._draw_rectangle_edge(height)

    def _create_threads(self,width,height):
        self.draw_circle_thread = threading.Thread(target=self._draw_circle)
        self.draw_circle_thread.daemon = True  
        self.draw_circle_thread.start()
        self.draw_rectangle_thread = threading.Thread(target=self._draw_rectangle, args=(width,height))
        self.draw_rectangle_thread.daemon = True  
        self.draw_rectangle_thread.start()

    def execute_threads(self):
        while not self.threads_queue.empty():
            (self.threads_queue.get())(1)
        if threading.active_count() > 1:
            turtle.ontimer(self.execute_threads, 100)

def main():
    drawer = Drawer(RECTANGLE_WIDTH,RECTANGLE_HEIGHT)
    drawer.execute_threads()

main()
