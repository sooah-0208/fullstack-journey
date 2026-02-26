import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        int a;
        // int a = new A().getA();
        a = new A(152).getA();
        System.out.println(new A());

    }
}

class A {
    int a;

    public A() {
    }

    public A(int a) {
        this.a = a;
        // this = class A
    }

    int getA() {
        return a;
    }

    public String toString(){
return "A class당.";
    }
}
