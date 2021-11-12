@ Fri Nov 12 09:28:30 2021                   YOUR NAME HERE
@ Compiler    = c2.py
@ Input file  = c2.in
@ Output file = c2.s
@------------------------------------------- Assembler code
          .global main
          .text
main:
          push {lr}

@ print(-59 + 20*3)
          ldr r1, =.i_59
          ldr r1, =.i20
          ldr r1, =.i3
          ldr r1, =.i60
          ldr r0, =.i_59
          ldr r0, [r0]
          ldr r1, =.i60
          ldr r1, [r1]
          add r0, r0, r1
          ldr r1, =.t0
          ldr r1, =.t0
          str r0, [r1]
          ldr r1, =.i119
          ldr r0, =.z0
          ldr r1, =.i119
          ldr r1, [r1]
          bl printf

@ a = 2
          ldr r1, =a
          ldr r1, =.i2
          ldr r0,  =.i2
          ldr r0, [r0]
          ldr r1, =a
          str r0, [r1]

@ bb_1 = -(a) + 12
          ldr r1, =bb_1
          ldr r0, =a
          ldr r0, [r0]
          neg r0, r0
          ldr r1, =.t1
          ldr r1, =.t1
          str r0, [r1]
          ldr r1, =.i12
