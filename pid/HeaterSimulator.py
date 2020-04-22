class HeaterSimulator:
    def __init__(self, mass=1, heater_power=10, temperature=30, specific_heat=4186, cooler_power=5):
        # KG
        self.mass = mass
        # Heating element power in Watts (Joules/second)
        self.heater_power = heater_power
        # Temperature in degrees celsius
        self.temperature = temperature
        # Amount of needed to increase 1kg of said mass in 1 degree
        self.specific_heat = specific_heat
        # Internal energy in Joules
        self.energy = specific_heat * mass * temperature
        # Loss of energy to the environment proportional to a delta of 1 degree to the ambient temperature
        self.cooler_power = cooler_power
        # Ambient temperature, starts equal to the mass (from equilibrium)
        self.ambient_temperature = temperature

    def dissipation_power(self):
        return self.cooler_power * (self.temperature - self.ambient_temperature)

    def simulate(self, intensity, duration):
        added_heat = self.add_heat(intensity, duration)
        lost_heat = self.remove_heat(duration)
        return {"t": self.temperature, "added_heat": added_heat, "lost_heat": lost_heat }

    def add_heat(self, intensity, duration):
        added_energy = self.heater_power * (intensity / 100) * duration
        self.energy += added_energy
        self.update_temperature()
        return added_energy

    def remove_heat(self, duration):
        dissipated_energy = self.dissipation_power() * duration
        self.energy -= dissipated_energy
        self.update_temperature()
        return dissipated_energy

    def update_temperature(self):
        self.temperature = self.energy / (self.specific_heat * self.mass)
