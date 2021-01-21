from OpenGL.GL import *
from glew_wish import *
import glfw
import random


def main ():
            #inicia glfw
        if not glfw.init():
            return
        
        #crea la ventana
        #independientemente del SO que usemos
        window = glfw.create_window(800,600,'Mi ventana', None, None)

        #configuracimos OpenGL
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        #validamos que se cree la ventana
        if not window:
            glfw.terminate()
            return
        #Establecemos el contexto
        glfw.make_context_current(window)

        #Activamos la validacion de funciones modernas en OpenGL
        glewExperimental = True 

        #Inicializar Glem
        if not window:
            glfw.terminate()
            return
        #Establecemos el contexto
        glfw.make_context_current(window) 

        #Obtener version
        version = glGetString(GL_VERSION)
        print(version)
        
        version_shaders =glGetString(GL_SHADING_LANGUAGE_VERSION)
        print(version_shaders)

        while not glfw.window_should_close(window):
            #establece region
            glViewport(0,0,800,600)

            r = random.random()
            g = random.random()
            b = random.random()
            a = random.random()

            glClearColor(r,g,b,a)
            #borrar contenido de ventana
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            #Dibujar

            #Preguntar si hubo entradas de perifericos
            #(Teclado,mouse,gamepad,etc.)
            glfw.poll_events()
            #intercambia los buffers
            glfw.swap_buffers(window)


        #Se destruye la ventana para liberar memoria
        glfw.destroy_window(window)
        #termina los procesos que inicio
        glfw.terminate()

if __name__ == "__main__":
    main()


