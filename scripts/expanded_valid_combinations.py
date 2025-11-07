"""
Expanded database of phonetically valid consonant combinations in American English.
Each entry includes detailed IPA with full coarticulation diacritics.
"""

# This will be imported by validate_combinations.py
EXPANDED_VALID_COMBINATIONS = {
    # The user's example and high-priority combinations with FULL IPA detail

    # T + all valid combinations
    ('t', 'ð'): [
        ('at the store', '/æt̪̚ ð̪ə ˈstoɹ/', 'Dentalized unreleased /t̪̚/ before dental /ð̪/'),
        ('not the one', '/nɑt̪̚ ð̪ə wʌn/', 'Complete dental assimilation'),
        ('hit them hard', '/hɪt̪̚ ð̪əm ˈhɑɹd/', 'Dental coarticulation across boundary'),
    ],
    ('t', 'θ'): [
        ('at three', '/æt̪̚ θɹi/', 'Dentalized /t̪/ before voiceless /θ/'),
        ('not thinking', '/nɑt̪̚ ˈθɪŋkɪŋ/', 'Place assimilation to dental'),
    ],
    ('t', 'p'): [
        ('at peace', '/æt̚ pʰis/', 'Unreleased alveolar, aspirated bilabial'),
        ('not possible', '/nɑt̚ ˈpʰɑsəbəl/', 'Stop-stop cluster'),
    ],
    ('t', 'b'): [
        ('at bat', '/æt̚ bæt/', 'Unreleased /t̚/, partial devoicing of /b/'),
        ('great book', '/ɡɹeɪt̚ bʊk/', 'Voiceless-voiced transition'),
    ],
    ('t', 'k'): [
        ('at camp', '/æt̚ kʰæmp/', 'Unreleased alveolar + aspirated velar'),
        ('night club', '/naɪt̚ kʰlʌb/', 'Double stop sequence'),
    ],
    ('t', 'g'): [
        ('at going', '/æt̚ ˈɡoʊɪŋ/', 'Voicing begins during /g/ closure'),
        ('not good', '/nɑt̚ ɡʊd/', 'Partial /g/ devoicing'),
    ],
    ('t', 'd'): [
        ('at dawn', '/æt̚ dɔn/', 'Homorganic voicing contrast'),
        ('not done', '/nɑt̚ dʌn/', 'Often merges to single [t̚] or [d̚]'),
    ],
    ('t', 'f'): [
        ('at first', '/æt̚ fɝst/', 'Stop to fricative transition'),
        ('not far', '/nɑt̚ fɑɹ/', 'Maintained stop closure'),
    ],
    ('t', 'v'): [
        ('at various times', '/æt̚ ˈvɛɹiəs tʰaɪmz/', 'Stop before voiced fricative'),
        ('not very', '/nɑt̚ ˈvɛɹi/', 'Slight /v/ devoicing possible'),
    ],
    ('t', 's'): [
        ('at school', '/æt̚ skuɫ/', 'Homorganic, /t/ often deleted'),
        ('cats', '/kʰæts/', 'Released /t/ in cluster'),
        ('it seems', '/ɪt̚ simz/', 'Unreleased or deleted /t/'),
    ],
    ('t', 'z'): [
        ('at zero', '/æt̚ ˈziɹoʊ/', 'Voicing contrast maintained'),
        ('it is', '/ɪt̚ ɪz/', 'Weak form, may reduce'),
    ],
    ('t', 'ʃ'): [
        ('at shore', '/æt̚ ʃoɹ/', 'Slight /t/ retraction anticipating /ʃ/'),
        ('not sure', '/nɑt̚ ʃʊɹ/', 'Postalveolar anticipation'),
    ],
    ('t', 'tʃ'): [
        ('at church', '/æt̚ tʃɝtʃ/', 'Stop before affricate'),
        ('not cheap', '/nɑt̚ tʃip/', 'May merge gestures'),
    ],
    ('t', 'dʒ'): [
        ('at just', '/æt̚ dʒʌst/', 'Voiceless stop + voiced affricate'),
        ('not John', '/nɑt̚ dʒɑn/', 'Slight devoicing of /dʒ/'),
    ],
    ('t', 'h'): [
        ('at home', '/æt̚ hoʊm/', 'May have glottal release'),
        ('not here', '/nɑt̚ hiɹ/', 'Breathy transition'),
    ],
    ('t', 'm'): [
        ('at my house', '/æt̚ maɪ haʊs/', 'Oral stop to nasal'),
        ('not much', '/nɑt̚ mʌtʃ/', 'Possible nasal release'),
    ],
    ('t', 'n'): [
        ('at night', '/æt̚ naɪt/', 'Nasal release, homorganic'),
        ('button', '/ˈbʌʔn̩/', 'Glottal + syllabic nasal'),
        ('not now', '/nɑt̚ naʊ/', 'Lateral plosion possible'),
    ],
    ('t', 'l'): [
        ('at last', '/æt̚ læst/', 'Lateral release'),
        ('bottle', '/ˈbɑɾɫ̩/', 'Tap or lateral release + syllabic'),
        ('not late', '/nɑt̚ leɪt/', 'Clear /l/ after fortis'),
    ],
    ('t', 'r'): [
        ('at risk', '/æt̚ ɹɪsk/', 'Stop before rhotic'),
        ('not really', '/nɑt̚ ˈɹiəli/', 'Slight retroflexion of /t/'),
    ],
    ('t', 'w'): [
        ('at work', '/æt̚ wɝk/', 'Lip rounding anticipation'),
        ('not willing', '/nɑt̚ ˈwɪlɪŋ/', 'Labial gesture overlaps'),
    ],
    ('t', 'j'): [
        ('at your place', '/æ(t̚) jɚ pʰleɪs/', 'Often becomes [tʃ]'),
        ('not yet', '/nɑtʃ jɛt/', 'Coalescence to affricate common'),
    ],

    # D + combinations
    ('d', 'ð'): [
        ('read the book', '/ɹid̪̚ ð̪ə bʊk/', 'Dentalized /d̪/ before /ð̪/'),
        ('had the time', '/hæd̪̚ ð̪ə tʰaɪm/', 'Complete dentalization'),
        ('could they', '/kʰʊd̪̚ ð̪eɪ/', 'Dental place assimilation'),
    ],
    ('d', 'θ'): [
        ('had three', '/hæd̪̚ θɹi/', 'Dentalized before voiceless'),
        ('need therapy', '/nid̪̚ ˈθɛɹəpi/', 'Devoicing + dentalization'),
    ],
    ('d', 'p'): [
        ('bad plan', '/bæd̥̚ pʰlæn/', 'Devoiced /d̥/ before /p/'),
        ('need practice', '/nid̥̚ ˈpʰɹæktɪs/', 'Partial devoicing'),
    ],
    ('d', 'b'): [
        ('bad book', '/bæd̚ bʊk/', 'Voiced sequence maintained'),
        ('red bird', '/ɹɛd̚ bɝd/', 'Unreleased /d̚/'),
    ],
    ('d', 't'): [
        ('bad time', '/bæd̥̚ tʰaɪm/', 'Devoicing of /d/, unreleased'),
        ('need to', '/nid̚ tə/', 'May merge to [t̚]'),
    ],
    ('d', 'k'): [
        ('bad call', '/bæd̥̚ kʰɔɫ/', 'Devoicing before /k/'),
        ('good coffee', '/ɡʊd̥̚ ˈkʰɔfi/', 'Place and voicing change'),
    ],
    ('d', 'g'): [
        ('bad guy', '/bæd̚ ɡaɪ/', 'Both voiced, maintained'),
        ('good game', '/ɡʊd̚ ɡeɪm/', 'Voiced sequence'),
    ],
    ('d', 'f'): [
        ('had five', '/hæd̥̚ faɪv/', 'Devoicing anticipation'),
        ('good food', '/ɡʊd̥̚ fud/', 'Partial devoicing'),
    ],
    ('d', 'v'): [
        ('had vision', '/hæd̚ ˈvɪʒən/', 'Voiced continuity'),
        ('good value', '/ɡʊd̚ ˈvælju/', 'Maintained voicing'),
    ],
    ('d', 's'): [
        ('needs', '/nidz/', 'Voiced /z/ allomorph'),
        ('had some', '/hæd̥̚ sʌm/', 'Devoicing to [t̚s]'),
    ],
    ('d', 'z'): [
        ('had zero', '/hæd̚ ˈziɹoʊ/', 'Voiced fricative maintained'),
    ],
    ('d', 'ʃ'): [
        ('had shoes', '/hæd̥̚ ʃuz/', 'Devoicing + slight retraction'),
        ('good show', '/ɡʊd̥̚ ʃoʊ/', 'Postalveolar anticipation'),
    ],
    ('d', 'tʃ'): [
        ('bad choice', '/bæd̥̚ tʃɔɪs/', 'Devoicing before affricate'),
    ],
    ('d', 'dʒ'): [
        ('bad joke', '/bæd̚ dʒoʊk/', 'Voiced sequence maintained'),
    ],
    ('d', 'h'): [
        ('had hoped', '/hæd̥̚ hoʊpt/', 'Devoicing, breathy onset'),
    ],
    ('d', 'm'): [
        ('bad man', '/bæd̚ mæn/', 'Possible nasal release'),
        ('good morning', '/ɡʊd̚ ˈmɔɹnɪŋ/', 'Oral to nasal'),
    ],
    ('d', 'n'): [
        ('had never', '/hæd̚ ˈnɛvɚ/', 'Nasal release, homorganic'),
        ('sudden', '/ˈsʌdn̩/', 'Syllabic nasal release'),
    ],
    ('d', 'l'): [
        ('bad luck', '/bæd̚ lʌk/', 'Lateral release possible'),
        ('middle', '/ˈmɪdɫ̩/', 'Syllabic lateral'),
    ],
    ('d', 'r'): [
        ('had reason', '/hæd̚ ˈɹizən/', 'Slight retroflexion'),
    ],
    ('d', 'w'): [
        ('had wanted', '/hæd̚ ˈwɑntɪd/', 'Labial anticipation'),
    ],
    ('d', 'j'): [
        ('did you', '/dɪdʒ ju/', 'Coalescence to [dʒ] common'),
        ('would you', '/wʊdʒ ju/', 'Palatalization'),
    ],

    # Will continue with more... this is getting large
    # For now let's test with what we have
}

# Merge with base database
def get_all_valid_combinations():
    """Get combined database from both files."""
    from validate_combinations import VALID_COMBINATIONS
    combined = {**VALID_COMBINATIONS, **EXPANDED_VALID_COMBINATIONS}
    return combined
