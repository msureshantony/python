class Multiplefunctions():
    def Subfields():
        flds = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for fld in flds:
            print(fld)
        return

    def OddEven():
         num=int(input("Enter a number: "))
         if (num%2==0):
            retTxt=print(num,"is an Even Number")
         else:
            retTxt=print(num,"is a Odd Number")
         return retTxt   

    def Eligibile():
        sex=input("Enter your gender: ")
        age=int(input("Enter your age: "))
        if (sex=='Male'):
            if (age > 20):
                retTxt='Eligible'
            else:
                retTxt='InEligible'
        else:
            if (age > 17):
                retTxt='Eligible'
            else:
                retTxt='InEligible'
        return retTxt

    def percentage():
        sub1=int(input("Subject1 = "))
        sub2=int(input("Subject2 = "))
        sub3=int(input("Subject3 = "))
        sub4=int(input("Subject4 = "))
        sub5=int(input("Subject5 = "))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total : ",total)
        percent=total/5
        print("Percent : ", percent)
        return

    def triangle():
        height=int(input("Height = "))
        breadth=int(input("Breadth = "))
        height2=int(input("Height2 = "))
        area=(height*breadth)/2
        perimeter=height+breadth+height2
        print("Area of Triangle: ",area)
        print("Perimeter of Triangle: ",perimeter)