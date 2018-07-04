import Foundation

//Dodatno prostudirati currentweather
//Prkeopirano sa sa table

let urlString
= "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

var f = ""

if let url = URL (string: urlString) {
  do {
    let content = try String(contentsOf: url, encoding: .utf8)
    f = content
  }
  catch {
    print("Greska")
  }
}

struct coord : Decodable {
  var lon: Double
  var lat: Double
  
}

struct SingleWeather : Decodable {
  var id: Int
  var main: String 
  var description: String
  var icon: String
}

struct Main : Decodable {
  var temp: Double
  var pressure: Int
  var humidity: Int
  var temp_min: Double
  var temp_max: Double
}

struct Wind : Decodable {
  var speed: Double
  var deg: Int 
}

struct Clouds : Decodable {
  var all: Int
}

struct CurrentWeather : Decodable {
  var coord: coord
  var weather: [SingleWeather]
  var base: String
  var main: Main
  var visibility: Int
  var wind: Wind
  var clouds: Clouds
  var tempCelsius: Double {
    return main.temp - 273.15
  } 
}

if let jsonData = f.data(using: .utf8) {
  let arr = try? JSONDecoder().decode(CurrentWeather.self, from:jsonData)
  print(arr!.tempCelsius)
}
