# preARCkmerFinder
creates the subtracted filtered meryl database necessary for ARCkmerFinder

To run this, you must have genomescope 2.0 installed since there are
some R libraries that are part of it.

module load R/4.4.0-openblas-rocky8
Get it here:

https://github.com/tbenavi1/genomescope2.0

It will install some packages in your
~/R/x86_64-pc-linux-gnu-library/4.4 directory.  In particular there
will be a directory genomescope.  Find a file named DESCRIPTION and change the package name from genomescope to genomescope2 and then installation can proceed.

Package: genomescope2
Title: Reference-free profiling of genomes
Version: 2.1.0
Authors@R: person("Timothy", "Ranallo-Benavidez", email = "tbenavi1@jhu.edu",
                  role = c("aut", "cre"))
Description: GenomeScope analyzes the k-mer histogram to output estimates for genome size, heterozygosity, and repetitiveness, without requiring a reference genome. GenomeScope employs a polyploid-aware mixture model that, within seconds, accurately infers genome properties from unassembled sequencing data. GenomeScope produces a report and several informative plots describing the genome properties.
Depends: R (>= 3.1.0)
Imports: argparse, jsonlite, minpack.lm
License: file LICENSE
LazyData: true
RoxygenNote: 6.1.1
Encoding: UTF-8


