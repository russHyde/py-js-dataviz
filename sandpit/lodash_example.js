// countBy value

var items = ["F", "C", "C", "A", "B", "A", "C", "E", "F"];

console.log(_.countBy(items));

// groupBy and average

var journeys = [
  { period: "morning", times: [44, 34, 56, 31] },
  { period: "evening", times: [35, 33] },
  { period: "morning", times: [33, 29, 35, 41] },
  { period: "evening", times: [24, 45, 27] },
  { period: "morning", times: [18, 23, 28] },
];

var groups = _.groupBy(journeys, "period");

var mTimes = _.map(groups["morning"], "times");
mTimes = _.flatten(mTimes);
var average = function (l) {
  var sum = _.reduce(
    l,
    function (a, b) {
      return a + b;
    },
    0
  );
  return sum / l.length;
};
console.log("Average morning time is " + average(mTimes));

// filter / map / reduce
//
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var isOdd = function (x) {
  return x % 2;
};

var sum = nums
  .filter(isOdd)
  .map(function (o) {
    return o * o;
  })
  .reduce(function (a, b) {
    return a + b;
  });

console.log("Sum of the odd squares is " + sum);
