# Release 1.1.0
 CargoLiftCalculator:
    def floor_price(self, weight, floor):
        floors = max(0, floor - 1)
        units = (weight + 99) // 100
        return 300 * floors * units
    def base_price(self, weight):
        if weight <= 50:
            return 300
        elif weight <= 100:
            return 1000
        elif weight <= 300:
            return 2000
        else:
            raise ValueError("Weight too large")
