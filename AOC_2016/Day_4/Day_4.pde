// David Keck
// Advent of Code Day 4
// Parts 1 & 2

char advance_character_by(int number_of_steps, char this_char) {
  int char_index = (int(this_char) + (number_of_steps % 26));
  if (char_index > 122) {
   char_index -= 26; 
  }
  return char(char_index);
}

void decode_cipher(Room this_room) {
  String decoded_cipher = "";
  for(int i = 0; i < this_room.puzzle_input.indexOf('[') - 4; i++) {
    String[] letter = match(str(this_room.puzzle_input.charAt(i)), "[A-Z,a-z]");
    if(letter != null) {
      decoded_cipher += advance_character_by(this_room.sector_id, letter[0].charAt(0));
    } else {
      decoded_cipher += " ";
    }
  }
  this_room.decoded_cipher = decoded_cipher;
}

String index_to_string(int index) {
 return str(char((index+97)));
}

void count_letters(Room room_input, String letter_input) {
  room_input.frequency_map.increment(str(letter_input.charAt(0)));
}

void compute_checksum(Room this_room) {
  int checksum_size = 5;
  int checksum_characters_found = 0;
  String checksum = "";
  IntDict map_copy = this_room.frequency_map;
  map_copy.sortKeys();
  
  while(checksum_characters_found < checksum_size) {
    int largest_value = 0;
    int largest_index = 0;
    for(int i = 0; i < map_copy.size(); i++) {
      if(map_copy.get(index_to_string(i)) > largest_value) {
        largest_value = map_copy.get(index_to_string(i));
        largest_index = i;
      }
    }
    checksum += index_to_string(largest_index);
    map_copy.set(index_to_string(largest_index), 0);
    checksum_characters_found++;
  }
  this_room.computed_checksum = checksum;
}

void decrypt_room(Room this_room) {
  for(int i = 0; i < this_room.puzzle_input.indexOf('[') - 4; i++) {
    String[] letter = match(str(this_room.puzzle_input.charAt(i)), "[A-Z,a-z]");
    if(letter != null) {
      count_letters(this_room, letter[0]);
    }
  }
  compute_checksum(this_room);
  this_room.sector_id = int(this_room.puzzle_input.substring(this_room.puzzle_input.indexOf('[') - 3, this_room.puzzle_input.indexOf('[')));
  this_room.checksum = this_room.puzzle_input.substring(this_room.puzzle_input.indexOf('[')+1, this_room.puzzle_input.indexOf(']'));
}

void setup() {
  surface.setVisible(false);
  String puzzle_input[] = loadStrings("puzzle_input.txt");
  int room_count = puzzle_input.length;
  Room[] rooms = new Room[room_count];
  
  for(int i = 0; i < room_count; i++) {
    rooms[i] = new Room(puzzle_input[i]);
    decrypt_room(rooms[i]);
  }
  
  println("There are " + room_count + " rooms.");

  int valid_rooms_id_sum = 0;
  Room[] valid_rooms = new Room[0];
  for(int i = 0; i < room_count; i++) {
    if(rooms[i].computed_checksum.equals(rooms[i].checksum)) {
      valid_rooms_id_sum += rooms[i].sector_id;
      valid_rooms = (Room[]) append(valid_rooms, rooms[i]);
    }
  }
  println("The sum of the valid rooms' sector ids is ", valid_rooms_id_sum + ".");
  
  for(int i = 0; i < valid_rooms.length; i++) {
    decode_cipher(valid_rooms[i]);
    //println("The decoded room name for sector id " + valid_rooms[i].sector_id + " is " + valid_rooms[i].decoded_cipher);
    if(valid_rooms[i].decoded_cipher.indexOf("northpole") != -1) {
      println("The sector ID of the room with North Pole objects is", valid_rooms[i].sector_id + ".");
    }
  }
  
}

void draw() {
  
}

class Room {
  IntDict frequency_map = new IntDict();
  String puzzle_input, decoded_cipher, encryption_key, checksum, computed_checksum = "";
  int sector_id;
  
  Room(String puzzle_input) {
    for(int i = 0; i < 26; i++) {
      frequency_map.set(str(char(i+97)), 0);
    }
    this.puzzle_input = puzzle_input;
  }
}
