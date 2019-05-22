#!/usr/bin/perl -l
open IN, "README.md" or die $!;
while (<IN>) {
    print $1 if /\((.*\.md)\)/;
}
