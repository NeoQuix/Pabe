 # Anmerkungen zu den Tasks
  -------------------------------------

 ## Task 01: Elf Header Part-1 ~abgeschlossen
 ### Theorie Aspekte
 - Elf Header Einführung (Magic Byte; .ELF 0x7F 0x45 0x4c 0x46)

 - Header wurde verschlüsselt (8 Bit Key) und man sollte es entschlüsseln

 ### Anmerkungen
 - Keine wichtige Aufgabe, Elf Header Theorie wichtig
 
 -------------------------------------
 ## Task 02: Elf Header Part-2 ~abgeschlossen
 ### Theorie Aspekte
 - Elf Header Weiterführung; wie man aus sections Werte raus parst
 
 - Lernen was Sections/Segments sind + wie halt eine ELF File grundlegend aufgebaut ist

 - Readelf Tool verstehen (wie man was auslesen kann)

 ==> z.B. readelf -h (für ELF Header) -S für Sections etc. ==> siehe man readelf

 ### Anmerkungen
 - zweiter Lösungsansatz via ELFtools hinzugefügt

 - Speicherorder (little Endian) immer beachten!
 
 -------------------------------------
 ## Task 03: ByteOrder/Datendarstellung ~abgeschlossen
 ### Theorie Aspekte
 - wie man Bytes interpretiert in Python (Binary mit verschiedenen "Typen" drinne zum parsen)

 - Big Endian vs. little Endian, signed vs unsigned etc. 

 ### Anmerkungen
 - nicht verwirren lassen von System Architektur! (oder interner Darstellung z.B. in C/C++)
 
 -------------------------------------
 ## Task 04: Seccomp/Linux Proc Hierarchie ~abgeschlossen
 ### Theorie Aspekte
 - Linux Kernel Seccomp Theorie + auslesen welche Prozesse das nutzen

 - Seccomp (Secure Computing Mode) ist ein Modus im Linux Kernel, sodass ein Prozess nur eingeschränkt Syscalls nutzen kann (nur exit, read, write). 
 Andere Syscalls werden blockiert/der Prozess wird terminiert

 - /proc hat alle Prozesse via Pid die gerade laufen als Ordner. 
 Im Ordner gibt es die Status Flag, wo steht wie genau der Prozess läuft (auch ob seccomp an ist)

 ### Anmerkungen
 - basic Linux File Structure sollte verstanden sein
 
 -------------------------------------
 ## Task 05: C Basics ~abgeschlossen
 ### Theorie Aspekte
 - C Programm Basics (Stack, Heap, Pointer, Methoden) + fixen von denen

 - Funktionspointer sehr wichtig! Konzept verstehen!

 ### Anmerkungen
 - Compiler Befehle könnten nicht wichtig sein, ist aber basic
 
 -------------------------------------
 ## Task 06: Key Reverse Engineering I ~abgeschlossen
 ### Theorie Aspekte
 - Binärdatei reverse Engineering, Basics von Ghidra/GDB; am Beispiel eines Keys für eine Binary

 - Ghidra sollten die Basics sitzen (Typenänderung, wo/wie anfangen etc.)

 - gdb/pwndbg deutlich schwerer, Assembler Code lesen können!

 ### Anmerkungen
 - war nicht gestrippt, d.h. alle Zeichen waren noch in Takt, jedoch geht es auch schwerer!

 - Breakpoints/disass super wichtig mit gdb
 
 -------------------------------------
 ## Task 07: Runtime Reverse Engineering II ~abgeschlossen
 ### Theorie Aspekte
 - Flag aus einer Binary klauen der "nur zu runtime" existiert

 - Gdb Scripte verstehen (integriertes Pythonmodul)

 - Stack/Heap + alle wichtigen Assembler Befehle verstehen

 - Calling Conventions (System V vs cdecl je nach Architektur)
 ### Anmerkungen
 - Gdb Scripte sind doof, aber die Aufgabe ist noch O.k.

 - hab die Aufgabe mit Kommentaren nochmal hinzugefügt (Logik der Aufgabe)
 
 -------------------------------------
 ## Task 08: ELF Header Part 3 ~abgeschlossen
 ### Theorie Aspekte
 - ELF Header Theorie gut verstehen!
 
 - Flags von den einzelnen Headern verstehen (einer hatte falsche Flags, sollte man selbst herrausfinden)

 ### Anmerkungen
 - immernoch readelf sehr wichtig! 
 
 -------------------------------------
 ## Task 09: TO DO
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 10: Unicorn CPU Emulator ~abgeschlossen
 ### Theorie Aspekte
 - CPU Emulator Fixen (gab paar Probleme beim emulieren)

 - Es gab keinen Stack

 - Der Adressbereich war zu klein (Adresse vom Stack war out of range)

 - ESP wurde Gesetz + der Inhalt an der Adresse auch

 ### Anmerkungen
 - relativ uninteressant für die Vorlesung

 - Assembler Code lesen/Register/Stack jedoch verstehen

 - gleiches gilt für Sections aus ELF!
 
 -------------------------------------
 ## Task 11
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 12
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 13
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 14
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 15
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 16
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 17
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 18
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 19
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 20
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 21
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 22
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 23
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 24
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 25
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 26
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 27
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 28
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 29
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 30
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
