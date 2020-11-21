

#ifndef BINARYSEARCHTREE_HPP
#define BINARYSEARCHTREE_HPP
#include "Node.hpp"
class BinarySearchTree
{

public:
    [[nodiscard]] std::shared_ptr<Node> root() const;

    void add(int value);

private:
    std::shared_ptr<Node> m_root;
};

#endif //BINARYSEARCHTREE_HPP
