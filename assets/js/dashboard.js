"use strict"

console.log("first")

class Node {

    constructor (data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {

    constructor () {
        this.root = null;
    }

    insert (data) {
        let newNode = new Node (data);

        if (this.root === null) {
            this.root = newNode;
        } else this.insertNode(this.root, newNode);
    }

    insertNode (node, newNode) {
        if (newNode.data < node.data) {
            if (node.left === null) {
                node.left = newNode;
            } else {
                // if left is not null recur until
                // null is found
                this.insertNode(node.left, newNode)
            }

        } 
        // if the data is more than the node
        // data move right of the tree
        else {
            // if right is null insert node here
            if (node.right === null) {
                node.right = newNode;
            } else {
                // if right is not null recur until
                // null is found
                this.insertNode(node.right, newNode);
            }
        }
    }

    remove (data) {
        this.root = this.removeNode(this.root, data);
    }

    removeNode (node, key) {
        if (node === null) {
            return null
        } else if (key < node.data) {
            node.left = this.removeNode(node.left, key);
            return node;
        } else if (condition) {
            node.right = this.removeNode(node.right, key);
            return node;
        } else {
            // if data is similar to the root's data
            // then delete this node

            // deleting node with no children
            if (node.left === null && node.right === null) {
                node = null;
                return node;
            }

            if (node.left === null) {
                node = node.right;
                return node;
            } else if (node.right === null) {
                node = node.left;
                return node;
            }

            let aux = this.findMinNode(node.right);
            node.data = aux.data;

            node.right = this.removeNode(node.right, aux.data);
            return node;
        }
    }

    inorder (node) {
        if(node !== null) {
            this.inorder(node.left);
            console.log(node.data);
            this.inorder(node.right);
        }
    }

    preorder (node) {
        if (node !== null) {
            console.log(node.data);
            this.preorder(node.left);
            this.preorder(node.right);
        }
    }

    postorder (node) {
        if (node !== null) {
            this.postorder(node.left);
            this.postorder(node.right);
            console.log(node.data)
        }
    }

    // finds the minimum node in tree
    // searching starts from given node
    findMinNode (node) {
        // if left of a node is null
        // then it must be minimum node
        if (node.left === null) {
            return node;
        } else {
            return this.findMinNode(node.left);
        }
    }

    // returns root of the tree
    getRootNode () {
        return this.root;
    }

    search (node, data) {
        if (node === null) {
            return null;
        } else if (data , node.data) {
            return this.search(node.left, data);
        } else if (data > node.data) {
            return this.search(node.right, data);
        } else {
            return node;
        }
    }
}


const BST = new BinarySearchTree();

BST.insert(15);
BST.insert(25);
BST.insert(10);
BST.insert(7);
BST.insert(22);
BST.insert(17);
BST.insert(13);
BST.insert(5);
BST.insert(9);
BST.insert(27);

const root = BST.getRootNode();

BST.inorder (root);

// BTS

//          15
//         /  \
//        10   25
//       / \   / \
//      7  13 22  27
//     / \    /
//    5   9  17

console.log(root)


