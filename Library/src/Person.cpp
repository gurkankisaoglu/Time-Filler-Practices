#include "Person.h"
Person::Person(){
}

Person::Person(string fullName){
    this->fullName=fullName;
}

Person::~Person(){

}

string Person::getName(){
    return this->fullName;
}

void Person::setName(string name){
    this->fullName=name;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Borrower::Borrower(){

}

void Borrower::borrowBook(LibraryList &library , string borrowerName , string bookName){
    BookNode* temp=library.getHead();
    while(temp){
        if(bookName==temp->get_bookName() && !temp->isBorrowed()){
            temp->makeItBorrowed();
            return;
        }
        if(bookName==temp->get_bookName() && temp->isBorrowed()){
            cout << "The book is already borrowed" << endl;
            return;
        }
        temp=temp->show_nextBook();
    }
    cout << "The book you want to borrow doesnt exists in our library" << endl;
}

void Borrower::giveBorrowedBook(LibraryList &library , string bookName){
    BookNode* temp=library.getHead();
    while(temp){
        if(bookName==temp->get_bookName()){
            temp->makeItNotBorrowed();
            return;
        }
    }
}
