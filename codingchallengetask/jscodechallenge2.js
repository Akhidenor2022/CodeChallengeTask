// Write a length converter function

//Convert meter to cm and cm to meter
function cm(x){
    const cm=x/100 + 'm';
    const m=x*100  + 'cm';
    return[{cm},{m}]
    
    }
        
    console.log(cm(10))