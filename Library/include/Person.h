#ifndef PERSON_H
#define PERSON_H
#include "Library.h"
#include <iostream>

using namespace std;

class Person{
    public:
        Person();
        Person(string);
        ~Person();
        string getName();
        void setName(string);
    private:
        string fullName;

};

class Borrower : public Person{
    public:
        Borrower();
        void borrowBook(LibraryList&,string,string);
        void giveBorrowedBook(LibraryList&,string);
};
#endif // PERSON_H
