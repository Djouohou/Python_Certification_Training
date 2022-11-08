                                                                             
#HIGH-LEVEL MODULE INTERFACE

Un descripteur de fichier est une petite valeur entière qui correspond à un fichier ou à une autre ressource d'entrée/sortie, comme un tuyau ou une prise réseau.
Il s'agit d'un indicateur abstrait d'une ressource qui sert de poignée pour effectuer diverses opérations d'entrée/sortie de niveau inférieur, comme la lecture,
l'écriture, l'envoi, etc. 

#io.DEFAULT_BUFFER_SIZE

   An int containing the default buffer size used by the module’s buffered I/O classes.
import io
print(io.DEFAULT_BUFFER_SIZE)    #8192    


#io.open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)      This is an alias for the builtin open() function.

import io
print(io.open("fiche.txt", mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None))  #<_io.TextIOWrapper name='fiche.txt' mode='r' encoding='cp1252'>

fichier=io.open("fiche.txt", mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
print(fichier.read())       #le contenu du fichier est effectivement lu


#io.open_code(path)
"""
    Ouvre le fichier fourni avec le mode 'rb'. Cette fonction doit être utilisée lorsque l'intention est de traiter le contenu comme un code exécutable.
    path should be a str and an absolute path.
"""
import io
f=io.open_code('fiche.txt')
print(f.read())          #b'Hello \r\nThis is python \r\nThis is my txt file\r\nThis is a test file\r\n'


#io.text_encoding(encoding, stacklevel=2, /)
"""
    This is a helper function for callables that use open() or TextIOWrapper and have an encoding=None parameter.
    This function returns encoding if it is not None and "locale" if encoding is None.
    This function emits an EncodingWarning if sys.flags.warn_default_encoding is true and encoding is None. stacklevel specifies where the warning is emitted. 
"""
import io
print(io.text_encoding('utf-8'))       #utf-8
print(io.text_encoding(None))        #locale


def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()                                  #In this example, an EncodingWarning is emitted for the caller of read_text().Car l'encoding est NONE.

read_text('fiche.txt', encoding)          Traceback (most recent call last):
                                            File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 21, in <module>
                                             read_text('fiche.txt')
                                            File "C:\Users\Ingrid\Desktop\COURS PROGRAMME\Course Level PCAP\Prog.py", line 18, in read_text
                                            with open(path, encoding) as f:
                                           ValueError: invalid mode: 'locale'



#exception io.BlockingIOError
"""
    This is a compatibility alias for the builtin BlockingIOError exception.
"""
import io
print(io.BlockingIOError)       #<class 'BlockingIOError'>



#exception io.UnsupportedOperation
"""
    An exception inheriting OSError and ValueError that is raised when an unsupported operation is called on a stream.
"""
import io
print(io.UnsupportedOperation)       #<class 'io.UnsupportedOperation'>



#IOBase provides these data attributes and methods:

#close()

    Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing)
    will raise a ValueError. As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.

f=open('fiche.txt', 'r')
print(f.close()) 

#closed         Returns True if the stream is closed.

f=open('fiche.txt', 'r')
print(f.closed)  #False

f=open('fiche.txt', 'r')
f.close
print(f.closed)  #True
 

#fileno()   Return the underlying file descriptor (an integer) of the stream if it exists. An OSError will occur if the operator system does not use a file descriptor.

f = open("fiche.txt", "r")
print(f.fileno())       #3


#flush()     Vide le flux d’écriture, ne fait rien en lecture.
Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
The flush() method in Python file handling clears the internal buffer of the file. In Python, files are automatically flushed while closing them.
However, a programmer can flush a file before closing it by using the flush() method.

f = open("fiche.txt", "r")
f.flush()      #it does not affect the content of the file. So, the contents of the file can be read and displayed.

Example 2:
In this program initially, we create a gfg.txt file and write Geeks 4 geeks! as content in it and then we close the file. After that,
we read and display the contents of the file, and then the flush() method is called which clears the input buffer of the file so the file object
reads nothing and file content remains an empty variable. Hence nothing is displayed after the flush() method.

# program to demonstrate the use of flush()
 
# creating a file
fileObject = open("test.txt", "w+")
 
# writing into the file
fileObject.write("testeur de fonction !")
 
# closing the file
fileObject.close()
 
 
# opening the file to read its content
fileObject = open("test.txt", "r")
 
# reading the contents before flush()
fileContent = fileObject.read()
 
# displaying the contents
print("\nBefore flush():\n", fileContent)      #ici le contenu du fichier est lu

# clearing the input buffer
fileObject.flush()
 
# reading the contents after flush()
# reads nothing as the internal buffer is cleared
fileContent = fileObject.read()
 
# displaying the contents
print("\nAfter flush():\n", fileContent)     #le contenu est vide car le buffer a ete efface
 
# closing the file
fileObject.close()


#isatty()    Retourne True si le flux est connecté à un terminal.
Return True if the stream is interactive (i.e., connected to a terminal/tty device).

f = open("fiche.txt", "r")
print(f.isatty())      #False



#readable()   method returns True if the file is readable, False if not. If False, read() will raise OSError.
f = open("fiche.txt", "r")
print(f.readable())     #True

#readline(size=- 1)               size :Optional. The number of bytes from the line to return. Default -1, which means the whole line.

    Read and return one line from the stream. If size is specified, at most size bytes will be read.
    The line terminator is always b'\n' for binary files; for text files, the newline argument to open() can be used to select the line terminator(s) recognized.

f = open("fiche.txt", "r")       #ici lit la premiere ligne et la deuxieme
print(f.readline())      
print(f.readline())

f = open("fiche.txt", "r")       #ici lit les 3 premier caracteres
print(f.readline(3))

#readlines(hint=- 1, /)        Return all lines in the file, as a list where each line is an item in the list object: 

    Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total
    size (in bytes/characters) of all lines so far exceeds hint.
    hint values of 0 or less, as well as None, are treated as no hint.
    Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
HINT: 	Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. Default value is  -1, which means all lines will be returned.

f = open("fiche.txt", "r")
print(f.readlines())       # ['Hello \n', 'This is python \n', 'This is my txt file\n', 'This is a test file\n'] 
print(f.readlines(3)) #[]  

f = open("fiche.txt", "r")
print(f.readlines(2)) # la liste contenant la premiere ligne est affiche  
# pourquoi cest le cas peut importe le parametre


#seek(offset, whence=SEEK_SET, /)       Return the new absolute position. which defines from where the data has to be read or written in the file. 

    Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence.
    The default value for whence is SEEK_SET. Values for whence are:

        SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive

        SEEK_CUR or 1 – current stream position; offset may be negative

        SEEK_END or 2 – end of the stream; offset is usually negative

f = open("fiche.txt", "r")
 
# Second parameter is by default 0
f.seek(20)    # sets Reference point to twentieth ,index position from the beginning
print(f.tell())  # prints current position
print(f.readline())
f.close()

Example 2: Seek() function with negative offset only works when file is opened in binary mode. Let’s suppose the binary file contains the following text.
b'Python est un langage de programmation de haut, niveau.'

f = open("data.txt", "rb")    #opening the file in binary mode
 
f.seek(-10, 2)   # sets Reference point to tenth position to the left from end
print(f.tell())
 #Converting binary to string and printing
print(f.readline().decode('utf-8'))            result: t, niveau.   
f.close()


#seekable()
returns True if the file is seekable,False if not.A file is seekable if it allows access to the file stream if False, seek(), tell() and truncate() will raise OSError.
f = open("fiche.txt", "r")
print(f.seekable())   #True


#tell()    Return the current stream position.
f = open("fiche.txt", "r")
print(f.tell())   #0
f.seek(10)
print(f.tell())    #10


#truncate(size)
    Resize the stream to the given size in bytes (or the current position if size is not specified). The current stream position isn’t changed.
    This resizing can extend or reduce the current file size. This method would not work in case file is opened in read-only mode.
fo = open("fiche.txt", "r+")
print ("Name of the file: ", fo.name)   #Name of the file:  fiche.txt
fo.truncate()
line = fo.readline()
print("Read Line: %s" % (line))    #Read Line:
fo.close

fo = open("fiche.txt", "r+")
fo.truncate(3)
line = fo.readline()
print("Read Line: %s" % (line))    #Read Line: pre (ici les trois premiers caracteres du fichier son conservé)
fo.close



#writable() Retourne True si on peut écrire depuis le flux. Si False, write() lève une exception OSError.
    Return True if the stream supports writing. If False, write() and truncate() will raise OSError.
f = open("fiche.txt", "r")
print(f.writable())   #True


#writelines(lines, /)   lines is The list of texts or byte objects that will be inserted.

    Write a list of lines to the stream. Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end.
f = open("fiche.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()
#open and read the file after the appending:
f = open("fiche.txt", "r")
print(f.read())        #See you soon!Over and out.

f = open("fiche", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()
#open and read the file after the appending:
f = open("fiche.txt", "r")
print(f.read()) #See you soon!Over and out.


#__del__()

    Prepare for object destruction. IOBase provides a default implementation of this method that calls the instance’s close() method.
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')    #Employee created.
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')   #Destructor called, Employee deleted.
 
obj = Employee()
del obj


#RawIOBase     Base class for raw binary streams. It inherits IOBase. RawIOBase provides these methods in addition to those from IOBase:

#read(size=- 1, /)

    Read up to size bytes from the object and return them. As a convenience, if size is unspecified or -1, all bytes until EOF are returned. Otherwise,
    only one system call is ever made. Fewer than size bytes may be returned if the operating system call returns fewer than size bytes.

    If 0 bytes are returned, and size was not 0, this indicates end of file. If the object is in non-blocking mode and no bytes are available, None is returned.

f = open("fiche.txt", "r")
print(f.read())    



#readall()
    Read and return all the bytes from the stream until EOF(End Of File), using multiple calls to the stream if necessary.
f = open("fiche.txt", "r")
print(f.read())    #AttributeError: '_io.TextIOWrapper' object has no attribute 'readall'. Did you mean: 'readable'?



#readinto(b, /)
    Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read. For example, b might be a bytearray.
    If the object is in non-blocking mode and no bytes are available, None is returned.
f = open("fiche.txt", "r")
print(f.readinto)#AttributeError: '_io.TextIOWrapper' object has no attribute 'readinto'. Did you mean: 'readline'?


#write(b, /)
    Write the given bytes-like object, b, to the underlying raw stream, and return the number of bytes written. This can be less than the length of b in bytes,
    depending on specifics of the underlying raw stream, and especially if it is in non-blocking mode. None is returned if the raw stream is set not to block and
    no single byte could be readily written to it. 
f = open("fiche", "w")
f.write("See you soon!")
f.write("Thank you!")
f.close()


#BufferedIOBase Base class for binary streams that support some kind of buffering. It inherits IOBase. provides these attributes and methods in addition to those from IOBase:
        
#raw

    The underlying raw stream (a RawIOBase instance) that BufferedIOBase deals with.
    This is not part of the BufferedIOBase API and may not exist on some implementations.

#detach()

    Separate the underlying raw stream from the buffer and return it.
    After the raw stream has been detached, the buffer is in an unusable state.
    Some buffers, like BytesIO, do not have the concept of a single raw stream to return from this method. They raise UnsupportedOperation.
f = open("fiche", "r")
print(f.detach())          #<_io.BufferedReader name='fiche'>

f.close()       #ValueError: underlying buffer has been detached


#read(size=- 1, /)

    Read and return up to size bytes. If the argument is omitted, None, or negative, data is read and returned until EOF is reached.
    An empty bytes object is returned if the stream is already at EOF.
    If the argument is positive, and the underlying raw stream is not interactive, multiple raw reads may be issued to satisfy the byte count
    (unless EOF is reached first). But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

#read1(size=- 1, /)

    Read and return up to size bytes, with at most one call to the underlying raw stream’s read() (or readinto()) method.
    If size is -1 (the default), an arbitrary number of bytes are returned (more than zero unless EOF is reached).

fo = open("fiche.txt", "r")
line = fo.read1(3)
print("Read1 : %s" % (line))    #AttributeError: '_io.TextIOWrapper' object has no attribute 'read1'. Did you mean: 'read'?
fo.close


#readinto(b, /)
    Read bytes into a pre-allocated, writable bytes-like object b and return the number of bytes read. For example, b might be a bytearray.
    Like read(), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.



#readinto1(b, /)

    Read bytes into a pre-allocated, writable bytes-like object b, using at most one call to the underlying raw stream’s read() (or readinto()) method.
    Return the number of bytes read.
    A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

#write(b, /)
    Write the given bytes-like object, b, and return the number of bytes written (always equal to the length of b in bytes, since if the write fails an OSError
    will be raised). Depending on the actual implementation, these bytes may be readily written to the underlying stream, or held in a buffer for performance and
    latency reasons.
    When in non-blocking mode, a BlockingIOError is raised if the data needed to be written to the raw stream but it couldn’t accept all the data without blocking.



#BUFFERED STREAMS   Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does.

#BytesIO(initial_bytes=b'')       BytesIO provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#getbuffer()   Note :As long as the view exists, the BytesIO object cannot be resized or closed.
Return a readable and writable view over the contents of the buffer without copying them. Also, mutating the view will transparently update the contents of the buffer:

import io
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
print(b.getvalue())     #b'ab56ef'

#getvalue()    Return bytes containing the entire contents of the buffer.

#read1(size=- 1, /)        In BytesIO, this is the same as read().

#readinto1(b, /)            In BytesIO, this is the same as readinto().



#BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)
    A buffered binary stream providing higher-level access to a readable, non seekable RawIOBase raw binary stream. It inherits BufferedIOBase.
    BufferedReader provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#peek(size=0, /)
Return bytes from the stream without advancing the position. At most one single read on the raw stream is done to satisfy the call. The number of bytes returned
may be less or more than requested.
f = open("fiche.txt", "r")
print(f.peek())   #AttributeError: '_io.TextIOWrapper' object has no attribute 'peek'. Did you mean: 'seek'?      


#read(size=- 1, /)         Read and return size bytes, or if size is not given or negative, until EOF or if the read call would block in non-blocking mode.

#read1(size=- 1, /)
Read and return up to size bytes with only one call on the raw stream. If at least one byte is buffered, only buffered bytes are returned. Otherwise, one raw stream
read call is made.



#BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)
    A buffered binary stream providing higher-level access to a writeable, non seekable RawIOBase raw binary stream. It inherits BufferedIOBase.
    BufferedWriter provides or overrides these methods in addition to those from BufferedIOBase and IOBase:

#flush()     Force bytes held in the buffer into the raw stream. A BlockingIOError should be raised if the raw stream blocks.

#write(b, /)
Write the bytes-like object, b, and return the number of bytes written. When in non-blocking mode, a BlockingIOError is raised if the buffer needs to be written out
but the raw stream blocks.




#TEXT I/O

#CLASS io.TextIOBase
    Base class for text streams. This class provides a character and line based interface to stream I/O. It inherits IOBase.
    TextIOBase provides or overrides these data attributes and methods in addition to those from IOBase:

    #encoding     The name of the encoding used to decode the stream’s bytes into strings, and to encode strings into bytes.

    #errors     The error setting of the decoder or encoder.

    #newlines     A string, a tuple of strings, or None, indicating the newlines translated so far. 

    #buffer   The underlying binary buffer (a BufferedIOBase instance) that TextIOBase deals with.

    #detach()    Separate the underlying binary buffer from the TextIOBase and return it.

    #read(size=- 1, /)      Read and return at most size characters from the stream as a single str. If size is negative or None, reads until EOF.

    #readline(size=- 1, /)
    Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.
    If size is specified, at most size characters will be read.

    #seek(offset, whence=SEEK_SET, /     Return the new absolute position as an opaque number.
    Change the stream position to the given offset. Behaviour depends on the whence parameter. The default value for whence is SEEK_SET.

        SEEK_SET or 0: seek from the start of the stream (the default); offset must either be a number returned by TextIOBase.tell(), or zero. Any other offset
        value produces undefined behaviour.

        SEEK_CUR or 1: “seek” to the current position; offset must be zero, which is a no-operation (all other values are unsupported).

        SEEK_END or 2: seek to the end of the stream; offset must be zero (all other values are unsupported).

    #tell()     Return the current stream position as an opaque number. The number does not usually represent a number of bytes in the underlying binary storage.

    #write(s, /)    Write the string s to the stream and return the number of characters written.


#TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)

    A buffered text stream providing higher-level access to a BufferedIOBase buffered binary stream. It inherits TextIOBase.
    TextIOWrapper provides these data attributes and methods in addition to those from TextIOBase and IOBase:

    #line_buffering   Whether line buffering is enabled.

    #write_through     Whether writes are passed immediately to the underlying binary buffer.

    #reconfigure(*[, encoding][, errors][, newline][, line_buffering][, write_through])
       Reconfigure this text stream using new settings for encoding, errors, newline, line_buffering and write_through.
    Parameters not specified keep current settings, except errors='strict' is used when encoding is specified but errors is not specified.
 It is not possible to change the encoding or newline if some data has already been read from the stream. On the other hand, changing encoding after write is possible.
 

#StringIO(initial_value='', newline='\n')
    A text stream using an in-memory text buffer. It inherits TextIOBase.
    StringIO provides this method in addition to those from TextIOBase and IOBase:

    #getvalue()    Return a str containing the entire contents of the buffer. Newlines are decoded as if by read(), although the stream position is not changed.
import io
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
print(b.getvalue())   











