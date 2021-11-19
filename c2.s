@ Tue Nov 16 20:49:21 2021                Mitchell Chappell
@ Compiler    = c2.py
@ Input file  = c2.in
@ Output file = c2.s
@------------------------------------------- Assembler code
          .global main
          .text
main:
          push {lr}

@ print(-59 + 20*3)
          ldr r0, =.i20
          mov r1, .i3
          mul r2, r0, r1
          ldr r0, =.i_59
          ldr r1, =.t0
          add r2, r0, r1
          ldr r0, =.fmt0
          ldr r1, =.t0
          ldr r1, [r1]
          bl printf

@ a = 2
          ldr r2, .i2

@ bb_1 = -(a) + 12
          mov r0, r2
          neg r0, r0
          mov r1, r0
          ldr r0
          ldr r0, [r0]
          mov r1, .i12
          add r2, r0, r1
          mov r3, r1

@ print(a*bb_1 + a*3*(-1 + -1 + -1))
          ldr r0
          ldr r0, [r0]
          ldr r1, =bb_1
          mul r2, r0, r1
          ldr r0
          ldr r0, [r0]
          mov r1, .i3
          mul r2, r0, r1
          ldr r0
          ldr r0, [r0]
          mov r1, .i_3
          mul r2, r0, r1
          ldr r0
          ldr r0, [r0]
          ldr r1, =.t1
          add r2, r0, r1
          ldr r0, =.fmt0
          ldr r1, =.t0
          ldr r1, [r1]
          bl printf
.fmt0:      .asciz "%d\n"

          mov r0, #0
          pop {pc}

          .data
.z0:      .asciz "%d\n"
.i_59:    .word -59
.i20:     .word 20
.i3:      .word 3
.t0:      .word 0
a:        .word 0
.i2:      .word 2
bb_1:     .word 0
.i12:     .word 12
.t1:      .word 0
.i_1:     .word -1
.i_2:     .word -2
.i_3:     .word -3
