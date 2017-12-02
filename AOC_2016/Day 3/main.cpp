#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

bool triangleIsPossible(int sideOne, int sideTwo, int sideThree) {
    if ((sideOne + sideTwo) > sideThree && (sideTwo + sideThree) > sideOne && (sideThree + sideOne) > sideTwo) {
        return true;
    } else {
        return false;
    }
}

void partOne() {
    ifstream puzzleInput;
    puzzleInput.open("puzzleInput.txt");
    string line;

    int possibleTriangles = 0;

    if (puzzleInput.is_open()) {
        while (getline(puzzleInput, line)) {
            istringstream sides(line);
            int sideOne, sideTwo, sideThree;
            sides >> sideOne;
            sides >> sideTwo;
            sides >> sideThree;

            if (triangleIsPossible(sideOne, sideTwo, sideThree)) {
                possibleTriangles++;
            }

        }
        puzzleInput.close();
    } else {
        cout << "file failed to open";
    }

    cout << "PART ONE: The number of possible triangles is: " << possibleTriangles << endl;
}

void partTwo() {
    ifstream puzzleInput;
    puzzleInput.open("puzzleInput.txt");

    int possibleTriangles = 0;

    vector<int> columnOne;
    vector<int> columnTwo;
    vector<int> columnThree;

    int tempSide = 0;

    if (puzzleInput.is_open()) {
        while(!puzzleInput.eof()) {
            puzzleInput >> tempSide;
            columnOne.push_back(tempSide);
            puzzleInput >> tempSide;
            columnTwo.push_back(tempSide);
            puzzleInput >> tempSide;
            columnThree.push_back(tempSide);
        }
        puzzleInput.close();
    } else {
        cout << "file failed to open";
    }

    vector<int>::iterator it = columnOne.begin();

    while (it < columnOne.end()) {
        vector<int> sides;
        for (int i = 0; i < 3; i++) {
            sides.push_back(*it);
            it++;
        }
        if (triangleIsPossible(sides[0], sides[1], sides[2])) {
            possibleTriangles++;
        }
    }

    it = columnTwo.begin();

    while (it < columnTwo.end()) {
        vector<int> sides;
        for (int i = 0; i < 3; i++) {
            sides.push_back(*it);
            it++;
        }
        if (triangleIsPossible(sides[0], sides[1], sides[2])) {
            possibleTriangles++;
        }
    }

    it = columnThree.begin();

    while (it < columnThree.end()) {
        vector<int> sides;
        for (int i = 0; i < 3; i++) {
            sides.push_back(*it);
            it++;
        }
        if (triangleIsPossible(sides[0], sides[1], sides[2])) {
            possibleTriangles++;
        }
    }

    cout << "PART TWO: The number of possible triangles is: " << possibleTriangles;
}

int main() {
    partOne();
    partTwo();

    return 0;
}