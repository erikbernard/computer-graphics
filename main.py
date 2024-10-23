from OpenGL.GL import *
from OpenGL.GLUT import *

# configuraÃ§Ãµes iniciais
def inicio():
    glClearColor(0,0,0,1) # define a cor de fundo da janela

# funÃ§Ã£o definida para atualizar o desenho da janela
def desenha():
    # atribui a cor de fundo a toda a janela
    glClear(GL_COLOR_BUFFER_BIT) 

    # desenha um triÃ¢ngulo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5,-0.5)
    glVertex2f( 0.5,-0.5)
    glVertex2f( 0.0, 0.5)
    glEnd()

    # ForÃ§a a exibiÃ§Ã£o da imagem criada na janela
    glFlush()

# corpo principal
glutInit()                      # inicializaÃ§Ã£o da GLUT e da OpenGL
glutInitWindowSize(500,500)     # tamanho inicial da janela em pixels
glutCreateWindow('Ola Mundo')   # criando a janela com tÃ­tulo

inicio()                        # configuraÃ§Ãµes iniciais
glutDisplayFunc(desenha)        # definindo que funÃ§Ã£o serÃ¡ usada para redesenhar a tela

glutMainLoop()                  # mantendo a janela aberta em um laÃ§o interno
