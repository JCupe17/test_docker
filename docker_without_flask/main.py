#!/bin/python3

import os
import sys
from sparseArray import SparseArray


if __name__ == '__main__':

    # Verify the number of arguments to run the script
    if len(sys.argv) > 2:
        print("[ERROR] Expected 2 arguments but got {} arguments.".format(len(sys.argv)))
    else:
        # Prepare the sparseArray instance
        stringData = open(os.environ['INPUT_PATH'], mode='r').read().splitlines()
        sparseArray = SparseArray(stringData)
        print(sparseArray)

        # Prepare the query
        query = sys.argv[1]
        query = query.split(',')

        # Prepare the output result
        queryResult = sparseArray.matching_strings(query)
        queryDict = {k: v for k, v in zip(query, queryResult)}

        print("{}".format(queryDict))
