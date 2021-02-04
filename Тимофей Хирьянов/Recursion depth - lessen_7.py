import graphics as gr

window = gr.GraphWin ("Russian game", 600, 600)
alfa = 0.2

def fractal_rectangle(A, B, C, D, deep=10)
    if deep < 1: # крайний случай
        return
    #gr.Line(gr.Point(*A), gr.Point(*B)).draw(window) # *А тоже самое A[0], A[1] развертывание этирированного объекта
    #gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    #gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    #gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    for M, N in (A,B), (B,C), (C,D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alfa) + B[0] * alfa, A[1](1 - alfa) + B[1] * alfa)
    B1 = (B[0] * (1 - alfa) + C[0] * alfa, B[1](1 - alfa) + C[1] * alfa)
    C1 = (C[0] * (1 - alfa) + D[0] * alfa, C[1](1 - alfa) + D[1] * alfa)
    D1 = (D[0] * (1 - alfa) + A[0] * alfa, D[1](1 - alfa) + A[1] * alfa)
    fractal_rectangle(A1, B1, C1, D1, deep-1)


fractal_rectangle((100,100), (500,100), (500,500), (100, 500), 100)