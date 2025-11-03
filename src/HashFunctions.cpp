// ASU CSE310 Hash Table Assignment
// File: HashFunctions.cpp
// Description: Implementation of hash functions


#include "../include/HashFunctions.h"


HashFunctions::HashFunctions(){
    k = 1000003;  //Large odd prime
    a = 31415;    //Random value
    b = 27183;    //Random value
}


//Division hash function using polynomial rolling hash
unsigned long HashFunctions::divisionHash(const string& url, int size){
    unsigned long hash = 0;
    
    for(size_t i=0; i<url.length(); i++){
        hash = (hash*31+(unsigned char)url[i])%size;
    }
    
    return hash%size;
}


//Universal hash function
//Formula: ha,b(x) = ((a * #(x) + b) mod k*Hsize) / k
unsigned long HashFunctions::universalHash(const string& url, int size){
    unsigned long kHsize = k*size;
    unsigned long hashValue = 0;
    
    //Compute #(x) using Horner's rule with base 256
    for(size_t i=0; i<url.length(); i++){
        hashValue = (hashValue*256+(unsigned char)url[i])%kHsize;
    }
    
    //Apply universal hash formula
    hashValue = ((a*hashValue+b)%kHsize)/k;
    return hashValue%size;
}
