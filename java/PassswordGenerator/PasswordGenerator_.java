import  java.util.Random;
import  java.util.Scanner;
 class PasswordGenerator_ {
 public static int n;
    
    public  static  void main(String[] args) {
        
           //create scanner to get input
        System.out.println("Welcome To Password Generator");
         Scanner Num= new Scanner(System.in);
         //checks number of digitd (max 20)
         System.out.println("Enter number of digits(4-10)");
          n = Num.nextInt();
          while(n>20){
             System.out.println("Enter number of digits(4-10)");
            n = Num.nextInt();
          }
            Num.close();

            // create an instance for the PasswordGenerator Class And then invokes the Generate method
        System.out.println("Generating......");
        PasswordGenerator ps = new  PasswordGenerator();
        ps.Generate(n);
    }

 
}
 class PasswordGenerator{
 // Password Generator

  String[] Keys={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"
                ,"w","x","y","z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","*","+"};
  Random rand = new Random();
 public  String Password ="";
       
 public  void Generate(int a){
  // Method To Generate The characters
for(int i=0;i<a;i++){

int randomNum = rand.nextInt(43- 1 + 1) + 1;

Password+=Keys[randomNum];
System.out.println("Generating Symbol "+Password.length());

}

System.out.println("Process Completed");
System.out.println("Your Password Generated  is \""+Password+"\"");
}
 
 
 
 
}
