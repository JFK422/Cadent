from OpenGL import GL

class Buffer:

    #Lists for the open Arrays an Buffers
    VAOS = None
    VBOS = []
    
    def loadToVAO(self, positions):
        vaoID = GL.glGenVertexArrays(n = 1)
        GL.glBindVertexArray(vaoID)
        Buffer.storeInVBO(self, 0, positions)
        Buffer.unbindVAO(self)

        return vaoID, len(positions)

    def storeInVBO(self, attributeNum, data):
        vboID = GL.glGenBuffers()
        Buffer.VBOS.append(vboID)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vboID)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, data, GL.GL_STATIC_DRAW)
        GL.glVertexAttribPointer(attributeNum, 3, GL.GL_FLOAT, False, 0, 0)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    
    def unbindVAO(self):
        GL.glBindVertexArray(0)

    def deleteBuffers(self):
        for i in range(len(Buffer.VAOS)):
            GL.glDeleteVertexArrays(Buffer.VAOS[i])

        for j in range(len(Buffer.VBOS)):
            GL.glDeleteBuffers(Buffer.VBOS[j])
