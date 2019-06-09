
import java.util.*;
import java.io.*;
import java.lang.*;


public class random{
  public static void main(String[] args){

  int[] rado = new int[16];
  Random rand = new Random();
  int key =22;
  int i=1; int j=16;
  for(int p=0; p<16; p++){
    rado[p] = rand.nextInt(25);
  }
   //ArrayList<Integer> ola = new ArrayList<>(Arrays.asList(rado));
   Arrays.sort(rado);
   //int[] rado2= (Integer) ola.toArray();
   for (int d=0; d<rado.length; d++)
   {
     System.out.print (rado[d]+" ");}
     System.out.print("\n");
  while(i<j){

    int mid = rado[(i+j)/2];
    System.out.println("Element="+ rado[mid] + " i=" + i +" j="+ j+" m="+mid);
    if (mid==key){

      System.out.println("Yahoo, "+key+" found at index "+mid);
      break;
    }
    else if(mid<key){
      i=mid+i;
    }
    else{
      j=mid-i;
    }
  }
}}
