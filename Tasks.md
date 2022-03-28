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
 ## Task 14 Programm Analysis II mit HTML ~abgeschlossen 
 ### Theorie Aspekte
 - ruft Domain aus einer File aus, parst HTML Erg. und nimmt den Titel davon

 - den Titel verschlüsselt er Byteweise ==> Erg ist der String davon

 - man musste nun die selben Funktionen in python reimplementieren (d.h. die ifs/while übersetzen, damit dasselbe rauskommt)

 ### Anmerkungen
 - typischer Ablauf bei der Analyse mit Ghidra/GDB (Schritt für Schritt die Funktionen)

 - auch wieder großer Teil Reverse Engineering!
 
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
 ## Task 18 Ret2LibC ~NICHT gemacht (Theorie schon)
 ### Theorie Aspekte
 - non exec Stack, geleakte Adressen + Bufferoverflow
 ==> ret2libc, d.h. base von libc berechnen, system, /bin/sh offset kriegen ==> ret vom stack auf system setzen (und halt bin/sh als argument darüber nach cdecl!)

 - Wichtig: Pointer! d.h. die Adresse von /bin/sh übergeben und nehmen


 ### Anmerkungen
 - ASLR, NX, Stack + pwntools (weil es alles DEUTLICH leichter macht!)
 
 -------------------------------------
 ## Task 19 Buffer Overflow III ~abgeschlossen
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
 ## Task 20 ASLR/Canariy Brutefoce ~abgeschlossen
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
 ## Task 21 Heap Buffer Overflow ~abgeschlossen
 ### Theorie Aspekte
 - Heap Buffer Overflows (kein Metadata Overflow)

 - Adresse von puts liegt auf dem Heap ==> diese leaken + durch system ersetzen

 - Heap Layout:

 - simple Note (eig. 60 Bytes) ___ printable Note (72 Bytes); Abstand zu puts von printable Note sind 143 Bytes

 - Leak via read

 - mit puts@got kann man die libc base berechnen ==> system + /bin/sh

 - /bin/sh landet in rdi durch den call von puts mit dem Inhalt der Note! 

 ### Anmerkungen
 - Heap Layout wichtig; Offsets wichtig; Wachstumsrichtung!

 - Kein Rop nötig weil puts mit argument was wir bestimmen aufgerufen wird

 - Abstand ermittelt durch Overflow (kann man aber auch berechnen mit den Infos von malloc (60 + 8 + 60 + 8 + 8 (-1 weil ja immer newline mit geschickt wird))
 
 - generell sehr schöne Heap Aufgabe, Overflow bissel schwerer zu finden

 -------------------------------------
 ## Task 22 Heap Visualization ~abgeschlossen (nicht programmiert)
 ### Theorie Aspekte
 - man sollte besser verstehen wie die Mainarena, bins (fastbins, tcachebins, smallbins, largebins funktionieren) und wie man sie parsen kann

 - parsen glaube ich wird nicht in der Klausur dran kommen, dennoch einzelne Elemente Interessant!

 - gdb scripte sind sooo Müll!

 ### Anmerkungen
 - wissen wie die alle aufgebaut sind + unterschiede 

 - tcachebins auch!

 - relativ viel Pointer gespiele; unlink Exploit damit auch besser verstehen!
 
 -------------------------------------
 ## Task 23: ROP ~ abgeschlossen (jaein)
 ### Theorie Aspekte
 - mittels ROP aus einer Binary die andere aufrufen 

 1. Programm Base berechnen ==> mittels puts main oder _start vom Stack leaken
 ==> Base Offset für Main

 2. Danach erste rop die puts aufruft mit der Adresse von puts@got als Parameter + danach das Programm neu starten indem man main aufruft (bzw. dahin returnt)
 ==> leaked puts adresse ==> libc base damit berechnenbar 

 3. Nun kann man die komplette ROP Chain machen (d.h. die Parameter erstellen + halt den Aufruf der Binary)
 ==> bisschen anstregend manuell, aber machbar!

 - hab die letzte Rop Chain nicht mehr gemacht, da die sehr ähnlich zum beispiel aus der Vorlesung ist und mehr tüfteln als wichtige Theorie

 ### Anmerkungen
 - readelf + offsets + aslr verstehen

 - Segment/lib Mapping von ASLR verstehen

 - Pwn Rop verstehen (ultra hexerei des Todes)

 - Idee von ROP verstehen (ULTRA GEILE IDEE)
 
 -------------------------------------
 ## Task 24 Advanced Shellcode Crafting + ROP ~TODO
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 25 C++ vTables ~ TODO
 ### Theorie Aspekte
 - x

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Task 26 Format String GOT Override ~ TODO
 ### Theorie Aspekte
 - standard format string exploit 
 
 - man musste den Offset finden wo der String selbst auf dem Stack ist 

 - Libc Base leaken mit einer Adresse auf dem Stack (init z.B.)

 - dann schreibt man die Adresse von puts@got am Anfang (write where) und muss die adresse von System 2 Byte weise reinschreiben (What)

 - als letztes muss man "/bin/sh" in den formatstring schreiben und ist fertig (wenn puts aufgerufen wird)

 ### Anmerkungen
 - Offset relativ schwer berechenbar (gdb + Little Endian etc.)

 - Formatstring struktur verstehen
 
 -------------------------------------
 ## Task 27 Format String + ROP ~abgeschlossen
 ### Theorie Aspekte
 - Zwei Bugs sind: Format String via argv[1] + stack buffer overflow via gets

 - 1. Leak Stack Canary + Libc base via Format String (%p)
    
 - 2. gets Overflow Canary + dann ret für ROP

 - 3. ROP macht dann einfach einen execve("/bin/sh")
    ==> /bin/sh muss dabei in rw bereich von libc geschrieben werden! 
    ==> entweder offset für Datenstrukturen oder die Base!

 ### Anmerkungen
 - 64 Bit Calling Convention beachten! ==> erste 6 Leaks sind Register ==> Offset für Stack immer + 6 rechnen! (also für format string)

 - Exe main NICHT nötig, da wir nur von libc rop machen!

 - Außerdem: call funktioniert nur mit base ==> müssen es manuell machen, also r.find_gadget()
 
 -------------------------------------
 ## Task 28 UAF (+ Format String Exploit) ~abgeschlossen
 ### Theorie Aspekte
 - man musste den "Dangeling Pointer" + UAF erkennen

 - heap fengshui war NICHT nötig, aber theoretisch wichtig
 ==> Befehle so nutzen, dass user auf der selben Stelle allokiert wird wie der alte Printer und der Dangeling Pointer drauf zeigt (waren fastbins also LIFO)

 - Formatstring exploit um libc base zu leaken

 - genauen Ablauf siehe task28

 ### Anmerkungen
 - formatstring hier nur für Leak wichtig; Fokus eher auf Heap + UAF
 
 -------------------------------------
 ## Task 29 TCache poisoning ~ Theorie gemacht!
 ### Theorie Aspekte
 - Tcache Poisoning + minimales Heap Fengshui

 - Erst mal Adressen leaken von libc + Binary (binary kriegt man geschenkt von der ATM backdoor func.)

 - Allokation in Fastbin schicken + UAF nutzen um *next zu überschreiben auf free@got 

 - später dann den Chunk zurück holen + bei free@got die adresse von atm_backdoor reinschreiben
    ==> bei nächstem free wird atm_backdoor aufgerufen was wiederum system aufruft

 - dann später free aufrufen (wichtig parameter von free muss "/bin/sh" sein!)

 ### Anmerkungen
 - Heap/Bins verständniss, LIFO Structure, Fastbins etc. 

 - sonst sehr nah am Beispiel in den Folien!
 
 -------------------------------------
 ## Task 30 Heap Feng Shui + UAF + TCache ~ KEINE ZEIT, Theorie halbwegs ok, relativ komplex ==> für Klausur zu komplex
 ### Theorie Aspekte
 - Libc Leak via panic ==> Overflow bei scanf mit einem Byte (8 byte buffer, man holt sich 8, darf aber nur 7 + 1 machen!; panic liegt dahinter)

 - 

 ### Anmerkungen
 - y
 
 -------------------------------------
 ## Pwn Tools Notes 
 ### Anmerkungen
 - kann seeeehhhrrrr vieles leichter machen

 - libcbase wird automatisch berechnet (ka. wie; aber tut es; trotzdem wissen wie es geht); d.h. ASLR wird damit geknackt 

 - exebase kann es nicht ausrechnen? 
 
 -------------------------------------

 ## Sicherheitsmechanismen 
 ### ASLR ~ Address Space Layout Randomization
 - 

 ### PIE ~ Position Independent Executeable
 - 

 ### RELRO ~ Relocation Read Only
 - 
 
 ### Canaries ~ Stack Canaries
 - 

 ### ASAN ~ Adress Sanatizer
 - 
 -------------------------------------