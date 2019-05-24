#!/usr/bin/perl
open IN, "chapters.md" or die $!;
mkdir "_data" unless -d "_data";
open OUT, ">_data/navigation.yml";
my $level;
print OUT "chapters:\n";
while (<IN>) {
  chomp;
  s/^(\s*)\*\s*// or die "Can't parse: {{$_}}";
  $level = length($1) + 2;
  print OUT ("  " x $level);
  if (/\[([^\]]+)\]\(([^\)]+).md\)/) {
    my ($title, $link) = ($1, $2);
    print OUT ("- title: \"$title\"\n");
    print OUT ("  " x $level);
    print OUT ("  url: \"$link\"\n");
  } else {
    print OUT ("- title: \"$_\"\n");
    print OUT ("  " x $level);
    print OUT ("  children:\n");
  }
}
