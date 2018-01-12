#include <iostream>
#include <cstdlib>
#include "Library.h"
#include "Person.h"


using namespace std;

LibraryList library;

void printMenu(){
    cout << "#######Select a process#######" << endl;
    cout << "'1' for adding book to library" << endl;
    cout << "'2' for see the books of library" << endl;
    cout << "'3' for see how many books are in library" << endl;
    cout << "'4' for borrow book" << endl;
    cout << "'5' for borrowed book list" << endl;
    cout << "'6' for borrowed book count" << endl;
}
void addBook(){
    cout << "Enter book name , author , publication year respectively" <<  endl;
    library.addBook();

}

void howManyBooks(){
    if(library.countOfBooks()==1 || library.countOfBooks()==0){
        cout << "there is " << library.countOfBooks() <<" book in library." << endl;
        return;
    }
    cout << "there are " << library.countOfBooks() <<" books in library." << endl;

}

void borrow(){
    cout << "Enter your name: " << endl;
    string name;
    cin.ignore();
    getline(cin,name);

    Borrower borrower;
    borrower.setName(name);

    cout << "Which book do you want to borrow: " << endl;
    string bookToBeBorrowed;
    getline(cin,bookToBeBorrowed);

    borrower.borrowBook(library,borrower.getName(),bookToBeBorrowed);
}

int main(){

    int process;
    char YesNo='y';

    while(YesNo=='y'){
        printMenu();
        cin >> process;

        switch (process){

            case 1:
                addBook();
                break;

            case 2:
                library.showBooks();
                break;

            case 3:
                howManyBooks();
                break;
            case 4:
                borrow();
                break;
            case 5:
                library.showBorrowed();
                break;
            default:
                break;
        }

        cout << "Do you want to continue(y/n)" << endl;
        cin >> YesNo;

        system("cls");
    }

    return 0;
}
