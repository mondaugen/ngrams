extract_ngram_freq.py Will just sort the ngrams by the product of their
frequency and their length with the idea that we want to prefer longer ngrams.

sort_normalized_frequency.py Preprocesses the ngrams by subtracting all the
occurrences of the contained ngrams in the longer words from the total number of
occurrences of the corresponding ngrams. This is done with the idea that what we
really want to write is the longest string we need, not its containing ngrams,
so we find out how many times we wrote that ngram as part of a larger ngram, and
subtract those occurrences.
This is sort of flawed because an ngram could be penalized by a relatively
infrequent longer ngram that contains the ngram many times.
run with
pcregrep -v [0-9]-gram ngrams1.tsv| python3 ~/Documents/study/ngrams/sort_normalized_frequency.py 
and the like

plot_2gram_freq.py attempts to see what letters almost always occur in pairs.
The idea is that the flatter the probability distribution of observing the letter-pair makes this letter a candidate for being alone on the keyboard. E.g., e combines with so many letters that it be best given its own key. On the other hand some letters mostly occur paired with others. In that case, it should be easy to type these pairs of letters but not the letter with an infrequent partner.

To get the ngrams full ngrams data, download from 
https://drive.google.com/file/d/1hhgNIgk-IQa3s4xRZ1SMWC5WPL8S5Vnt/view?usp=sharing
