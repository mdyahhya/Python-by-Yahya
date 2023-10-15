def main():
    try:
        age = int(input('enter age:'))
        if age<=0:
            raise ValueError #throw
        #end : if
        
        print(f'you are {age} years old')
    except ValueError : #catch
        print(f'{age} is invalid \n'
            f'age cannot be -ve')
    #except
#end : main
        
main()
            
