"""
Comprehensive database of coarticulation examples for American English.
Contains realistic phrases showing consonant coarticulation in natural speech contexts.
"""

# Dictionary mapping (sound1, sound2) to list of (phrase, IPA transcription) tuples
COARTICULATION_EXAMPLES = {
    # Examples with 'nst' cluster (from user's example)
    ('nst', 'ð'): [
        ('against the sky', '/əˈɡɛns̪t̪̚ ð̪ə ˈskʰaɪ/'),
        ('against the wall', '/əˈɡɛns̪t̪̚ ð̪ə ˈwɔl/'),
    ],
    ('nst', 'k'): [
        ('against cold winds', '/əˈɡɛns̪t̪ kʰoʊld ˈwɪndz/'),
        ('amongst killers', '/əˈmʌŋs̪t̪ ˈkʰɪləɹz/'),
    ],
    ('nst', 'w'): [
        ('against wishes', '/əˈɡɛns̪t̪ ˈwɪʃɪz/'),
        ('against winter', '/əˈɡɛns̪t̪ ˈwɪntəɹ/'),
    ],
    ('nst', 'p'): [
        ('against protocol', '/əˈɡɛns̪t̪ ˈpʰɹoʊtəkɔl/'),
        ('against plans', '/əˈɡɛns̪t̪ ˈpʰlænz/'),
    ],
    ('nst', 'b'): [
        ('against better judgment', '/əˈɡɛns̪t̪ ˈbɛtəɹ ˈdʒʌdʒmənt/'),
        ('against belief', '/əˈɡɛns̪t̪ bəˈlif/'),
    ],
    ('nst', 't'): [
        ('against time', '/əˈɡɛns̪t̪ ˈtʰaɪm/'),
        ('against terrible odds', '/əˈɡɛns̪t̪ ˈtʰɛɹəbəl ˈɑdz/'),
    ],
    ('nst', 'd'): [
        ('against darkness', '/əˈɡɛns̪t̪ ˈdɑɹknəs/'),
        ('against defeat', '/əˈɡɛns̪t̪ dɪˈfit/'),
    ],
    ('nst', 'g'): [
        ('against great odds', '/əˈɡɛns̪t̪ ˈɡɹeɪt ˈɑdz/'),
        ('amongst giants', '/əˈmʌŋs̪t̪ ˈdʒaɪənts/'),
    ],
    ('nst', 'f'): [
        ('against family', '/əˈɡɛns̪t̪ ˈfæməli/'),
        ('against forces', '/əˈɡɛns̪t̪ ˈfoɹsɪz/'),
    ],
    ('nst', 'v'): [
        ('against violence', '/əˈɡɛns̪t̪ ˈvaɪələns/'),
        ('against various threats', '/əˈɡɛns̪t̪ ˈvɛɹiəs ˈθɹɛts/'),
    ],
    ('nst', 'θ'): [
        ('against thinking', '/əˈɡɛns̪t̪ ˈθɪŋkɪŋ/'),
        ('against theft', '/əˈɡɛns̪t̪ ˈθɛft/'),
    ],
    ('nst', 's'): [
        ('against science', '/əˈɡɛns̪t̪ ˈsaɪəns/'),
        ('against society', '/əˈɡɛns̪t̪ səˈsaɪəti/'),
    ],
    ('nst', 'z'): [
        ('against zealots', '/əˈɡɛns̪t̪ ˈzɛləts/'),
        ('against zoning laws', '/əˈɡɛns̪t̪ ˈzoʊnɪŋ lɔz/'),
    ],
    ('nst', 'ʃ'): [
        ('against shipping', '/əˈɡɛns̪t̪ ˈʃɪpɪŋ/'),
        ('against shame', '/əˈɡɛns̪t̪ ˈʃeɪm/'),
    ],
    ('nst', 'h'): [
        ('against hate', '/əˈɡɛns̪t̪ ˈheɪt/'),
        ('against history', '/əˈɡɛns̪t̪ ˈhɪstəɹi/'),
    ],
    ('nst', 'tʃ'): [
        ('against change', '/əˈɡɛns̪t̪ ˈtʃeɪndʒ/'),
        ('against children', '/əˈɡɛns̪t̪ ˈtʃɪldɹən/'),
    ],
    ('nst', 'dʒ'): [
        ('against justice', '/əˈɡɛns̪t̪ ˈdʒʌstɪs/'),
        ('against judgment', '/əˈɡɛns̪t̪ ˈdʒʌdʒmənt/'),
    ],
    ('nst', 'm'): [
        ('against my will', '/əˈɡɛns̪t̪ maɪ ˈwɪl/'),
        ('against modern values', '/əˈɡɛns̪t̪ ˈmɑdəɹn ˈvæljuz/'),
    ],
    ('nst', 'n'): [
        ('against nature', '/əˈɡɛns̪t̪ ˈneɪtʃəɹ/'),
        ('against new ideas', '/əˈɡɛns̪t̪ ˈnu aɪˈdiəz/'),
    ],
    ('nst', 'l'): [
        ('against logic', '/əˈɡɛns̪t̪ ˈlɑdʒɪk/'),
        ('against law', '/əˈɡɛns̪t̪ ˈlɔ/'),
    ],
    ('nst', 'r'): [
        ('against reason', '/əˈɡɛns̪t̪ ˈɹizən/'),
        ('against reality', '/əˈɡɛns̪t̪ ɹiˈæləti/'),
    ],

    # Stop + stop coarticulations
    ('t', 'p'): [
        ('out promoting', '/aʊt̚ pʰɹəˈmoʊtɪŋ/'),
        ('great plan', '/ɡɹeɪt̚ pʰlæn/'),
    ],
    ('t', 'b'): [
        ('at bat', '/æt̚ bæt/'),
        ('great book', '/ɡɹeɪt̚ bʊk/'),
    ],
    ('t', 'k'): [
        ('at camp', '/æt̚ kʰæmp/'),
        ('not clean', '/nɑt̚ kʰlin/'),
    ],
    ('t', 'g'): [
        ('at going', '/æt̚ ˈɡoʊɪŋ/'),
        ('great game', '/ɡɹeɪt̚ ɡeɪm/'),
    ],
    ('t', 'd'): [
        ('at dawn', '/æt̚ dɔn/'),
        ('great day', '/ɡɹeɪt̚ deɪ/'),
    ],
    ('d', 'p'): [
        ('bad plan', '/bæd̚ pʰlæn/'),
        ('need practice', '/nid̚ ˈpʰɹæktɪs/'),
    ],
    ('d', 'b'): [
        ('bad book', '/bæd̚ bʊk/'),
        ('red bird', '/ɹɛd̚ bɜɹd/'),
    ],
    ('d', 't'): [
        ('bad time', '/bæd̚ tʰaɪm/'),
        ('need to go', '/nid̚ tə ɡoʊ/'),
    ],
    ('d', 'k'): [
        ('bad call', '/bæd̚ kʰɔl/'),
        ('need clarity', '/nid̚ ˈkʰlæɹəti/'),
    ],
    ('d', 'g'): [
        ('bad guy', '/bæd̚ ɡaɪ/'),
        ('need guidance', '/nid̚ ˈɡaɪdəns/'),
    ],
    ('k', 'p'): [
        ('back pay', '/bæk̚ pʰeɪ/'),
        ('quick punch', '/kwɪk̚ pʰʌntʃ/'),
    ],
    ('k', 'b'): [
        ('back bone', '/bæk̚ boʊn/'),
        ('quick break', '/kwɪk̚ bɹeɪk/'),
    ],
    ('k', 't'): [
        ('backed', '/bækt̚/'),
        ('packed tight', '/pʰækt̚ tʰaɪt/'),
    ],
    ('k', 'd'): [
        ('back door', '/bæk̚ doɹ/'),
        ('packed down', '/pʰækt̚ daʊn/'),
    ],
    ('k', 'g'): [
        ('back garden', '/bæk̚ ˈɡɑɹdən/'),
        ('quick glance', '/kwɪk̚ ɡlæns/'),
    ],
    ('p', 'p'): [
        ('cup placed', '/kʰʌp̚ pʰleɪst/'),
        ('tap politely', '/tʰæp̚ pəˈlaɪtli/'),
    ],
    ('p', 'b'): [
        ('cup broke', '/kʰʌp̚ bɹoʊk/'),
        ('tap button', '/tʰæp̚ ˈbʌtən/'),
    ],
    ('p', 't'): [
        ('slept', '/slɛpt̚/'),
        ('cup tight', '/kʰʌp̚ tʰaɪt/'),
    ],
    ('p', 'k'): [
        ('cup cake', '/ˈkʰʌp̚ kʰeɪk/'),
        ('tap key', '/tʰæp̚ kʰi/'),
    ],
    ('p', 'd'): [
        ('cup down', '/kʰʌp̚ daʊn/'),
        ('nap daily', '/næp̚ ˈdeɪli/'),
    ],
    ('p', 'g'): [
        ('cup gone', '/kʰʌp̚ ɡɔn/'),
        ('tap gently', '/tʰæp̚ ˈdʒɛntli/'),
    ],
    ('b', 'p'): [
        ('cab pulled', '/kʰæb̚ pʰʊld/'),
        ('web page', '/wɛb̚ pʰeɪdʒ/'),
    ],
    ('b', 'b'): [
        ('cab broke', '/kʰæb̚ bɹoʊk/'),
        ('web browser', '/wɛb̚ ˈbɹaʊzəɹ/'),
    ],
    ('b', 't'): [
        ('cab trip', '/kʰæb̚ tʰɹɪp/'),
        ('web traffic', '/wɛb̚ ˈtʰɹæfɪk/'),
    ],
    ('b', 'k'): [
        ('cab came', '/kʰæb̚ kʰeɪm/'),
        ('web camera', '/wɛb̚ ˈkʰæməɹə/'),
    ],
    ('b', 'd'): [
        ('cab driver', '/kʰæb̚ ˈdɹaɪvəɹ/'),
        ('web design', '/wɛb̚ dɪˈzaɪn/'),
    ],
    ('b', 'g'): [
        ('cab going', '/kʰæb̚ ˈɡoʊɪŋ/'),
        ('web graphics', '/wɛb̚ ˈɡɹæfɪks/'),
    ],
    ('g', 'p'): [
        ('big problem', '/bɪɡ̚ ˈpʰɹɑbləm/'),
        ('bag packed', '/bæɡ̚ pʰækt/'),
    ],
    ('g', 'b'): [
        ('big boat', '/bɪɡ̚ boʊt/'),
        ('bag broke', '/bæɡ̚ bɹoʊk/'),
    ],
    ('g', 't'): [
        ('big time', '/bɪɡ̚ tʰaɪm/'),
        ('bag tucked', '/bæɡ̚ tʰʌkt/'),
    ],
    ('g', 'd'): [
        ('big deal', '/bɪɡ̚ dil/'),
        ('bag dropped', '/bæɡ̚ dɹɑpt/'),
    ],
    ('g', 'k'): [
        ('big car', '/bɪɡ̚ kʰɑɹ/'),
        ('bag crumpled', '/bæɡ̚ ˈkʰɹʌmpəld/'),
    ],
    ('g', 'g'): [
        ('big guy', '/bɪɡ̚ ɡaɪ/'),
        ('bag going', '/bæɡ̚ ˈɡoʊɪŋ/'),
    ],

    # Stop + fricative coarticulations
    ('t', 'f'): [
        ('at first', '/æt̚ fɜɹst/'),
        ('great fight', '/ɡɹeɪt̚ faɪt/'),
    ],
    ('t', 'v'): [
        ('at various times', '/æt̚ ˈvɛɹiəs tʰaɪmz/'),
        ('not very', '/nɑt̚ ˈvɛɹi/'),
    ],
    ('t', 'θ'): [
        ('at this', '/æt̚ ðɪs/'),
        ('great thinking', '/ɡɹeɪt̚ ˈθɪŋkɪŋ/'),
    ],
    ('t', 'ð'): [
        ('at the store', '/æt̪̚ ð̪ə ˈstoɹ/'),
        ('not the one', '/nɑt̪̚ ð̪ə wʌn/'),
    ],
    ('t', 's'): [
        ('at school', '/æt̚ skul/'),
        ('great service', '/ɡɹeɪt̚ ˈsɜɹvɪs/'),
    ],
    ('t', 'z'): [
        ('at zero', '/æt̚ ˈziɹoʊ/'),
        ('cats', '/kʰæts/'),
    ],
    ('t', 'ʃ'): [
        ('at shore', '/æt̚ ʃoɹ/'),
        ('great show', '/ɡɹeɪt̚ ʃoʊ/'),
    ],
    ('t', 'h'): [
        ('at home', '/æt̚ hoʊm/'),
        ('not here', '/nɑt̚ hiɹ/'),
    ],
    ('d', 'f'): [
        ('had five', '/hæd̚ faɪv/'),
        ('need five', '/nid̚ faɪv/'),
    ],
    ('d', 'v'): [
        ('had vision', '/hæd̚ ˈvɪʒən/'),
        ('red vest', '/ɹɛd̚ vɛst/'),
    ],
    ('d', 'θ'): [
        ('had three', '/hæd̚ θɹi/'),
        ('need therapy', '/nid̚ ˈθɛɹəpi/'),
    ],
    ('d', 'ð'): [
        ('read the book', '/ɹid̪̚ ð̪ə bʊk/'),
        ('had the chance', '/hæd̪̚ ð̪ə tʃæns/'),
    ],
    ('d', 's'): [
        ('had some', '/hæd̚ sʌm/'),
        ('needs', '/nidz/'),
    ],
    ('d', 'z'): [
        ('had zero', '/hæd̚ ˈziɹoʊ/'),
        ('beads', '/bidz/'),
    ],
    ('d', 'ʃ'): [
        ('had shoes', '/hæd̚ ʃuz/'),
        ('red shirt', '/ɹɛd̚ ʃɜɹt/'),
    ],
    ('d', 'h'): [
        ('had hoped', '/hæd̚ hoʊpt/'),
        ('red house', '/ɹɛd̚ haʊs/'),
    ],

    # More to come - this is a starter set
    # In production, you'd want examples for all possible combinations
}

def get_example(sound1: str, sound2: str, index: int = 0):
    """
    Get an example for a specific coarticulation pair.
    Returns (phrase, ipa) tuple or None if not found.
    """
    key = (sound1, sound2)
    if key in COARTICULATION_EXAMPLES:
        examples = COARTICULATION_EXAMPLES[key]
        if index < len(examples):
            return examples[index]
        return examples[0]  # Return first if index out of range
    return None

def get_all_examples(sound1: str, sound2: str):
    """
    Get all examples for a specific coarticulation pair.
    """
    key = (sound1, sound2)
    return COARTICULATION_EXAMPLES.get(key, [])
