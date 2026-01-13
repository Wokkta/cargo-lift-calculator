class CargoLiftCalculator:
    def floor_price(self, weight, floor):
        floors = max(0, floor - 1)
        units = (weight + 99) // 100
        return 300 * floors * units
