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
* zip
* curl

## Resources

Development:
* https://www.onlinegdb.com/online_c++_compiler
* http://quick-bench.com
* https://godbolt.org/

Reference:
* https://github.com/JarateKing/Competitive-Programming-Snippets
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