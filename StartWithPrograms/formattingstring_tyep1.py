brand = 'Apple'

message = "The price of the %s laptop is %d" %(brand, 1466)
print(message)

message = "The price of the %s laptop is %5d" %(brand, 1466)
print(message)


exchangeRate = 92.7074

message1 = "The exchange rate is %4.2f Rupees to 1 Pound" %(exchangeRate)
print(message1)

messageFormatString = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EURO'.format('Apple', 1989, 1.4897755445)
print(messageFormatString)                                                                                                                       
                                                                                                                       

messageWithoutFormat = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EURO'.format('Apple', 1989, 1.4897755445)
print(messageWithoutFormat)                                                                                                                       
                                                                                                                       

            
