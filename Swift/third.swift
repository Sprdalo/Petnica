import Foundation;

var num = readLine(strippingNewline: true)!
var resenje = "";
var mapa = [1: "", 2 : "desetice", 3 : "stotine", 4 : "hiljade", 5 : "desetina hiljada", 6 : "stotina hiljada", 7 : "miliona", 8 : "desetina miliona", 9 : "stotina miliona"] 
var sajedan = [1: "", 2: "desetica", 3 : "stotina", 4: "hiljada", 5 : "desetina hiljada", 6: "stotina hiljada", 7 : "miliona", 8 : "desetina miliona", 9 : "stotina miliona"]

var cnt = 0;
var arr = [String]()
var s = ""
for c in num.reversed() {
  cnt += 1
  var sol = ""
  if (cnt == 1) {
    if (c == "1") {
      sol = "jedan"
    }
    if (c == "2") {
      sol = "dva"
    } 
    if (c == "3") {
      sol = "tri"
    }
    if (c == "4") {
      sol = "cetiri"
    } 
    if (c == "5") {
      sol = "pet"
    }
    if (c == "6") {
      sol = "sest"
    }
    if (c == "7") {
      sol = "sedam"
    }
    if (c == "8") {
      sol = "osam"
    }
    if (c == "9") {
      sol = "devet"
    }
  }
  if (cnt > 1) {
    if (c == "1") {
      sol = "jedna"
    }
    if (c == "2") {
      sol = "dve"
    } 
    if (c == "3") {
      sol = "tri"
    }
    if (c == "4") {
      sol = "cetiri"
    } 
    if (c == "5") {
      sol = "pet"
    }
    if (c == "6") {
      sol = "sest"
    }
    if (c == "7") {
      sol = "sedam"
    }
    if (c == "8") {
      sol = "osam"
    }
    if (c == "9") {
      sol = "devet"
    }
  }
  var a = sajedan[cnt]
  if (c != "1") {
    a = mapa[cnt]
  }
  arr.append(sol + " " + a! + " ")
}
 var res = ""
var i = arr.count - 1
while i >= 0 {
  res += arr[i]
  i -= 1
}
print(res)
