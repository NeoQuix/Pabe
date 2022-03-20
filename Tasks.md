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
 ## Task 09: Binaries/ELF Files .text ~abgeschlossen
 ### Theorie Aspekte
 - ProgrammCode in der Binary fixen 

 - disassemble _start für den Code (und dort sieht man einen write syscall + exit syscall) ==> man weiß was man überschreiben muss

 - mit readelf -e kann man den Offset für die .text Section finden ==> dort rein schreiben

 ### Anmerkungen
 - hier war die syscall nummer + size falsch im ersten block + syscall selbst wurde nicht aufgerufen (int 0x80)

 - aufpassen bei Offsets im schreiben

 - mit Elftools deutlich cleaner möglich aber KA WEIL KEINE DOKUMENTATION!!!!
 
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
 ## Task 11: Key Reverse Engineering II ~abgeschlossen 
 ### Theorie Aspekte
 - nun mit dem modul z3 den key herausfinden 

 - Bedingungen relativ leicht mit Ghidra/gdb erkennbar 


 ### Anmerkungen
 - wieder bissel Logik + Assembler 
 
 -------------------------------------
 ## Task 12: Funktions Tracer mit GDB Scripten implementieren ~abgeschlossen
 ### Theorie Aspekte
 - Funktionen Tracen (Ablauf)
 
 - relativ leicht mit rbreak

 ### Anmerkungen
 - GDB Scripte nicht sooo wichtig, aber wissen wie die funktionieren!
 
 -------------------------------------
 ## Task 13: Programm Analysis I ~abgeschlossen(!) 
 ### Theorie Aspekte
 - Programm welches einen Flag mit einer Signal Method printet (SEGFault)

 - Overflow wird ausgelöst durch strcpy welches ab 16 Bytes einen Overflow macht und RBP zerstört (oder auch return danach)

 ### Anmerkungen
 - File war stripped, d.h. keine Symbole! 

 - ==> entry Point nutzen aus readelf -h

 - stripped Binaries nochmal angucken!
 
 -------------------------------------
 ## Task 14 TO DO
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 15 Runtime Reverse Engineering III ~abgeschlossen
 ### Theorie Aspekte
 - wieder ein Flag der nur in runtime existiert, jedoch deutlich schwerer zu extrahieren ist 

 - muss man via gdb script machen, welches mit watchpoints die Register ausliest

 - in eax ist immer das erg von der i-ten Iteration wenn ecx == counter ist (zählt von 0x15 bis 0x0 runter)

 ### Anmerkungen
 - fixed script damit es lesbarer ist (loop statt 200 Zeilen)
 
 -------------------------------------
 ## Task 16 Buffer Overflow I ~abgeschlossen
 ### Theorie Aspekte
 - Programm mit Bufferoverflow + Methode die unseren Flag ausprintet 

 - alle Sicherheitsmechanismen waren aus, d.h. einfach in saved rip (from call) die Adresse von der Methode reinschreiben die den Flag ausprintet

 ### Anmerkungen
 - Stack Verständnis ist wichtig
 
 -------------------------------------
 ## Task 17 Buffer overflow II ~abgeschlossen
 ### Theorie Aspekte
 - Programm mit Bufferoverflow und Stack Adresse leak

 - alle Sicherheitsmechanismen waren aus, d.h. einfach den Stack missbrauchen da er executable ist 

 - d.h. rip springt zurück auf den Stack, landet in Nope Slede, landet in Shellcode der execve ausführt und das Flag printet

 ### Anmerkungen
 - Stack Verständnis wieder wichtig

 - Nur möglich, da der Stack exe ist (NX Bit ist aus) + weil wir eine Adresse vom ASLR haben!
 
 -------------------------------------
 ## Task 18 Ret2LibC ~TO DO
 ### Theorie Aspekte
 - non exec Stack, geleakte Adressen + Bufferoverflow
 ==> ret2libc, d.h. base von libc berechnen, system/bin/sh offset kriegen ==> ret vom stack auf system setzen (und halt bin/sh als argument dadrüber nach cdecl!)


 ### Anmerkungen
 - ASLR, NX, Stack + pwntools (weil es alles DEUTLICH leichter macht!)
 
 -------------------------------------
 ## Task 19 Buffer Overflow III ~abgeschlossen (Nochmal machen!)
 ### Theorie Aspekte
 - Programm hatte alle Sicherheitsvorkehrungen an + halt Bufferoverflow via read (ließt bis '\0')

 - d.h. man musste 1 den Canary brute forcen (da wir in einer Loop waren konnten wir den Byte für Byte holen)

 - danach brauchte man eine Adresse die im gleichen Bereich liegt wie givemeashellplz (z.B. start/main)

 - mit denen kann man den relativen Offset berechnen aus readelf -s 

 - ==> damit kann man den return call überschreiben, sodass das Programm zu givemeashellplz zurückkehrt 

 ### Anmerkungen
 - sehr viel Theorie in der Aufgabe (auch relativ schwer!)

 - Calling Conventions MÜSSEN NICHT EINGEHALTEN WERDEN! (z.B. für Stack alignment etc)

 - Stack Canaries, NX, ASLR, PIE verstehen
 
 -------------------------------------
 ## Task 20 ASLR/Canariy Brutefoce ~abgeschlossen (angucken)
 ### Theorie Aspekte
 - Forking Server der pro Verbindung sich klont und diese bearbeitet

 - durchs forken wird der canary/aslr offset übernommen

 - ==> wenn der Canary gebruteforced ist wissen wir eine Adresse 
 
 - den relativen offset zu givemeashellplz wissen wir ==> müssen nur die ersten 4 Byte von ASLR bruteforcen

 ### Anmerkungen
 - sind nur 16 Kombinationen für ASLR Force

 - sind 256 (2^8) * 8 viele Kombinationen für den Canary 

 - relativ leichte Aufgabe wenn man die Theorie gerafft hat 
 
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
