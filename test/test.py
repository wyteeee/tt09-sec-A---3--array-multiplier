# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test


    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    

    dut.ui_in.value = 0x1_4 
      
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x04  
    # dut.uio_in.value = 0xFF 
    
    # Test case 2: All zeros in A
    dut.ui_in.value = 0x1_1 # Input A: 00000000
    #dut.uio_in.value = 0xFF 
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1

    # Test case 3: All zeros in B
    dut.ui_in.value = 0x2_6 
    #dut.uio_in.value = 0x00  
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 12

    # Test case 4: Identical inputs
    dut.ui_in.value = 0x3_3  # Input A: 00110011
    #dut.uio_in.value = 0x33  # Input B: 00110011
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 9

    # Test case 5: Alternating bits
    dut.ui_in.value = 0x7_8  # Input A: 00001111
    #dut.uio_in.value = 0xF0  # Input B: 11110000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 56

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
