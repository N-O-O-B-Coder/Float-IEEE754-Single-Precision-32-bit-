def decimal_to_binary(integer):
    binary_integer=[]
    while(integer/2>=1):
        i=int(integer%2)
        binary_integer.append(i)
        integer/=2
    if(len(binary_integer)>1):
        binary_integer.reverse()
    binary_integer.insert(0,1)
    return binary_integer

def float_to_binary(decimal):
    binary_float=[]
    count=1
    product=decimal
    while(count<=23):
        product=product*(10**-len(str(product)))
        product *=2
        decimal_int,dec_rem=str(product).split('.')
        decimal_int=int(decimal_int)
        dec_rem=int(dec_rem)
        binary_float.append(decimal_int)
        if (product==1.0):
            binary_float=str.ljust(23-len(str(binary_float)),'0')
            break
        else:
            product=dec_rem
        count +=1
    return binary_float

def list_to_string(list):
    list_string=''.join([str(elem) for elem in list ])
    return list_string

def ieee_754_conversion(num):

    
    integer,decimal=str(num).split('.')
    sign_check=[]
    sign_check=integer
    if integer[0][0]=='-':
        integer[0]=integer[0][1:]
    integer=int(integer)
    decimal=int(decimal)

    binary_integer_part=decimal_to_binary(integer)
    
    exponent=127 + len(str(binary_integer_part))-1
    binary_exponent=decimal_to_binary(exponent)
    if (len(str(binary_exponent))==7):
        binary_exponent.insert(0,0)
    if sign_check[0][0]=='-':
        binary_exponent.insert(0,1)
    else:
        binary_exponent.insert(0,0)


    binary_float_part=float_to_binary(decimal)

    binary_exponent=list_to_string(binary_exponent)
    binary_integer_part=list_to_string(binary_integer_part)
    binary_float_part=list_to_string(binary_float_part)

    res1="".join((binary_exponent,binary_integer_part))
    res_final="".join((res1,binary_float_part))

    return res_final
   
num=float(input('Enter a floating point decimal number:'))

ieee=ieee_754_conversion(num)

print(ieee)

    
    

    