JFLAGS = -g
JC = javac

.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	Secuencial.java \
    Fork.java \
	Threads.java

default: classes

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class

run:
	@java Secuencial
	@java Fork
	@java Threads
