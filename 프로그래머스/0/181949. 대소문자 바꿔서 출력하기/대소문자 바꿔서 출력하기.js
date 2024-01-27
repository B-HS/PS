const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    const result = str.split("").map(ele=>{
        if(ele.toUpperCase() === ele){
            return ele.toLowerCase()
        }else{
            return ele.toUpperCase()
        }
    }).join("")
    
    console.log(result)
});