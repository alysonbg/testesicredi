class Orders:
    def combine_orders(self, requests, n_max):
        """
        Returns the amount of travels that are required to fulfill an agency request
        """
        number_of_travels = 0
        index = 0

        while index < len(requests) - 1:
            if requests[index] + requests[index + 1] < n_max:
                number_of_travels += 1
                index += 2

            else:
                number_of_travels += 1
                index += 1

        return number_of_travels
