from queue import Queue

resume_queue = Queue()

resume_queue.put(
    "resume1.pdf"
)

resume = resume_queue.get()

print(
    "Processing:",
    resume
)