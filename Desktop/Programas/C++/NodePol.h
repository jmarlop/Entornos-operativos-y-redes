#ifndef NODEPOL_H
#define NODEPOL_H

#include "Polygon.h"
using namespace std;

class NodePol {
    public:
        Polygon* data;
        NodePol* next;
    
        NodePol(Polygon* p);
        NodePol(Polygon* p, NodePol* n);
        ~NodePol();
};

#endif