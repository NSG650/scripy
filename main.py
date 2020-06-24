import compiler
print("wait it worked till here now let us see")
print("type exit to exit")
print("type help to get help")
while True:
    text = input('scripy% ')
    if text == 'exit':
        break
    elif text == 'help':
        print("Welcome to Scripy! Right now you can do basic condition checks and assign variables along with do maths operations")
        print("use VAR to declare a variable, IF THEN ELIF ELSE for conditions, AND ,OR ,NOT for use with conditions")
    else:
        result, error = compiler.run('<stdin>', text)
        if error: print(error.as_string())
        else: print(result)
