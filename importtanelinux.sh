#!/bin/bash
cat <<END 
hi this is shobhit srivastava
and i am curently syduing in nit srinagar
and having brach computer science
END


echo " gedit ~/.bashrc"


echo "function addition "

getsum(){
num3=$1
num4=$2
sum=$((num3+num4))



# or print thorugh the following 
# sum=$((num1+num2))


echo $sum
}
num1=50
num2=6
sum=$(getsum num1 num2)
echo "thse sum is $sum"








num1=87
num2=23
num3=$(python -c "print $num1+$num2")
echo "$num3"





getdate(){
date 
return
}
getdate



#READING THE INPUT FROM THE USER





read -p "what is your name" name
read -p "enter the number" num
echo "Hello $name"

if((num==1));then
echo "your number equals one"
else
echo "your number is other than 1"
fi


#IF DIRECTORY DOENT EXIT THEN MAKE IT

[ -d sam_dir ] || mkdir sam_dir


#Reduce Lambda Function Use


b=reduce(lambda x,y: x if(x>y) else y,[11,75,89,8])
print b
