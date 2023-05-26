/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Logic;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author manur
 */
public class control_servo extends Thread 
{
    
    public control_servo(){
    start();
    }
    public void run()
    {
        send_ins si=new send_ins();
    while(true){
    
    try{
        si.execute("sensorData?");
    }catch(Exception e)
    {
    e.printStackTrace();
    
    }
            try {
                Thread.sleep(2000);
            } catch (InterruptedException ex) {
                Logger.getLogger(control_servo.class.getName()).log(Level.SEVERE, null, ex);
            }
    
    }
    
    
    }
    public static void main(String[] args) {
        new control_servo();
    }
}
