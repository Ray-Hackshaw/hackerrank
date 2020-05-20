'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
///////////////////////////////////
function getLetter(s) {
    let letter;
    const set1 = "aeiou";
    const set2 = "bcdfg";
    const set3 = "hjklm";
    const first = s[0].toLowerCase();

    switch(true){
        case set1.includes(first):
            letter = "A";
            break;
        case set2.includes(first):
            letter = "B";
            break;
        case set3.includes(first):
            letter = "C"
            break;
        default:
            letter = "D"
            break;
        }
    return letter;
}

///////////////////////////////////

function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}

// https://www.hackerrank.com/challenges/js10-switch/problem
