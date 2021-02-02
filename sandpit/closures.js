function Counter(inc){
  var count = 0; // private member

  var api = {};

  // private method
  var report = function(){
    console.log("Current count: " + count);
  }
  // public methods are added to the api and returned to the caller
  api.add = function(){
    count += inc;
    report();
  };
  api.sub = function(){
    count -= inc;
    report();
  };
  api.reset = function(){
    count = 0;
    console.log("Counter reset to 0");
  }

  return api;
};

var cntr = Counter(3);
cntr.add();
cntr.add();
cntr.sub();
cntr.reset();
