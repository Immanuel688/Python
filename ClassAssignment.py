class ClassAssignment():
    def SubfieldsinAI():
        list=['Machine Learning','Neural Networks','Vision','Robotics','speech    processing','Natural language processing']
        print("Sub-fields in AI are :")
        for subfields in list:
                print(subfields)
                
    def oddeven():
        num=int(input("enter the number:"))
        if((num%2)==0):
            print(num,"is even number")
        else:
            print(num,"is odd number")
            
    def marriageeligibiity():
        gender=input("your gender:")
        age=int(input("your age:"))
        if(gender=='male'):
            if(age>21):
                print("eligible")
            else:
                print("not eligible")
        if(gender=='female'):
            if(age>18):
                print("eligible")
            else:
                print("not eligible")
                
    def findpercent():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        Total=subject1+subject2+subject3+subject4+subject5
        print("Total:",Total)
        print("percentage:",(Total/500)*100)
        
    def triangle():
        height=int(input("height :"))
        breadth=int(input("breadth :"))
        print("Area formula:(height*breadth)/2")
        print("Area of triangle", (height*breadth)/2)
        height1=int(input("height1 :"))
        height2=int(input("height2 :"))
        breadth=int(input("breadth :"))
        print("perimeter formula: height1+height2+breadth")
        print("perimeter of the triangle:", height1+height2+breadth)