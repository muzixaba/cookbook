void main() {
  PowerGrid grid = PowerGrid();
  NuclearPlant nuclear = NuclearPlant();
  SolarPlant solar = SolarPlant();
  
  grid.addPlant(nuclear);
  grid.addPlant(solar);
}

class PowerGrid {
  List<PowerPlant> connectedPlants = [];
  
  addPlant(PowerPlant plant) {
    plant.turnOn();
    connectedPlants.add(plant);
  }
}

/// abstract class to classify types using their methods.
/// if class has turnOn(), it's a PowerPlant
abstract class PowerPlant {
  turnOn();
}

/// NewClass implements AbstractClass
/// At minimum, it has to have the same methods as the AbstractClass
class NuclearPlant implements PowerPlant {
  turnOn() {
    print("Nuclear Plant switched on");
  }
}

class SolarPlant implements PowerPlant {
  
  turnOn() {
    print("Solar plant switched on");
  }
}