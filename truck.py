class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # in order to put the maximum number of units in the truck, we have to
        # access the per_box efficiency. i.e. which type of box contains the most units.
        # we have to sort the boxes from "most_units_per_box" to "least_units_per_box"
        # then assign boxes to the truck, until the capacity is full.

        boxTypes = [list(reversed(i)) for i in boxTypes]
        boxTypes.sort(reverse = True)
        max_unit, check_size = 0, 0
        for i in boxTypes:
            if check_size == truckSize:
                return max_unit
            if truckSize - check_size >= i[1]:
                max_unit += i[1] * i[0]
                check_size += i[1]
            else:
                max_unit += (truckSize - check_size) * i[0]
                check_size += truckSize - check_size

        return max_unit





