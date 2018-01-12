#ifndef LIBRARY_H
#define LIBRARY_H

#include <iostream>

using namespace std;

class BookNode{
    public:
        BookNode();
        ~BookNode();
        BookNode(string,string,int);
        BookNode *show_nextBook()const;
        void set_nextBook(BookNode* );
        void printInfo() const;
        string get_bookName();
        void makeItBorrowed();
        int isBorrowed();
        void makeItNotBorrowed();

    private:
        string author;
        string bookName;
        int publicationYear;
        BookNode *nextBook;
        int signOfBorrow;

};


class LibraryList{
    public:
        LibraryList();
        ~LibraryList();
        void addBook();
        void showBooks();
        int countOfBooks();
        BookNode* getHead();
        void showBorrowed();
        int borrowedCount();

    private:
        BookNode *head;
        int bookCount;

};

#endif // LIBRARY_H
