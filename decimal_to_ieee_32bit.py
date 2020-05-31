def list_to_string(list):
    list_string=''.join([str(elem) for elem in list ])
    return list_string

def decimal_to_binary(convert):
    binary_integer=[]
    while(convert/2>=1):
        i=int(convert%2)
        binary_integer.append(i)
        convert/=2
    if(len(binary_integer)>1):
        binary_integer.reverse()
    binary_integer.insert(0,1)
    return binary_integer

def float_to_binary(decimal,place):
    binary_float=[]
    count=1
    product=decimal
    while(count<=place):
        product=product*(10**-len(str(product)))
        product *=2
        decimal_int,dec_rem=str(product).split('.')
        decimal_int=int(decimal_int)
        dec_rem=int(dec_rem)
        binary_float.append(decimal_int)
        if (product==1.0):
            while(len(binary_float)<=place):
                binary_float.append(0)
            break
        else:
            product=dec_rem
        count +=1
    return binary_float

def ieee_754_conversion(num):

    
    integer,decimal=str(num).split('.')
    string=list(integer)
    sign_check=string.copy()
    if string[0][0]=='-':
        string[0]=string[0][1:]
        integer=list_to_string(string)
    integer=int(integer)
    decimal=int(decimal)

    binary_integer_part=decimal_to_binary(integer)
    exponent=127 + len((binary_integer_part))-1
    binary_exponent=decimal_to_binary(exponent)
    binary_integer_part.pop(0)
    if (len((binary_exponent))==7):
        binary_exponent.insert(0,0)
    if sign_check[0][0]=='-':
        binary_exponent.insert(0,1)
    else:
        binary_exponent.insert(0,0)

    place=23-len(binary_integer_part)
    binary_float_part=float_to_binary(decimal,place)

    binary_exponent=list_to_string(binary_exponent)
    binary_integer_part=list_to_string(binary_integer_part)
    binary_float_part=list_to_string(binary_float_part)

    res1="".join((binary_exponent,binary_integer_part))
    res_final="".join((res1,binary_float_part))

    return res_final
   
num=float(input('Enter a floating point decimal number:'))

ieee=ieee_754_conversion(num)

print(ieee)

    
    

    
