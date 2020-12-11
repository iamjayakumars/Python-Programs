while True:
    name = input('Enter name:')           
    if name == 'stop': 
        break 
    age  = input('Enter age: ') 
    print('Hello', name, '=>', int(age) )


Output:
Enter name:bob 
Enter age: 40 
Hello bob => 40