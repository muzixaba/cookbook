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

/// abstract class to classify types using their methods & instance variables.
/// if class has turnOn(), it's a PowerPlant
abstract class PowerPlant {
  int costOfEnergy;
  turnOn();
}

abstract class PlantSize {
  int sizeOfPlant;
}

/// NewClass implements AbstractClass
/// At minimum, it has to have the same methods as the AbstractClass
class NuclearPlant implements PowerPlant {
  //instance variables have to have the same name & type
  int costOfEnergy;
  turnOn() {
    print("Nuclear Plant switched on");
  }
}

// A class can implement multiple abstract classes
class SolarPlant implements PowerPlant, PlantSize {
  int costOfEnergy;
  int sizeOfPlant;
  turnOn() {
    print("Solar plant switched on");
  }
}