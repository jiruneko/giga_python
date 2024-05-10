def print_hello():
    print("hello world")
    
print_hello()

def num_max(a, b):
    print('a = {}, b = {}'.format(a, b))
    if a < b:
        return a
    else:
        return b

print(num_max(b=100,a=20))
print(num_max('20', '30'))