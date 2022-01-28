# TC358870_Drivers
一些TC358870XBG HDMI转MIPI桥接器的驱动程序。  

# 硬件
本项目硬件基于zengcym的硬件: [链接](https://github.com/zengcym/HDMI-To-MIPI)。  
注意：该电路板存在一个问题,I2C的电路没有上拉电阻。如果想要使用本工程的代码，需要在板子上飞两个1k电阻到I2C总线上，或者使用软件模拟I2C。  
MCU使用STM32F103C8T6。  

# 软件
软件方面，使用PlatformIO作为IDE，STM32Cube HAL库作为SDK。