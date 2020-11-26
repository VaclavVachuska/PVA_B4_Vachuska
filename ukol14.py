#!/usr/bin/python3
Nula = ["  ***  ",
        " *   * ",
        "*   * *",
        "*  *  *",
        "* *   *",
        " *   * ",
        "  ***  "]
Jedna =["   *   ",
        "  **   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "  ***  "]
Dva =  ["  ***  ",
        " *   * ",
        "     * ",
        "   *   ",
        "  *    ",
        " *     ",
        " ***** "]
Tri  = ["  ***  ",
        " *   * ",
        "     * ",
        "   *   ",
        "     * ",
        " *   * ",
        "  ***  "]
Ctyri =["   *   ",
        "  **   ",
        " * *   ",
        "*  *   ",
        "****** ",
        "   *   ",
        "   *   "]
Pet  = [" ***** ",
        " *     ",
        " ***   ",
        "     * ",
        "      *",
        "*    * ",
        "  ***  "]
Sest = ["    *  ",
        "   *   ",
        "  *    ",
        "  ***  ",
        " *   * ",
        " *   * ",
        "  ***  "]
Sedm = [" ***** ",
        "     * ",
        "    *  ",
        "   *   ",
        "  *    ",
        " *     ",
        " *     "]
Osm  = ["  ***  ",
        " *   * ",
        " *   * ",
        "  ***  ",
        " *   * ",
        " *   * ",
        "  ***  "]
Devet= ["  ***  ",
        " *   * ",
        " *   * ",
        "  ***  ",
        "     * ",
        "     * ",
        "  **   "]
Cislice = [Nula, Jedna, Dva, Tri, Ctyri, Pet, Sest, Sedm, Osm, Devet]
while True:
    try:
        cislo = input("zadejte cislo: ")
        for radka in range(0,7):
            for pozice in range(0,len(cislo)):
                x = Cislice[int(cislo[pozice])][radka]
                print(x.replace("*",cislo[pozice]), end=" ")
            print("")
    except ValueError as err:
        print(err, "Neni cislo") 
        cisla=""
    except EOFError:
        break
