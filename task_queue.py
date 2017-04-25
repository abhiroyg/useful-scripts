from diskcache import Cache

task_queue = Cache('/tmp/ad-poster')
# print dir(task_queue)
print "Count:", task_queue.count
print "Cleared:", task_queue.clear()
