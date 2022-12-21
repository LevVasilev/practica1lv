import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {
        int n;
        System.out.println("Введите число больше 5");
        Scanner input = new Scanner(System.in);
        //n = input.nextInt();
        if (input.hasNextInt()) {
            do{
                n = input.nextInt ();
                if (n <= 5)
                {System.out.println("Повтори");}
            }
            while (n <= 5);


            int[] mas1 = new int[n];
            System.out.println("массив из " + n + " случайных целых чисел от 0 до " + n );
            for (int i = 0; i < n; i++) {
                mas1[i] = (int) (Math.random() * n);
                System.out.print(mas1[i] + " ");
            }


            System.out.println("\n");
            System.out.println("массив из чётных случайных целых чисел от 0 до " + n );
            for (int j = 0; j < n; j++) {
                if (mas1[j] % 2 < 1) {
                    System.out.print(mas1[j] + " ");
                }
            }
        }
    }

}
