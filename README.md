
The Madman Mad Lib Generator
============================

Replace words in a sentence with words chosen from a Markov chain generated from
your favorite source material. Or, in non-technical terms, automatic Mad Libs!

Provide a source file of thousands of words of text; Madman will use this as
inspiration when choosing its Mad Libs.

Requires NLTK.

Usage
-----

1. Install [NLTK](http://www.nltk.org/) for your Python version.
2. Install the `wordnet`, `maxent_treebank_pos_tagger`, and `punkt` datasets for
NLTK, using `nltk.download`. (That is, run the Python CLI, `import nltk`, and
then run `nltk.download()` and select the datasets.)
3. Place your favorite source material in `sources/` as plain text files, named
in the format `sourcename-raw.txt`. Large files (50,000 words or more) are good.
4. Use the `sources/format.pl` script to turn the files into
one-sentence-per-line files (e.g `./format.pl sourcename`).
5. Run `python makeChains.py sourcename` to build the Markov chain.

Now you're ready to make some mad libs. You can do this two ways: interactively
in Python, or at the command line.

For interactive mode, just run `python` or `ipython` in this directory, and then
just use

    import madman
    m = madman.Madman("sourcename")
    m.madlib("Your text goes here.") # Only one sentence at a time
    
Alternately, to madlibify an entire text file in one shot, just run

    python madfile.py yourfile.txt

Each sentence will be printed with strategic mad lib replacements.

Enjoy.
