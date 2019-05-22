#!/usr/bin/perl -l
open IN, "chapters.md" or die $!;
while (<IN>) {
    print $1 if /\((.*\.md)\)/;
}
