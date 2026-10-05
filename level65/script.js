const languageA=["qartuli","franguli","svanuri","kaxuri","inglisuri"]
const languageB=["qartuli","chinuri","svanuri","arabuli","ebrauli"]
const mutual=[]
for(let i=0 ; i<languageA.length;i++){
    for(let j=0; j< languageB.length;i++){
        if(languageA[i]===languageB[j]){
            mutual.push(languageA[i])
        }
    }
}
console.log(`found mutual language: ${mutual}`)


const fruits=['apple', 'cherry', 'melon'];
let current_fruits="";
while(current_fruits !=="cherry"){
    let random_index=Math.floor(Math.random()*fruits.length);
    current_fruits=fruits[random_index];
    console.log(current_fruits)
}
