class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.slots = {
            'diesel': {
                'current': diesel,
                'max': diesel
            },
            'electric': {
                'current': electric,
                'max': electric
            },
            'petrol': {
                'current': petrol,
                'max': petrol
            }
        }
        
    def fuel_vehicle(self, fuel_type: str) -> bool:
        if fuel_type in self.slots and self.slots[fuel_type]['current'] > 0:
            self.slots[fuel_type]['current'] -= 1
            return True
            
        return False
        
    def open_fuel_slot(self, fuel_type: str) -> bool:
        if fuel_type in self.slots and self.slots[fuel_type]['max'] == self.slots[fuel_type]['current']:
            return False
            
        if fuel_type in self.slots:
            self.slots[fuel_type]['current'] += 1
            return True
            
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
