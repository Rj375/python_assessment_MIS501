// const x = {}
// x['Foo'] = 'bar';
// x.bar = {
//     'First': 100,
//     'second': 200
// }
// console.log(x.bar['First'] + x['bar'].second)

// printNum(150)
// // f
// function printNum() {
//     console.log(num)
//     var num = 5
// }

// function Banana(diameter){
//     this.color = 'yellow';
//     this.length = length;
//     this.diameter = diameter;
//     this.isYummy = true ;
//     let rot = function() {
//         this.isYummy = !false;
//         console.log(color, length, this.diameter, isYummy)
//     }
//     rot()
// };

// Banana()

const a = [1,2,3]
const b = [...a,4,5]
const c = a
c.push(4)
console.log(a.length) //result is 4
console.log(b.length) //result is 5

const value = 20.0
const result = Number.isInteger(value)
console.log(result) // result is true