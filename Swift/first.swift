var word = readLine(strippingNewline: true)!
var arr = [ "a" : 0 ];

for c in word {
  if (arr[String(c)] != nil) {
      let value = arr[String(c)]
      arr[String(c)] = value! + 1
  } else {
      arr[String(c)] = 1 
  }
}

for (a, b) in arr {
  if b > 0 {
    print("\(a) : \(b)")
  }
}
