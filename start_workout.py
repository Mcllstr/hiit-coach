import os
import time
import threading
import random
import functools

positive_affirmations = ["you're doing better than expected human",
                         "good work!",
                         "you get cake after this. Just kidding.  that was a joke",
                         "29 isn't a bad age",
                         "you're beautiful!",
                         "keep going",
                         "you can fly! you can literally fly!  Where is the stairwell to the roof?",
                         ]

# def finish_wrapper(func):
#     @functools.wraps(func)
#     def inner_wrapper(*args):
#         func(*args)
#         return announce("HIT workout complete.  Great work, give yourself a pat on the backup drive.")
#     return inner_wrapper()

def announce(announcement):
    print(announcement)
    os.system(f'say {announcement}')

def thread_announcements(announcement):
    thread_ = threading.Thread(target=announce, args=(announcement,))
    thread_.start()

# @finish_wrapper
def start_workout(exercises, num_cycles):
    time_interval = 5
    sprint_duration = 6 * time_interval
    rest_duration = 2 * time_interval
    announce(
        f'prepare for vigorous activity, human! you will go hard for {sprint_duration} seconds and rest for {rest_duration} seconds for each exercise')
    time.sleep(3)

    def all_excercises_once(exercises=exercises):

        def countdown(sprint_type, duration):
            thread_announcements(sprint_type)
            for i in list(range(0, duration, time_interval))[::-1]:
                time.sleep(time_interval)
                thread_announcements(i)
            return

        def one_cycle():
            countdown('begin!', sprint_duration)
            random_int = random.randint(1, 101)
            if random_int >70:
                thread_announcements(random.choice(positive_affirmations))

            countdown('begin rest', rest_duration)
            return

        for an_excercise in exercises:
            announce(f'now do {an_excercise}.')
            time.sleep(2)
            one_cycle()

        thread_announcements('Cycle finished.')
        return

    for i, a_full_cycle in enumerate(list(range(0, num_cycles))):
        all_excercises_once()
        if i != num_cycles-1:
            thread_announcements('Take a water break, you have 20 seconds.')
            time.sleep(20)
        else:
            announce("HIT workout complete.  Great work, give yourself a pat on the backup drive.")

    # announce('start')
    # for i in list(range(0,sprint_duration, time_interval))[::-1]:
    #     time.sleep(time_interval)
    #     thread_ = threading.Thread(target=announce, args=(i,))
    #     thread_.start()

if __name__ == '__main__':
    exercises = ['predator squats! '*3, 'plank! '*3, 'lunge! '*3, 'burpee! '*3, 'side skates! '*3, 'push-up! '*3, 'high-knee! '*3, 'jumping jacks! '*3]
    init_time = time.time()
    start_workout(exercises=exercises, num_cycles=1)
    print(time.time()-init_time)

