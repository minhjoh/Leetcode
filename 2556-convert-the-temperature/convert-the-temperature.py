class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        li = []
        li.append(celsius + 273.15)
        li.append(celsius * 1.8 + 32)
        return li