import Foundation;	//Ovo je library za matematiku 

var word = readLine(strippingNewline: true)!
var ar = [1 : 0];

for c in word {		//Iteriramo radi inicijalizacije mape
  let s = String(c);
  if let someint = Int(s) {
    if (ar[someint] != nil) {
      let num = ar[someint]; 
      ar[someint] = num! + 1;
    }
    else {
      ar[someint] = 1;
    }
  }
}

for (key, value) in ar {	//Proveravamo uslov
  let a = String(key);
  let b = String(value);
  if value > 0 {
    print(" \(a) : \(b)");
  }
}
