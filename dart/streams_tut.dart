import 'dart:async';

class Cake {}

/// Cake order that only carries the type/flavour
class Order {
  Order(this.type);
  String type;
}

void main() {
  // new order for a cake
  final order = Order('chocolate');
  
  // controller to take in the order
  final controller = StreamController();
  
  // transforms the order into an actual cake
  // StreamTransformers can be chained to check for different things
  final baker = StreamTransformer.fromHandlers(
    handleData: (cakeType, sink) {
      if (cakeType == 'chocolate') {
        sink.add(Cake());
      } else {
        sink.addError('Can\'t bake that type');
      }
    }
  );
  
  // sink takes order and passes to stream
  controller.sink.add(order);

  // map checks order type
  // transform sends order to baker
  // second sink created at transform
  // listen returns the output from baker
  controller.stream
    .map((order) => order.type)
    .transform(baker)
    .listen(
      (cake) => print("Here's your cake $cake"),
      onError: (err) => print(err)
  );
}