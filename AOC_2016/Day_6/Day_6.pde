// David Keck
// Advent of Code Day 6
// Parts 1 & 2

String index_to_string(int index) {
 return str(char((index+97)));
}

void count_letters(Position position_input, String letter_input) {
  position_input.frequency_map.increment(str(letter_input.charAt(0)));
}

void setup() {
  surface.setVisible(false);
  String puzzle_input[] = loadStrings("puzzle_input.txt");
  int position_count = puzzle_input[0].length();
  Position[] positions = new Position[position_count];
  String error_corrected_message = "";
  
  for (int position = 0; position < position_count; position++) {
    positions[position] = new Position(position);
  }
  
  for (int i = 0; i < puzzle_input.length; i++) {
    for (int j = 0; j < puzzle_input[i].length(); j++) {
      count_letters(positions[j], str(puzzle_input[i].charAt(j)));
    }
  }
  
  for (int position = 0; position < position_count; position++) {
    IntDict map_copy = positions[position].frequency_map;
    map_copy.sortValuesReverse();
    
    String keys[] = map_copy.keyArray();
    
    error_corrected_message += keys[0];
  }
  
  println("The original error-corrected message is " + error_corrected_message + ".");
  
  error_corrected_message = "";
  
  for (int position = 0; position < position_count; position++) {
    IntDict map_copy = positions[position].frequency_map;
    map_copy.sortValues();
    
    String keys[] = map_copy.keyArray();
    
    error_corrected_message += keys[0];
  }
  
   println("The real error-corrected message is " + error_corrected_message + ".");
  
}

void draw() {
  
}

class Position {
  IntDict frequency_map = new IntDict();
  int position_number;
  
  Position(int position_number) {
    for(int i = 0; i < 26; i++) {
      frequency_map.set(str(char(i+97)), 0);
    }
    this.position_number = position_number;
  }
}