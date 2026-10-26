#Name: Vishvrajsinh zala
#Eno : 92600584082
# Expert System For Medical Diagnosis

print('==== Expert System ====')

print('Ansewr the following questions with yes or no')

fever=input(print('Do you have fever? : Yes/No')).lower()
cough=input(print('Do you have cough? : Yes/No')).lower()
headache=input(print('Do you have headache? : Yes/No')).lower()

if(fever=='no' and cough=='no' and headache=='no'):
    print('you seem to be healthy')

elif(fever=='yes' and cough=='no' and headache=='no'):
    print('you may have a mild infaction')

elif(fever=='no' and cough=='yes' and headache=='no'):
    print('you may have a throut infaction or mild cold')

elif(fever=='no' and cough=='no' and headache=='yes'):
    print('you may have a stress, magaine, or fatigue')

elif(fever=='yes' and cough=='yes' and headache=='no'):
    print('you may have flu')

elif(fever=='yes' and cough=='no' and headache=='yes'):
    print('you may have a viral fever')

elif(fever=='no' and cough=='yes' and headache=='yes'):
    print('you may have a mild common cold')

elif(fever=='yes' and cough=='yes' and headache=='yes'):
    print('you may have a flu or a viral infection')

else:
    print('plese enter yes or no')