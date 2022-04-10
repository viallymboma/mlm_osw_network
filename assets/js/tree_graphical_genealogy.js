"use strict";

// const { left } = require("@popperjs/core");

const getTreeData = () => {
    return {
        element: "Ariel",
        id: 1,
        position: "right",
        left: {
            element: "Betsy",
            position: "left",
            id: 2,
            left: {
                element: "Paul",
                position: "left",
                id: 4,
                left: {
                    element: "Abeiku",
                    position: "left",
                    id: 8,
                },
                right: {
                    element: "Doris",
                    position: "right",
                    id: 9,
                }
            },
            right: {
                element: "Gifty",
                position: "right",
                id: 5,
                left: {
                    element: "Bernard",
                    position: "left",
                    id: 10,
                    // left: {
                    //     element: "Neida",
                    //     id: 1,
                    // },
                    right: {
                        element: "Anita",
                        id: 14,
                        left: {
                            element: "Neida",
                            id: 15,
                        },
                    }
                },
                right: {
                    element: "Abigail",
                    position: "right",
                    id: 11,
                }
            }
        },
        right: {
            element: "Frank",
            id: 3,
            position: "right",
            left: {
                element: "Kofi",
                id: 6,
                position: "left",
                // left: {
                //     element: "Neida"
                //     id: 1,
                // },
                // right: {
                //     element: "Anita"
                //     id: 1,
                // }
            },
            right: {
                element: "Abena",
                position: "right",
                id: 7,
                left: {
                    element: "Derrick",
                    position: "left",
                    id: 12,
                },
                right: {
                    element: "Andrew",
                    position: "right",
                    id: 13,
                }
            }
        }
    }
}

const side_iba_details = document.querySelector(".side_iba_details");
const backdrop = document.querySelector(".backdrop");


backdrop.addEventListener("click", () => {
    backdrop.style.transform = "translate(0%)";
    side_iba_details.style.transform = "translate(100%)";
    doPlacement.style.transform = "translate(100%)";
})

const tree_container_id = document.getElementById ("tree_container_id");

// I will get an array coming from backend and i will
// use it as an array and 
console.log(tree_container_id)

const renderGraphicalTree = (node) => {

    const { left, right, element, id, position } = node;
    // console.log(left)
    // console.log(lelement)
    // console.log(id)

    return `
        <div class="node node_root">
            <div class="node_element node_element_child" data-name=${element} data-position=${position} id="view_position" value=${id}>
                ${element}
                <br/>
                ${id}
            </div>
            
            ${
                left || right ? 
                `
                    <div class="parent_node_connect_line"></div>
                    <div class="node_bottom_line"></div>
                    <div class="node_children">
                        ${
                            left ? (
                                `
                                    <div class="node"  >
                                        ${ renderGraphicalTree (left) }
                                    </div>
                                `
                            ) : 
                            `
                                <div class="node" data-sponsort=${id} data-position=${position} id="add_left">
                                    <div class="node_element node_element_child"> No Left Child </div>
                                </div>
                            `
                        }
                        
                        ${
                            right ? (
                                `
                                    <div class="node">
                                        ${ renderGraphicalTree (right) }
                                    </div>
                                `
                            ) : 
                            
                            `
                                <div class="node" data-sponsort=${id} data-position=${position} id="add_right">
                                    <div class="node_element node_element_child"> No Right Child </div>
                                </div>
                            `
                        }
                    </div>
                ` : 
                `
                    <div class="parent_node_connect_line"></div>
                    <div class="node_bottom_line"></div>
                    <div class="node_children">
                        <div class="node" data-sponsort=${id} data-position=${position} id="add_left">
                            <div class="node_element node_element_child" > No Left child </div>
                        </div>
                        <div class="node" data-sponsort=${id} data-position=${position} id="add_right">
                            <div class="node_element node_element_child"> No Right child </div>
                        </div>
                    </div>
                `
            }
        </div>
        
    `
}


const main = () => {
    const rootNode = getTreeData ()
    const treeElement = document.querySelector(".tree");
    treeElement.innerHTML = renderGraphicalTree(rootNode)
}

main ();


// const view_position = document.getElementById("view_position");
const view_position_all = document.querySelectorAll("#view_position");
console.log(view_position_all);
const view_position_all_arr = Array.prototype.slice.call(view_position_all);
console.log(view_position_all_arr);

const doPlacement = document.querySelector(".doPlacement");
const add_left_all = document.querySelectorAll("#add_left");
const add_left = Array.prototype.slice.call(add_left_all);

console.log(add_left)
const add_right_all = document.querySelectorAll("#add_right");
const add_right = Array.prototype.slice.call(add_right_all);

const sponsor_id = document.getElementById("sponsor_id")
const radio_left_id = document.getElementById("radio_left_id");
const radio_right_id = document.getElementById("radio_right_id");

const h2_position = document.querySelector(".h2_position");

const h1 = document.querySelector(".h1")
const h2 = document.querySelector(".h2")

for (let i = 0; i < view_position_all_arr.length; i++) {
    // const element = view_position_all_arr[i];
    view_position_all_arr[i].addEventListener('click', () => {
        // data-name
        h1.innerHTML = view_position_all_arr[i].getAttribute('data-name');
        h2.innerHTML = view_position_all_arr[i].getAttribute('value');
        h2_position.innerHTML = view_position_all_arr[i].getAttribute("data-position")
        backdrop.style.transform = "translate(100%)";
        side_iba_details.style.transform = "translate(0%)";
        console.log(view_position_all_arr[i].getAttribute('value'));
    })

}

for (let i = 0; i < add_left.length; i++) {
    // const element = view_position_all_arr[i];
    add_left[i].addEventListener('click', () => {
        // data-name
        // radio_left_id.setAttribute("checked") = true;
        radio_left_id.checked = true
        radio_right_id.checked = false
        sponsor_id.value = add_left[i].getAttribute('data-sponsort');
        backdrop.style.transform = "translate(100%)";
        doPlacement.style.transform = "translate(0%)";
        console.log("clicked")
    })
}

for (let i = 0; i < add_right.length; i++) {
    // const element = view_position_all_arr[i];
    add_right[i].addEventListener('click', () => {
        // data-name
        // radio_left_id.setAttribute("checked") = true;
        radio_right_id.checked = true
        radio_left_id.checked = false
        sponsor_id.value = add_right[i].getAttribute('data-sponsort');
        backdrop.style.transform = "translate(100%)";
        doPlacement.style.transform = "translate(0%)";
        console.log("clicked")
    })
}

// add_left.addEventListener('click', () => {
//     // data-name
//     // radio_left_id.setAttribute("checked") = true;
//     // sponsor_id.setAttribute("value") = add_left.getAttribute('data-sponsort');
//     backdrop.style.transform = "translate(100%)";
//     doPlacement.style.transform = "translate(0%)";
//     console.log("clicked")
//     // console.log(add_left.getAttribute('value'));
// })


// view_position.addEventListener("click", () => {
//     h2.innerHTML = view_position.value
//     side_iba_details.style.transform = "translate(0%)"
//     console.log(view_position.value)
// })

// view_right.addEventListener("click", () => {
//     h2.innerHTML = view_right.value
//     side_iba_details.style.transform = "translate(0%)"
//     console.log(view_right.value)
// })

// console.log(view_position.value)

const theData = getTreeData ()

console.log(theData)



// return `
//         <div class="node_element">${element}</div>
//         ${
//             left || right ? 
//             `
//                 <div class="parent_node_connect_line"></div>
//                 <div class="node_bottom_line"></div>
//                 <div class="node_children">
//                     ${
//                         left ? (
//                             `
//                                 <div class="node">
//                                     ${ renderGraphicalTree (left) }
//                                 </div>
//                             `
//                         ) : 
//                         `
//                             <div class="node">
//                                 <div class="node_element node_element_child"> No Left Child </div>
//                             </div>
//                         `
//                     }
                    
//                     ${
//                         right ? (
//                             `
//                                 <div class="node">
//                                     ${ renderGraphicalTree (right) }
//                                 </div>
//                             `
//                         ) : 
//                         `
//                             <div class="node">
//                                 <div class="node_element node_element_child"> No Right Child </div>
//                             </div>
//                         `
//                     }
//                 </div>
//             ` : 
//             `
//                 <div class="parent_node_connect_line"></div>
//                 <div class="node_bottom_line"></div>
//                 <div class="node_children">
//                     <div class="node">
//                         <div class="node_element node_element_child"> No child </div>
//                     </div>
//                     <div class="node">
//                         <div class="node_element node_element_child"> No child </div>
//                     </div>
//                 </div>
//             `
//         }
        
//     `



// class Node {

//     constructor (data) {
//         this.data = data;
//         this.left = null;
//         this.right = null;
//     }
// }

// class BinarySearchTree {

//     constructor () {
//         this.root = null;
//     }

//     insert (data) {
//         let newNode = new Node (data);

//         if (this.root === null) {
//             this.root = newNode;
//         } else this.insertNode(this.root, newNode);
//     }

//     insertNode (node, newNode) {
//         if (newNode.data < node.data) {
//             if (node.left === null) {
//                 node.left = newNode;
//             } else {
//                 // if left is not null recur until
//                 // null is found
//                 this.insertNode(node.left, newNode)
//             }

//         } 
//         // if the data is more than the node
//         // data move right of the tree
//         else {
//             // if right is null insert node here
//             if (node.right === null) {
//                 node.right = newNode;
//             } else {
//                 // if right is not null recur until
//                 // null is found
//                 this.insertNode(node.right, newNode);
//             }
//         }
//     }

//     remove (data) {
//         this.root = this.removeNode(this.root, data);
//     }

//     removeNode (node, key) {
//         if (node === null) {
//             return null
//         } else if (key < node.data) {
//             node.left = this.removeNode(node.left, key);
//             return node;
//         } else if (condition) {
//             node.right = this.removeNode(node.right, key);
//             return node;
//         } else {
//             // if data is similar to the root's data
//             // then delete this node

//             // deleting node with no children
//             if (node.left === null && node.right === null) {
//                 node = null;
//                 return node;
//             }

//             if (node.left === null) {
//                 node = node.right;
//                 return node;
//             } else if (node.right === null) {
//                 node = node.left;
//                 return node;
//             }

//             let aux = this.findMinNode(node.right);
//             node.data = aux.data;

//             node.right = this.removeNode(node.right, aux.data);
//             return node;
//         }
//     }

//     inorder (node) {
//         if(node !== null) {
//             this.inorder(node.left);
//             console.log(node.data);
//             this.inorder(node.right);
//         }
//     }

//     preorder (node) {
//         if (node !== null) {
//             console.log(node.data);
//             this.preorder(node.left);
//             this.preorder(node.right);
//         }
//     }

//     postorder (node) {
//         if (node !== null) {
//             this.postorder(node.left);
//             this.postorder(node.right);
//             console.log(node.data)
//         }
//     }

//     // finds the minimum node in tree
//     // searching starts from given node
//     findMinNode (node) {
//         // if left of a node is null
//         // then it must be minimum node
//         if (node.left === null) {
//             return node;
//         } else {
//             return this.findMinNode(node.left);
//         }
//     }

//     // returns root of the tree
//     getRootNode () {
//         return this.root;
//     }

//     search (node, data) {
//         if (node === null) {
//             return null;
//         } else if (data , node.data) {
//             return this.search(node.left, data);
//         } else if (data > node.data) {
//             return this.search(node.right, data);
//         } else {
//             return node;
//         }
//     }
// }


// const BST = new BinarySearchTree();

// BST.insert(15);
// BST.insert(25);
// BST.insert(10);
// BST.insert(7);
// BST.insert(22);
// BST.insert(17);
// BST.insert(13);
// BST.insert(5);
// BST.insert(9);
// BST.insert(27);

// const root = BST.getRootNode();

// BST.inorder (root);

// // BTS

// //          15
// //         /  \
// //        10   25
// //       / \   / \
// //      7  13 22  27
// //     / \    /
// //    5   9  17

// console.log(root)


