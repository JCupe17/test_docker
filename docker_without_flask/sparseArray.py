class SparseArray:
    def __init__(self, stringData):
        self.stringData = stringData

    def __str__(self):
        return "Input Size: {}".format(len(self.stringData))

    def matching_strings(self, stringQuery):
        """
        This function returns the number of matches in stringData
        per element in the stringQuery argument.
        :param stringQuery: an array of query strings
        :return: an integer array of the results of all queries in order
        """
        return [self.stringData.count(q) for q in stringQuery]

