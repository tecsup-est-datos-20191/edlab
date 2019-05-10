# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}
 
def postfixConvert(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        if char not in operatorPrecedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[len(stack) - 1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operatorPrecedence[char] > operatorPrecedence[stack[len(stack) - 1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
     
    while len(stack) != 0:
        postfix.append(stack.pop())
 
    return "".join(postfix)

#
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.right is not None and self.left is not None :
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()

        else:
            return float(self.value)


#
class ExressionTree(object):
    def __init__(self, root=None):
        self.__root = root 
     
    def inorder(self):
        self.__inorder_helper(self.__root)
         
    def __inorder_helper(self, node):
        if node:
            self.__inorder_helper(node.left)
            print(node.value)
            self.__inorder_helper(node.right)
 
    def preorder(self):
        self.__preorderUtil(self.__root)
         
    def __preorderUtil(self, node):
        if node:
            print(node.value)
            self.__preorderUtil(node.left)
            self.__preorderUtil(node.right)
 
    def postorder(self):
        self.__postorderUtil(self.__root)
         
    def __postorderUtil(self, node):
        if node:
            self.__postorderUtil(node.left)
            self.__postorderUtil(node.right)
            print(node.value)

#
def buildExpressionTree(infix):
    postfix = postfixConvert(infix)

    print(postfix)

    stack = []
 
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)   
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)

    #return ExressionTree(stack.pop())

    #return stack.pop().eval()
    return stack.pop()

def evalFull():
    print("Evaluate:")
    root = buildExpressionTree("(5+3)*6")
    print(root.eval())

#print("In Order:")
#buildExpressionTree("(5+3)*6").inorder()
#print("Post Order:")
#buildExpressionTree("(5+3)*6").postorder()
#buildExpressionTree("5*8+(5+(3+2-1))*6").postorder()
#print("Pre Order:")
#buildExpressionTree("(5+3)*6").preorder()

#################################
# First Case :  (5+3)*6
#
#         *
#     +      6
#   5   3
#################################
def evalManual():
    opeNodeA = Node(5)
    opeNodeB = Node(3)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    opeNodeC = Node(6)
    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())

#################################
# Second Case :  (5+3)*6
# input : postfix
# return : Binary Tree
#################################
def parserToTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)

    return stack.pop()

#################################
# Second Case :  Evaluate Postfix
#                espression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
# Prefix expression  : *+536
#################################
def evalPostfixExpression():

  postfix =  "53+6*"
  rootNode = parserToTree(postfix)
  print(rootNode.eval())


#################################
# Third Case :  Create postfix
#                expression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
#################################
def convertIndorToPostfixExp():
    indor = "(5+3)*6"
    postfix = postfixConvert(indor)
    print(postfix)

#################################
# Fourth Case :  Create postfix
# Indor expression   : (5+3)*6
#################################
def evalIndorExpression():
    indor = "(5+5)*6"
    postfix = postfixConvert(indor)
    rootNode = parserToTree(postfix)
    print(rootNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
   # evalManual()
   # evalPostfixExpression()
   # convertIndorToPostfixExp()
    evalIndorExpression()



