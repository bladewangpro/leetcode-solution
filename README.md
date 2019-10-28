### Code Practice Repository

---

#### Targets

This repository is designed for storing our practice code. 

#### Structure

We have three pals in this group and each of us will have a folder to store our practice code. There are "Liwei", "Wuyekang" and "Wangtianyi" respectively. Here is the structure of our code repository:

![image-20191027181904294](/home/blade/Documents/Leetcode/src/tools/structure.png)

**Each folder should have a corresponding log, such as Python folder -- 'py_map', from those logs, 'run.py' can help us to store the information of each files**

#### Standards

```Python
'''@name: 2. Add Two Numbers
'''


'''
@performance:
Runtime: 64 ms, faster than 23.98% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 25.73% of Python online submissions for Add Two Numbers.
'''
```

In the head of each scripts, there should be an annotation which will include the name of the topics, the performance and runtime of your code. Those information will be given from Leetcode platform automatically. 

If you have more than one method to address this problem. please add the same annotation format above your code and sort your solutions according to the quality of the solution. The solution with the best performance should be set on the above of the whole script.

##### NOTICE

'''@name:\<one space\>\<topic number in leetcode repos\>\<dot\>\<one space\>topic name

'''

> We should capitalize the first letter of each word in "topic name"

***There is a template script whose name is called "add_two_numbers.py"***

#### Tools

**run.py**

1. update log files

   ```shell
   # our path is $dir/src/tools/
   python run.py --update --folder ../Wangtianyi/Python/ --log ../Wangtianyi/py_map
   ```

2. get the topic information from the name of script

   ```shell
   # our path is $dir/src/tools/
   python run.py --search haha.py --log Wangtianyi/py_map
   ```

   