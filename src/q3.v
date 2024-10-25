/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_a3_array_multiplier (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
    wire [3:0] m = ui_in [7:4];
    wire [3:0] q = ui_in [3:0];
    wire [7:0] p;

    wire [3:0] m0,m1,m2,m3;
    wire c1, c2, c3, c4, c5,c6,c7,c8,c9,c10,c11,c12;
    wire s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12;
        
    assign m0[0]=m[0]&q[0];
    assign m0[1]=m[1]&q[0];
    assign m0[2]=m[2]&q[0];
    assign m0[3]=m[3]&q[0];
   
    assign m1[0]=m[0]&q[1];
    assign m1[1]=m[1]&q[1];
    assign m1[2]=m[2]&q[1];
    assign m1[3]=m[3]&q[1];
    
    assign m2[0]=m[0]&q[2];
    assign m2[1]=m[1]&q[2];
    assign m2[2]=m[2]&q[2];
    assign m2[3]=m[3]&q[2];
    
    assign m3[0]=m[0]&q[3];
    assign m3[1]=m[1]&q[3];
    assign m3[2]=m[2]&q[3];
    assign m3[3]=m[3]&q[3];
    
    
    full_adder fa1(m0[1], m1[0], 1'b0, s1, c1);
    full_adder fa2(m0[2], m1[1], c1, s2, c2);
    full_adder fa3(m0[3], m1[2], c2, s3, c3);
    full_adder fa4(c3, m1[3], c3, s4, c4);
    
    full_adder fa5(s2, m2[0], 1'b0, s5, c5);
    full_adder fa6(s3, m2[1], c4, s6, c6);
    full_adder fa7(s4, m2[2], c5, s7, c7);
    full_adder fa8(c4, m2[3], c6, s8, c8);
    
    full_adder fa9(s6, m3[0], 1'b0, s9, c9);
    full_adder fa10(s7, m3[1], c9, s10, c10);
    full_adder fa11(s8, m3[2], c10, s11, c11);
    full_adder fa12(c8, m3[3], c11, s12, c12);
    
    assign p[0] = m0[0];
    assign p[1] = s1;
    assign p[2] = s5;
    assign p[3] = s9;
    assign p[4] = s10;
    assign p[5] = s11;
    assign p[6] = s12;
    assign p[7] = c12;
    
    assign uo_out = p;
    assign uio_out = 0;
    assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
    module full_adder (
    input a,
    input b,
    input cin,
    output sum, 
    output cout
    );
    assign sum = a^b^cin;
    assign cout = (a&b)| (cin & a) |(cin & b);
endmodule
