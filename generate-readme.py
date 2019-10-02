from os import scandir

readme = open('./Readme.md', 'w+')
readme.write("""# Kattis Grind

A repo of solved Kattis problems. Uses [Kattis-Grind-Setup](https://github.com/JarateKing/Kattis-Grind-Setup).

## Usage

To create a new problem, run `new-problem.bat` on Windows, or `newprob.sh` on UNIX, and type the problem id on open Kattis.

The source file for the problem is given as `prog.cpp` by default; it includes <bits/stdc++.h> and a main function skeleton.

To run compile and run a problem, run `run.bat` on Windows, or `run.sh` on UNIX, inside the problem folder.

To open a link to the problem online, run `kattis.bat` on Windows, or open `link.html` on UNIX, inside the problem folder.

## Requirements

* [GCC](https://gcc.gnu.org/) / [MinGW](http://mingw.org/) 

### UNIX Requirements
* bash
* zip
* curl
* diff

## UNIX Configuration Notes

It is recommended to use the included GCC_ARGS since they are [the args Kattis uses](https://open.kattis.com/help/cpp).

You must change the GCC_PATH to a valid G++ compiler binary path, or an equivalent alias; eg. `GCC_PATH='g++'` or `GCC_PATH='/usr/bin/g++'`

Be careful when using an alias with arguments, because the GCC_ARGS variable will also be used; set them to empty string if you do not want them.

### macOS Configuration

It is recommended that you install [homebrew](https://brew.sh/) and use it to install gcc. This is so that you can use GNU extensions, `#include <bits/stdc++.h>`, and it is closer to Kattis' environment.

You must then set GCC_PATH to `/usr/local/bin/g++-9` or equivalent.

## Resources

* [Kattis Help Page](https://open.kattis.com/help)

Development:
* [Online C++ Compiler](https://www.onlinegdb.com/online_c++_compiler)
* http://quick-bench.com
* https://godbolt.org/

Reference:
* [JarateKings's Competitive Programming Code Snippets](https://github.com/JarateKing/Competitive-Programming-Snippets)
* https://cpbook.net/
* https://cp-algorithms.com/
* https://www.geeksforgeeks.org/how-to-begin-with-competitive-programming/
* https://www.codechef.com/wiki/contest-editorial

""")
problems = ''
for dirpath in scandir('./problems/'):
	if dirpath.is_dir():
		problemName = dirpath.name
		problemFile = 'problems/' + dirpath.name + '/prog.cpp'
		problemLink = 'https://open.kattis.com/problems/' + problemName
		problems = problems + '* [![:link:](https://open.kattis.com/favicon)](' + problemLink + ') [' + problemName + '](' + problemFile + ')\n'
		
if (problems is not ''):
	readme.write('## Solutions\n\n')
	readme.write(problems)

readme.close()