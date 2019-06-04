import requests
import json
import unittest

class Posts:

        def postonly(self,): 
                req = requests.get('https://jsonplaceholder.typicode.com/posts') 
                count=1  
                for i in json.loads(req.content):
                        print("Post ",count,":",i['body'])
                        count+=1

        def postdetail(self,): 
                req = requests.get('https://jsonplaceholder.typicode.com/posts')   
                for i in json.loads(req.content):
                        #print(i['userId'])
                        print("User id",i['userId'])
                        print("Post Id  :",i['id'])
                        print("Title    :",i['title'])
                        print("Post :",i['body'])
                        print("************************************************")

        def getpostonId(self,userid):
                #self.userid=userid                
                req1 = requests.get('https://jsonplaceholder.typicode.com/users/?id=%s' % userid)
                for i in json.loads(req1.content):
                        print("User id",i['id'])
                        print("Name of User :", i['name'])
                        print("************************************************")
                req = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=%s' % userid)
                return(json.loads(req.content))    
                
        def getcomments(self,):
                req = requests.get('https://jsonplaceholder.typicode.com/comments')     
                count=1
                for i in json.loads(req.content):
                        print("comment ",count,":  ",i['body'])
                        count+=1

        def getcommentsPostid(self,postid):
                print("Post Id  :", postid)
                req1 = requests.get('https://jsonplaceholder.typicode.com/posts/?id=%s' % postid)
                for i in json.loads(req1.content):
                        print("Post :", i['body'])
                        print("*************************************")
                req = requests.get('https://jsonplaceholder.typicode.com/comments/?postId=%s' % postid)
                return(json.loads(req.content))
                
#************************************************************************************************       
class Testing(unittest.TestCase):
        def setUp(self):
                self.posts = Posts()

        def testpostdetail(self):
                req = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=5')
                req1 = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=2')
                req2 = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=3')
                self.assertEqual(json.loads(req.content), self.posts.getpostonId(5))   
                self.assertEqual(json.loads(req1.content), self.posts.getpostonId(2))   
                self.assertEqual(json.loads(req2.content), self.posts.getpostonId(3)) 

        def testgetcommentsPostid(self,):
                req = requests.get('https://jsonplaceholder.typicode.com/comments/?postId=2')
                req1 = requests.get('https://jsonplaceholder.typicode.com/comments/?postId=3')
                req2 = requests.get('https://jsonplaceholder.typicode.com/comments/?postId=4')
                self.assertEqual(json.loads(req.content), self.posts.getcommentsPostid(2))   
                self.assertEqual(json.loads(req1.content), self.posts.getcommentsPostid(3))   
                self.assertEqual(json.loads(req2.content), self.posts.getcommentsPostid(4))

#*******************************************************************
obj = Posts()
var = obj.getpostonId(int(input("enter user id   :")))
for i in var:
        print("Post Id  :",i['id'])
        print("Title    :",i['title'])
        print("Post :",i['body'])
        print("************************************************")

#*******************************************************************
var1 = obj.getcommentsPostid(int(input("enter post Id   :")))
count = 1
for i in var1:
        print("Comment ", count,":  ",i['body'])
        count +=1
#*******************************************************************
obj.postdetail()
obj.postonly()
obj.getcomments()
#*******************************************************************
unittest.main()  




