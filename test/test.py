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
    dut.ui_in.value = 0x42
    dut.ui_in.value = 0x34
    dut.ui_in.value = 0x56
    dut.ui_in.value = 0x11
    dut.ui_in.value = 0x09

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 0x10
    assert dut.uo_out.value == 0x78
    assert dut.uo_out.value == 0x27
    assert dut.uo_out.value == 0x46
    assert dut.uo_out.value == 0x52

    dut.ui_in.value = 0x42
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x10

    dut.ui_in.value = 0x34
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x78

    dut.ui_in.value = 0x56
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x27

    dut.ui_in.value = 0x11
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x46

    dut.ui_in.value = 0x09
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0x52

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
