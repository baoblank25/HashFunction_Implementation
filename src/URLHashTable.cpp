// ASU CSE310 Hash Table Assignment
// File: URLHashTable.cpp
// Description: Implementation of URLHashTable class


#include "../include/URLHashTable.h"
#include <iostream>


URLHashTable::URLHashTable(int tableSize){
    size = tableSize;
    numElements = 0;
    table.resize(size);
    current_hType = DIVISION_HASH;
    current_pType = LINEAR_PROBING;
}


URLHashTable::~URLHashTable(){}


void URLHashTable::setHashFunction(HashType hashType){
    current_hType = hashType;
}


void URLHashTable::setProbingMethod(ProbingMethod probingType){
    current_pType = probingType;
}


int URLHashTable::probe(unsigned long hash, int i){
    if(current_pType==LINEAR_PROBING){
        return (hash+i)%size;
    }
    else{
        return (hash+i*i)%size;
    }
}


bool URLHashTable::searchURL(const string& url){
    clock_t start = clock();
    int comp = 0;
    bool found = false;
    
    unsigned long hash;
    if(current_hType==DIVISION_HASH){
        hash = hashFunc.divisionHash(url, size);
    }
    else{
        hash = hashFunc.universalHash(url, size);
    }
    
    int idx = hash;
    int i = 0;
    
    while(i<size){
        comp++;
        
        if(table[idx].status==EMPTY){
            break;
        }
        
        if(table[idx].status==OCCUPIED && table[idx].url==url){
            found = true;
            break;
        }
        
        i++;
        idx = probe(hash, i);
    }
    
    clock_t end = clock();
    stats.recordQuery(comp, end-start);
    
    if(found){
        cout << "\n\"" << url << "\" is found in the hash table." << endl;
    }
    else{
        cout << "\n\"" << url << "\" is NOT found in the hash table." << endl;
    }
    
    return found;
}


bool URLHashTable::insertURL(const string& url){
    clock_t start = clock();
    int comp = 0;
    
    unsigned long hash;
    if(current_hType==DIVISION_HASH){
        hash = hashFunc.divisionHash(url, size);
    }
    else{
        hash = hashFunc.universalHash(url, size);
    }
    
    int idx = hash;
    int i = 0;
    
    //Check if URL exists
    while(i<size){
        comp++;
        
        if(table[idx].status==EMPTY){
            break;
        }
        
        if(table[idx].status==OCCUPIED && table[idx].url==url){
            clock_t end = clock();
            stats.recordQuery(comp, end-start);
            cout << "\n\"" << url << "\" is a HIT - already exists in the hash table." << endl;
            return false;
        }
        
        i++;
        idx = probe(hash, i);
    }
    
    //Insert URL
    idx = hash;
    i = 0;
    
    while(i<size){
        if(table[idx].status==EMPTY || table[idx].status==DELETED){
            table[idx].url = url;
            table[idx].status = OCCUPIED;
            numElements++;
            
            clock_t end = clock();
            stats.recordQuery(comp, end-start);
            return true;
        }
        
        i++;
        idx = probe(hash, i);
    }
    
    cout << "Error: Hash table is full!" << endl;
    return false;
}


bool URLHashTable::deleteURL(const string& url){
    clock_t start = clock();
    int comp = 0;
    bool deleted = false;
    
    unsigned long hash;
    if(current_hType==DIVISION_HASH){
        hash = hashFunc.divisionHash(url, size);
    }
    else{
        hash = hashFunc.universalHash(url, size);
    }
    
    int idx = hash;
    int i = 0;
    
    while(i<size){
        comp++;
        
        if(table[idx].status==EMPTY){
            break;
        }
        
        if(table[idx].status==OCCUPIED && table[idx].url==url){
            table[idx].status = DELETED;
            table[idx].url = "";
            numElements--;
            deleted = true;
            break;
        }
        
        i++;
        idx = probe(hash, i);
    }
    
    clock_t end = clock();
    stats.recordQuery(comp, end-start);
    
    if(deleted){
        cout << "\"" << url << "\" is deleted from hash table." << endl;
    }
    else{
        cout << "\"" << url << "\" is NOT deleted from hash table." << endl;
    }
    
    return deleted;
}


void URLHashTable::displayTable(){
    cout << "\nHash Table Contents" << endl;
    for(int i=0; i<size; i++){
        cout << "Slot[" << i << "]: ";
        if(table[i].status==OCCUPIED){
            cout << table[i].url;
        }
        else if(table[i].status==DELETED){
            cout << "[DELETED]";
        }
        else{
            cout << "[EMPTY]";
        }
        cout << endl;
    }
}


void URLHashTable::displayStats(){
    cout << "\nHash Function: ";
    if(current_hType==DIVISION_HASH){
        cout << "Division Hashing" << endl;
    }
    else{
        cout << "Universal Hashing" << endl;
    }
    
    cout << "Probing Method: ";
    if(current_pType==LINEAR_PROBING){
        cout << "Linear Probing" << endl;
    }
    else{
        cout << "Quadratic Probing" << endl;
    }
    
    stats.display(size, numElements, getLoadFactor());
}


void URLHashTable::resetStats(){
    stats.reset();
}


double URLHashTable::getLoadFactor(){
    return (double)numElements/size;
}


int URLHashTable::getSize(){
    return size;
}


int URLHashTable::getNumElements(){
    return numElements;
}
