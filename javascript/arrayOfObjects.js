let cars = [
    {
      "color": "purple",
      "type": "minivan",
      "registration": new Date('2017-01-03'),
      "capacity": 7
    },
    {
      "color": "red",
      "type": "station wagon",
      "registration": new Date('2018-03-03'),
      "capacity": 5
    }
]

// ADD a new object to array
let car = {
    "color": "red",
    "type": "cabrio",
    "registration": new Date('2016-05-02'),
    "capacity": 1
  }
  // add in first position
  cars.unshift(car);

  // add at the end of the array
  cars.push(car);

// add object in specific position using Splice
// adds a new car in 5th position
cars.splice(4, 0, car)


// FIND an object using a specific attribute. Returns 1st match
let redCar = cars.find(car => car.color === 'red');

// FILTER array of objects. Returns an array
let redCars = cars.filter(car => car.color === 'red');

// New array from array of objects using Map
let sizes = cars.map(car => {
    if (car.capacity <= 3){
        return "small";
    }
    if (car.capacity <= 5){
        return "medium";
    }
    return "large";
})

// Change an object's property in array of objects
const newCars = cars.map(obj => {
    // find object that meets condition & modify attribute
    if (obj.type == "minivan"){
        return {...obj, color: 'blue'};
    }
    // else return object as is
    return obj;
})

// Update a property of a single object
for (const obj of cars){
    if (obj.type === 'minivan'){
        obj.capacity = 10;
        // exit loop afterwards
        break;
    }
}
// console.log(cars);


// Add a property to every object in array using forEach
cars.forEach(car => {
    car['size'] = 'large';
    if (car.capacity <= 5){
        car['size'] = 'medium';
    }
    if (car.capacity <= 3){
        car['size'] = 'small';
    }
})

// Sort array of objects using a certain attribute
let sortedCars = cars.sort((c1, c2) => (c1.capacity < c2.capacity) ? 1 : (c1.capacity > c2.capacity) ? -1 : 0);

// Check if SOME objects fulfill a condition
cars.some(car => car.color === 'red' && car.type === 'cabrio');

// Check if ALL objects fulfill a condition
cars.every(car => car.color === 'red' && car.type === 'cabrio');