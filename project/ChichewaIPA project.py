#IPA converter for Chichewa language
#References: The phonology of Chichewa (2017), Laura J.Downing and Al Mtenje

import re





# exceptions dictionary for unclassified words depending on:
chichewaExceptionsDIA = [u"mkango", u"m̩tsiinje", u"tsiiku", u"tsaamba", u"dzuulo", u"dzaana"
                         u"dziina", u"tsopaano", u"tsooka", u"citseeko", u"matsooka"]                                           # the dialect 
chichewaExceptionsCL = [u"m'bale", u"m'phunzitsi", u"anáḿpatsa", ]                                                              # the noun classes
chichewaExceptionsVAR = [u"zyolika"]                                                                                            # free variation between speakers
exceptionsD = []
exceptionsCL = []
exceptionsVAR = []





# vowels dictionary / no exceptions
IPAvowels = {'a': 'a',
             'i': 'i',
             'o': 'ɔ',
             'e': 'ɜ',
             'u': 'u'}

# consonants dictionary / no exceptions
IPAconsonants = {'b': 'ɓ',  # voiced
                 'bw': 'ɓʷ',
                 'bz': 'bzʲ',
                 'd': 'ɗ',
                 'dw': 'ɗʷ',
                 'dy': 'ɗʲ',
                 'g': 'g',
                 'gw': 'gʷ',
                 'j': 'd͡ʒ',
                 'v': 'v',
                 'vw': 'vʷ',
                 'vy': 'vʲ',
                 'z': 'z',
                 'zy': 'zʲ',
                 'dz': 'd͡z',
                 'dzw': 'd͡zʷ',
                 'p': 'p',  # plain
                 'pw': 'pʷ',
                 'py': 'pʲ',
                 't': 't',
                 'tw': 'tʷ',
                 'ty': 'tʲ',
                 'k': 'k',
                 'kw': 'kʷ',
                 'ch': 't͡ʃ',
                 'ph': 'pʰ',  # aspirated
                 'phw': 'pʷʰ',
                 'ps': 'psʲ',
                 'th': 'tʰ',
                 'thw': 'tʷʰ',
                 'thy': 'tʲʰ',
                 'kh': 'kʰ',
                 'khw': 'kʷʰ',
                 'tch': 't͡ʃʰ',
                 'f': 'f',
                 'fw': 'fʷ',
                 'fy': 'fʲ',
                 's': 's',
                 'sw': 'sʷ',
                 'sh': 'ʃ',
                 'ts': 't͡s',
                 'tsw': 't͡sʷ',
                 'mb': 'ᵐb',  # nasalised voiced
                 'mbw': 'ᵐbʷ',
                 'mbz': 'ᵐbzʲ',
                 'nd': 'ⁿd',
                 'ndw': 'ⁿdʷ',
                 'ndy': 'ⁿdʲ',
                 'ng': 'ᵑg',
                 'ngw': 'ᵑgʷ',
                 'nj': 'ⁿd͡ʒ',
                 'mv': 'ᶬv',
                 'nz': 'ⁿz',
                 'nzw': 'ⁿzʷ',
                 'ndz': 'ⁿd͡z',
                 'mph': 'ᵐpʰ',  # nasalised aspirated
                 'mphw': 'ᵐpʷʰ',
                 'mps': 'ᵐpsʲ',
                 'nth': 'ⁿtʰ',
                 'nthw': 'ⁿtʷʰ',
                 'nthy': 'ⁿtʲʰ',
                 'nkh': 'ᵑkʰ',
                 'nkhw': 'ᵑkʷʰ',
                 'ntch': 'ⁿt͡ʃʰ',
                 'mf': 'ᶬf',
                 'ns': 'ⁿs',
                 'nsw': 'ⁿsʷ',
                 'm': 'm',  # nasal
                 'mw': 'mʷ',
                 'my': 'mʲ',
                 'n': 'n',
                 'ng^': 'ŋ',
                 'ng^w': 'ŋʷ',
                 'ny': 'ɲ',
                 'ŵ': 'w⁽ᵝ',  # liquid
                 'w': 'w',
                 'l': 'ɽ',
                 'r': 'ɽ',
                 'w': 'ɽʷ',
                 'rw': 'ɽʷ',
                 'h': 'h',
                 'y': 'j'}

orthography = input('Enter a chichewa text for IPA transliteration: ')
split = orthography.split()

for c in split:
    if c in chichewaExceptionsDIA:
        exceptionsD.append(c)
for c in split:
    if c in chichewaExceptionsCL:
        exceptionsCL.append(c)
for c in split:
    if c in chichewaExceptionsVAR:
        exceptionsVAR.append(c)
        
        
        


def getTrans(orthography):
    trans = ''
    snip = ''
    vowels = False
    snips = []
    for letter in orthography:
        if letter.lower() in IPAvowels:
            if not vowels:
                snips.append(snip)
                snip = letter.lower()
                vowels = True
            else:
                snip += letter
        else:
            if vowels:
                snips.append(snip)
                snip = letter.lower()
                vowels = False
            else:
                snip += letter
    snips.append(snip)

    for frame in snips:
        trans += tranSnips(frame)
    return trans


def tranSnips(snip):
    trans = ''
    toTranslate = snip
    lenofsnip = len(snip)
    while lenofsnip > 0 and len(toTranslate) > 0:
        if snip[len(trans):lenofsnip] in IPAconsonants:
            trans += IPAconsonants[snip[len(trans):lenofsnip]]
            toTranslate = toTranslate[len(trans):]
            lenofsnip = len(snip)
        else:
            lenofsnip -= 1
    if len(trans) > 0:
        return trans
    else:
        return snip





print('IPA transliteration: ', getTrans(orthography))
print('\n')
if len(exceptionsD) != 0: 
    print('Care! The following words might have the wrong transliteration: specify the dialect and look up in the grammar: ', exceptionsD)
    print('\n')

if len(exceptionsCL) != 0:
    print('Care! The following words might have the wrong transliteration: specify the noun classes of the words and look up in the grammar: ', exceptionsCL)
    print('\n')

if len(exceptionsVAR) != 0:
    print("Care! The following words might have the wrong transliteration: these words are pronounced differently depending on the speaker's idiolect: ", exceptionsVAR)

if len(exceptionsD) == 0 and len(exceptionsCL) == 0 and len(exceptionsVAR) == 0:
    print('No exceptions! This is most likely a correct transliteration.')

