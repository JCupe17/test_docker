class SparseArray:
    def __init__(self, stringData):
        self.stringData = stringData
        self.querySize = 0

    def __str__(self):
        return "Input Size: {}".format(len(self.stringData))

    def matching_strings(self, stringQuery):
        """
        This function returns the number of matches in stringData
        per element in the stringQuery argument.
        :param stringQuery: an array of query strings
        :return: an integer array of the results of all queries in order
        """
        self.update_query_size(len(stringQuery))

        return [self.stringData.count(q) for q in stringQuery]

    def update_query_size(self, value):
        """
        This function updates the size of the last queryString passed to
        the class.
        :param value: value to update the querySize
        :return: None
        """
        self.querySize = value
