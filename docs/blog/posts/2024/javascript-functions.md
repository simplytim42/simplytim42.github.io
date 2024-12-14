---
draft: true
authors:
  - tim
date:
  created: 1900-01-01
categories:
  - JavaScript
tags:
  - functions
  - programming
  - javascript
description: From basics to advanced concepts, explore how functions can enhance your JavaScript projects.
title: Enhance Your JavaScript Functions
series: Essential JavaScript
---

Explore the world of JavaScript functions and see how mastering them can enhance your programming projects. Whether you're just getting started or looking to deepen your understanding, this guide covers everything from basic function declarations to more advanced topics like Higher-Order Functions and Closures. By exploring these concepts, you'll learn to write cleaner code and leverage JavaScript's full potential.

<!-- more -->

!!! tip
    _As we go through these functions, take note of how they often overlap and are used in combination with each other._

## Beginner: Billy Basics
### The Function
This is the function that most people are familiar with. It is simple and easy to understand. In this example we first declare the function and then call (execute) it.
```javascript
function greet(name) {
  return `Hello, ${name}`;
}

console.log(greet("Kaladin"));
// Expected output: Hello, Kaladin
```

### Function Expression
This is where a function is assigned to a variable. This enables it to be passed into other functions or allow for a function to be created conditionally.
```javascript
const add = function (a, b) {
  return a + b;
};

console.log(add(10, 32));
// Expected output: 42
```
If you're new to programming you might ask "_Why is this useful?_". As an example, some built in JS functions like `.filter()` allow you to pass in another function that determines how you want to filter the data.

### Arrow Functions
_Introduced in ES6._
A more streamline way to write functions. Mainly used as an efficient replacement for Function Expressions and Anonymous Functions.

If the function only needs one statement, you can fit it all onto one line and remove the curly braces and `return` keyword:
```javascript
const greet = (name) => `Hello, ${name}`;

console.log(greet("Kaladin"));
// Expected output: Hello, Kaladin
```

If you need more than one statement then you do need the curly braces and `return` keyword:
```javascript
const greet = (name) => {
  if (name === "Sadeas") return null;
  return `Hello, ${name}`;
};

console.log(greet("Kaladin"));
// Expected output: Hello, Kaladin
```

## Intermediate: Dial it Up a Notch
### Anonymous Functions
A function that has no name. We can use them to reduce the syntax required for Function Expressions by combining it with Arrow Function syntax:
```javascript
const sayHi = () => console.log("Hi!");

sayHi();
// Expected output: Hi!
```

It is also commonly used when you need to pass a function into another function, such as `.map()` or `.filter()`)
```javascript
const doubled = [1, 2, 3].map((num) => {
  return num * 2;
});

console.log(doubled);
// Expected output: [2, 4, 6]
```

### Immediately Invoked Function Expression (IIFE)
This is an Anonymous Function that is called immediately at runtime.
```javascript
(function () {
  console.log("I run right away!");
})();
```

It allows us to have finer control over the scope of variables and not litter the global namespace.
```javascript
let foo = "Global Scope";

(function () {
  let foo = "Local Scope";
  console.log(foo);
  // Expected output: Local Scope
})();

console.log(foo);
// Expected output: Global Scope
```

IIFEs are less common these days thanks to JS modules and `const`/`let` keywords giving us more control over scoped variables. But you will still find it in legacy code so it's worth knowing.

<figure markdown="span">
  ![Modules of reusable code represented as blocks](https://raw.githubusercontent.com/simplytim42/turbo-umbrella/refs/heads/main/tstd/programming/modules.webp){ width="600", loading=lazy, main-image }
</figure>

## Advanced: The Pro-Zone
### Higher-Order Functions
These are functions that can take other functions as arguments _AND/OR_ return a function. This first example creates a Higher-Order Function called `stick` which takes and executes another function (commonly called a 'callback' function). Note that whatever callback function is passed into `stick()`, it will always be given the same argument of `"I am a stick"`.
```javascript
function stick(callback) {
  console.log(callback("I am a stick"));
}

stick((string) => string.toUpperCase());
// Expected output: I AM A STICK

function getLength(string) {
  return string.length;
}
stick(getLength);
// Expected output: 12
```

This example, however, uses the argument passed in to decide which function to return. It is the returning of a function that makes `chooseCharacter` a Higher-Order Function:
```javascript
function chooseCharacter(type) {
  // return an arrow function
  if (type === "leader") return () => "Dalinar";

  // return a named function...because you're a rebel!
  if (type === "scholar") {
    return function veryCleverPeeps() {
      return "Jasnah";
    };
  }
}

const scholar = chooseCharacter("scholar");
console.log(scholar());
// Expected output: Jasnah

const leader = chooseCharacter("leader");
console.log(leader());
// Expected output: Dalinar
```

### Closures
A closure is a function that 'remembers' the _enclosing_ scope. In this example we have a local variable that is essentially 'hidden' from the global scope. But the returned function still 'remembers' it.
```javascript
function theEnclosure() {
  const secret = "Do not reveal me. I am hiding from global scope!";
  return function traitor() {
    console.log(secret);
  };
}
const revealSecret = theEnclosure();
revealSecret();
// `revealSecret()` has access to the scoped variables from `theEnclosure()`
// Expected output: Do not reveal me. I am hiding from global scope!
```

Closures can also be used to influence the behaviour of the returned function such as in this example:
```javascript
function createMultiplier(multiplier) {
  return function (num) {
    return num * multiplier;
  };
}

const double = createMultiplier(2);
console.log(double(5));
// Expected output: 10

const triple = createMultiplier(3);
console.log(triple(5));
// Expected output: 15
```

## Wrapping Up
Understanding JavaScript functions in their various forms is crucial to mastering the language. Starting with basic function declarations and expressions, we see how they form the bedrock of reusable and modular code. As you progress, concepts like anonymous functions and IIFEs showcase the flexibility and scope management that JavaScript offers. At the advanced level, higher-order functions and closures unlock powerful patterns for dynamic and efficient programming.

Each level of complexity builds on the previous one, demonstrating how functions can adapt to solve problems. By practising these concepts, you not only become proficient in JavaScript but also gain a deeper appreciation for the art of programming itself.
