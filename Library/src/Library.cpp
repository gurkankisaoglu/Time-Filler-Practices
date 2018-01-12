#include "Library.h"

BookNode::BookNode(){
    this->set_nextBook(NULL);
}

BookNode::BookNode(string name,string author, int pubYear){
    this->author=author;
    this->bookName=name;
    this->publicationYear=pubYear;
    this->set_nextBook(NULL);
    this->signOfBorrow=0;
}

BookNode::~BookNode(){
}

void BookNode::set_nextBook(BookNode *aBook){
    this->nextBook=aBook;
}

BookNode* BookNode::show_nextBook()const{
    return this->nextBook;
}

void BookNode::printInfo()const{
    cout << this->bookName << "-" << this->author << "-" << this->publicationYear << endl;
}

string BookNode::get_bookName(){
    return this->bookName;
}

void BookNode::makeItBorrowed(){
    this->signOfBorrow++;
}

void BookNode::makeItNotBorrowed(){
    this->signOfBorrow--;
}

int BookNode::isBorrowed(){
    return this->signOfBorrow;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

LibraryList::LibraryList(){
    bookCount=0;
}

LibraryList::~LibraryList(){

}

void LibraryList::addBook(){
    string author,name;
    int pubYear;

    cin.ignore();
    getline(cin,name,'\n');
    getline(cin,author,'\n');
    cin >>pubYear;

    BookNode *newBook = new BookNode(name,author,pubYear);

    if(bookCount==0) head=newBook;
    else{
        BookNode *tmp=head;
        while(tmp->show_nextBook()){
            tmp=tmp->show_nextBook();
        }
        tmp->set_nextBook(newBook);
    }
    bookCount++;
}

void LibraryList::showBooks(){
    if(countOfBooks()==0){
        cout << "Library is empty!" << endl;
        return;
    }
    cout << "Books of library are: \n";
    BookNode* tmp=head;
    while(tmp){
        tmp->printInfo();
        tmp=tmp->show_nextBook();
    }
}

int LibraryList::countOfBooks(){
    return bookCount;
}

BookNode* LibraryList::getHead(){
    return this->head;
}

void LibraryList::showBorrowed(){
    BookNode* temp=head;
    while(temp && temp->isBorrowed()){
        temp->printInfo();
        temp=temp->show_nextBook();
    }
}

int LibraryList::borrowedCount(){
    BookNode* temp=head;
    int cnt=0;
    while(temp && temp->isBorrowed()){
        cnt++;
        temp=temp->show_nextBook();
    }
    return cnt;
}






