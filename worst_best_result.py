#! /usr/bin/env python3

results = [10, 5, 20, 20, 4, 5, 2, 25, 1]
results_2 = [12, 24, 10, 24]

def get_broken_results(results):

    max_result = results[0]
    min_result = results[0]

    min_changes = 0
    max_changes = 0

    for result in results:

        if result < min_result:
            min_result = result
            min_changes += 1

        elif result > max_result:
            max_result = result
            max_changes += 1

        else:
            continue


    print(max_changes, min_changes)

get_broken_results(results)
get_broken_results(results_2)
