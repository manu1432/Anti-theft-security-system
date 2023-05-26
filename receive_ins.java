/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import Logic.send_ins;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author sumit
 */
public class receive_ins extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            String type=request.getParameter("type");
            System.out.println("type"+type);
            String status=request.getParameter("status");
            System.out.println("status"+status);
            if(type.equalsIgnoreCase("Buzzer") && status.equalsIgnoreCase("ON"))
            {
              
                send_ins si=new send_ins();
               si.execute("buzzeron?");
             
            }
            if(type.equalsIgnoreCase("Buzzer") && status.equalsIgnoreCase("OFF"))
            {
              
                send_ins si=new send_ins();
                si.execute("buzzeroff?");
            }
            if(type.equalsIgnoreCase("Light") && status.equalsIgnoreCase("ON"))
            {
              
                send_ins si=new send_ins();
                si.execute("ledon?");
            }
          
            if(type.equalsIgnoreCase("Light") && status.equalsIgnoreCase("OFF"))
            {
              
                send_ins si=new send_ins();
                si.execute("ledoff?");
            }
             if(type.equalsIgnoreCase("Hidden Door") && status.equalsIgnoreCase("ON"))
            {
              
                send_ins si=new send_ins();
                si.execute("open?");
            }
            if(type.equalsIgnoreCase("Hidden Door") && status.equalsIgnoreCase("OFF"))
            {
              
                send_ins si=new send_ins();
                si.execute("close?");
            }
            out.print("Instruction Sent");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
