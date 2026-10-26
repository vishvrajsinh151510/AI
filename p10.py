#Name: Vishvrajsinh zala
#Eno : 92600584082
# Rule Based System For CAREER GUIDANCE

print('='*30)
print('      CAREER GUIDANCE SYSTEM       ')
print('='*30)

print('Answer the following question with yes or no.')

q1=input('Do you like coding? : Yes/No =').lower()
q2=input('Do you like mathematics? : Yes/No =').lower()
q3=input('Do you like bialogy? : Yes/No =').lower()
q4=input('Do you like drawing? : Yes/No =').lower()

print('========Career Suggestion========')

if(q1=='no' and q2=='no' and q3=='no' and q4=='no'):
    print('Suggested Career : Explor your interestes and career options further.')

elif(q1=='no' and q2=='no' and q3=='no' and q4=='yes'):
    print('Suggested Career : Graphic Designer / Animator.')

elif(q1=='no' and q2=='no' and q3=='yes' and q4=='no'):
    print('Suggested Career : Pharmacist / Nurse.')

elif(q1=='no' and q2=='no' and q3=='yes' and q4=='yes'):
    print('Suggested Career : Medical illustrator / Healthcare Educator.')

elif(q1=='no' and q2=='yes' and q3=='no' and q4=='no'):
    print('Suggested Career : Engineer / Data Analyst.')

elif(q1=='no' and q2=='yes' and q3=='no' and q4=='yes'):
    print('Suggested Career : Architect.')

elif(q1=='no' and q2=='yes' and q3=='yes' and q4=='no'):
    print('Suggested Career : Doctor.')

elif(q1=='no' and q2=='yes' and q3=='yes' and q4=='yes'):
    print('Suggested Career : Medical illustrator / Biomedical Designer.')

elif(q1=='yes' and q2=='no' and q3=='no' and q4=='no'):
    print('Suggested Career : Programmer / Web Developer.')

elif(q1=='yes' and q2=='no' and q3=='no' and q4=='yes'):
    print('Suggested Career : Web Developer Ui-Ux Designer.')

elif(q1=='yes' and q2=='no' and q3=='yes' and q4=='no'):
    print('Suggested Career : Health App Developer.')

elif(q1=='yes' and q2=='no' and q3=='yes' and q4=='yes'):
    print('Suggested Career :  Medical illustrator.')

elif(q1=='yes' and q2=='yes' and q3=='no' and q4=='no'):
    print('Suggested Career : Software Engineer / Computer Scientist.')

elif(q1=='yes' and q2=='yes' and q3=='no' and q4=='yes'):
    print('Suggested Career : Game Developer / UI Engineer.')

elif(q1=='yes' and q2=='yes' and q3=='yes' and q4=='no'):
    print('Suggested Career : Bioinformatics Scientist.')

elif(q1=='yes' and q2=='yes' and q3=='yes' and q4=='yes'):
    print('Suggested Career : Biomedical Software Engineer / Medical Technology Specialist.')

else:
    print('plese enter yes or no')

print('\n | Thank you using the career guidance Expert system |')
    