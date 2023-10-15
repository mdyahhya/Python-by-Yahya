def display(**record):#record:dict
    print('Record:')
    for k,v in  record.items():
        print(f'{k}:{v}')
    #end : for
#end : display
def main():
    display(company='Yamaha',cost=90000)
    display(name='Raj',roll=101,percent=90.77)
#end : main
main()

'''
Comment - OUTPUT:
Record:
company:Yamaha
cost:90000
Record:
name:Raj
roll:101
percent:90.77
'''
