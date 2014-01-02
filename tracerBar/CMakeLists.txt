cmake_minimum_required(VERSION 2.8)
project( TracerBar )

find_package( OpenCV REQUIRED )

add_executable( tracerBar tracerBar.cpp )

target_link_libraries( tracerBar ${OpenCV_LIBS} )
