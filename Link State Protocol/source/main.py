import manager, router
import os

manager = manager.Manager()
init_config = manager.make_table()


# os.spawnv()
# pid = os.fork()
#
# if pid > 0:
#     os.fork()
#
# # pid greater than 0 represents
# # the parent process
# if pid > 0:
#     print("I am parent process:")
#     print("Process ID:", os.getpid())
#     print("Child's process ID:", pid)
#
# # pid equal to 0 represnts
# # the created child process
# else:
#     print("\nI am child process:")
#     print("Process ID:", os.getpid())
#     print("Parent's process ID:", os.getppid())
