import Foundation


struct Movie : Codable {
  var Title: String
  var Year: String
}

struct Movies : Codable {
  var Search : [Movie]
}

var film = ""

if let linija = readLine() {
  film = linija 
}

let urlString = "https://www.omdbapi.com/?s=" + film + "&apikey=9dbcc5eb"

var sadrzaj = ""

if let url = URL (string: urlString) {
  do {
    let content = try String(contentsOf: url, encoding: .utf8) 
    sadrzaj = content
  }
  catch {
    print("Greska")
  } 
}

if let jsonData = sadrzaj.data(using: .utf8) {
    let movies = try? JSONDecoder().decode(Movies.self, from:jsonData)
    if let d = movies {
      for i in d.Search {
        print("\(i.Title) \(i.Year)")
      }
    }
    else {
      print("Nece") 
    }
}
