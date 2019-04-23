import freetype
from OpenGL.GL import *
from OpenGL.GLM import *

roboto = freetype.Face("./resources/fonts/Roboto/Roboto-Regular.ttf")
roboto.set_pixel_sizes(0,64)
roboto.load_char("P", flags=freetype.FT_LOAD_RENDER)

roboto.glyph.bitmap
roboto.glyph.bitmap.width
roboto.glyph.bitmap.rows
roboto.glyph.bitmap_left
roboto.glyph.bimap_top
roboto.glyph.advance.x

@dataclass
class char():
    textureID: GLuint
    size: glm.ivec2
    bearing: glm.ivec2
    advance: GLuint

glPixelStorei(GL_UNPACK_ALIGNMENT, 1) #Disable byte-alignment restriction

#Get every ascii char till 255
for i in range(255):

    #Load char glyph
    roboto.load_char(i, flags=freetype.FT_LOAD_RENDER)
    texture: GLuint
    glGenTextures(1, texture)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RED,
        roboto.glyph.bitmap.width,
        roboto.glyph.bitmap.rows,
        0,
        GL_RED,
        GL_UNSIGNED_BYTE,
        roboto.glyph.bitmap.buffer)

    #Set Texture options
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    #Store the ccharacter for later use
    character = char(
        texture,
        glm.ivec2(roboto.glyph.bitmap.width, roboto.glyph.bitmap.rows),
        glm.ivec2(roboto.glyph.bitmap_left, roboto.glyph.bitmap_top),
        roboto.glyph.advance.x)

glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

