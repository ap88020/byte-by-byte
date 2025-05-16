import java.util.Scanner;

public class conditional{
    public static void printJava(){
        System.out.println("Hllow world");
    }
    public static void printName(String name){
        System.out.println(name);
    }
    public static void printSum(int a , int b){
        int sum = a + b;
        System.out.println(sum);
    }
    public static void main(String[] args){
        // System.out.println("hllow world");       
        Scanner sc = new Scanner(System.in);

        // int cash = sc.nextInt();

        // if(cash < 10){
        //     System.out.println("can not buy anything");
        //     System.out.println("get more cash");
        // }else if (cash > 10 && cash < 60){
        //     System.out.println("you can buy only Onething");
        // }else {
        //     System.out.println("you can buy both thing");
        // }

        // String day = sc.nextLine();
        // switch (day) {
        //     case "Monday":
        //         System.out.println("schlool is open today");
        //         break;
        
        //     default:
        //     System.out.println("school is not open today");
        //         break;
        // }

        // for(int i=9; i<=40; i++){
        //     System.out.println(i);
        // }
        // for(int i=40; i>=0; i--){
        //     System.out.println(i);
        // }

        // int i=10;
        // while(i >= 0){
        //     System.out.println(i);
        //     i--;
        // }

        // int i =0;
        // while(true){
        //     if(i == 3){
        //         i++;
        //         continue;
        //     }
        //     System.out.println(i);
        //     if(i > 5){
        //         break;
        //     }
        //     i++;
        // }
        // printJava();
        // printJava();
        // printJava();
        // printJava();

        // printName("Akash");
        // printName("Anurag");

        printSum(30, 84);
    }
}