#!/usr/bin/env python3
"""
Generate coarticulation exercise pages for American English consonants and clusters.
Each page focuses on one consonant/cluster and shows coarticulation with all others.
"""

import os
from typing import List, Dict, Tuple, Optional
try:
    from coarticulation_examples import get_example, get_all_examples
    EXAMPLES_LOADED = True
except ImportError:
    EXAMPLES_LOADED = False

# Define all consonants and clusters in American English
CONSONANTS = {
    # Single consonants
    'p': 'voiceless bilabial stop',
    'b': 'voiced bilabial stop',
    't': 'voiceless alveolar stop',
    'd': 'voiced alveolar stop',
    'k': 'voiceless velar stop',
    'g': 'voiced velar stop',
    'f': 'voiceless labiodental fricative',
    'v': 'voiced labiodental fricative',
    'θ': 'voiceless dental fricative',
    'ð': 'voiced dental fricative',
    's': 'voiceless alveolar fricative',
    'z': 'voiced alveolar fricative',
    'ʃ': 'voiceless postalveolar fricative',
    'ʒ': 'voiced postalveolar fricative',
    'h': 'voiceless glottal fricative',
    'tʃ': 'voiceless postalveolar affricate',
    'dʒ': 'voiced postalveolar affricate',
    'm': 'bilabial nasal',
    'n': 'alveolar nasal',
    'ŋ': 'velar nasal',
    'l': 'alveolar lateral',
    'r': 'alveolar approximant',
    'w': 'labial-velar approximant',
    'j': 'palatal approximant',
}

# Common consonant clusters
CLUSTERS = {
    # Two-consonant clusters - initial
    'pl': 'voiceless bilabial stop + lateral',
    'bl': 'voiced bilabial stop + lateral',
    'pr': 'voiceless bilabial stop + approximant',
    'br': 'voiced bilabial stop + approximant',
    'tr': 'voiceless alveolar stop + approximant',
    'dr': 'voiced alveolar stop + approximant',
    'kl': 'voiceless velar stop + lateral',
    'gl': 'voiced velar stop + lateral',
    'kr': 'voiceless velar stop + approximant',
    'gr': 'voiced velar stop + approximant',
    'kw': 'voiceless velar stop + labial-velar approximant',
    'gw': 'voiced velar stop + labial-velar approximant',
    'tw': 'voiceless alveolar stop + labial-velar approximant',
    'dw': 'voiced alveolar stop + labial-velar approximant',
    'fl': 'voiceless labiodental fricative + lateral',
    'fr': 'voiceless labiodental fricative + approximant',
    'θr': 'voiceless dental fricative + approximant',
    'ʃr': 'voiceless postalveolar fricative + approximant',
    'sp': 's + voiceless bilabial stop',
    'st': 's + voiceless alveolar stop',
    'sk': 's + voiceless velar stop',
    'sm': 's + bilabial nasal',
    'sn': 's + alveolar nasal',
    'sl': 's + lateral',
    'sw': 's + labial-velar approximant',

    # Two-consonant clusters - final
    'pt': 'voiceless bilabial stop + voiceless alveolar stop',
    'kt': 'voiceless velar stop + voiceless alveolar stop',
    'ps': 'voiceless bilabial stop + voiceless alveolar fricative',
    'ts': 'voiceless alveolar stop + voiceless alveolar fricative',
    'ks': 'voiceless velar stop + voiceless alveolar fricative',
    'ft': 'voiceless labiodental fricative + voiceless alveolar stop',
    'θt': 'voiceless dental fricative + voiceless alveolar stop',
    'mp': 'bilabial nasal + voiceless bilabial stop',
    'nt': 'alveolar nasal + voiceless alveolar stop',
    'ŋk': 'velar nasal + voiceless velar stop',
    'nd': 'alveolar nasal + voiced alveolar stop',
    'ŋg': 'velar nasal + voiced velar stop',
    'lp': 'lateral + voiceless bilabial stop',
    'lb': 'lateral + voiced bilabial stop',
    'lt': 'lateral + voiceless alveolar stop',
    'ld': 'lateral + voiced alveolar stop',
    'lk': 'lateral + voiceless velar stop',
    'lf': 'lateral + voiceless labiodental fricative',
    'lv': 'lateral + voiced labiodental fricative',
    'lθ': 'lateral + voiceless dental fricative',
    'ls': 'lateral + voiceless alveolar fricative',
    'lz': 'lateral + voiced alveolar fricative',
    'lʃ': 'lateral + voiceless postalveolar fricative',
    'ltʃ': 'lateral + voiceless postalveolar affricate',
    'ldʒ': 'lateral + voiced postalveolar affricate',
    'lm': 'lateral + bilabial nasal',
    'rp': 'approximant + voiceless bilabial stop',
    'rb': 'approximant + voiced bilabial stop',
    'rt': 'approximant + voiceless alveolar stop',
    'rd': 'approximant + voiced alveolar stop',
    'rk': 'approximant + voiceless velar stop',
    'rf': 'approximant + voiceless labiodental fricative',
    'rv': 'approximant + voiced labiodental fricative',
    'rθ': 'approximant + voiceless dental fricative',
    'rs': 'approximant + voiceless alveolar fricative',
    'rz': 'approximant + voiced alveolar fricative',
    'rʃ': 'approximant + voiceless postalveolar fricative',
    'rtʃ': 'approximant + voiceless postalveolar affricate',
    'rdʒ': 'approximant + voiced postalveolar affricate',
    'rm': 'approximant + bilabial nasal',
    'rn': 'approximant + alveolar nasal',

    # Three-consonant clusters
    'spl': 's + voiceless bilabial stop + lateral',
    'spr': 's + voiceless bilabial stop + approximant',
    'str': 's + voiceless alveolar stop + approximant',
    'skr': 's + voiceless velar stop + approximant',
    'skw': 's + voiceless velar stop + labial-velar approximant',
    'mpt': 'bilabial nasal + voiceless bilabial stop + voiceless alveolar stop',
    'mps': 'bilabial nasal + voiceless bilabial stop + voiceless alveolar fricative',
    'nst': 'alveolar nasal + voiceless alveolar fricative + voiceless alveolar stop',
    'nts': 'alveolar nasal + voiceless alveolar stop + voiceless alveolar fricative',
    'ŋkt': 'velar nasal + voiceless velar stop + voiceless alveolar stop',
    'ŋks': 'velar nasal + voiceless velar stop + voiceless alveolar fricative',
    'lpt': 'lateral + voiceless bilabial stop + voiceless alveolar stop',
    'lps': 'lateral + voiceless bilabial stop + voiceless alveolar fricative',
    'lst': 'lateral + voiceless alveolar fricative + voiceless alveolar stop',
    'lts': 'lateral + voiceless alveolar stop + voiceless alveolar fricative',
    'lkt': 'lateral + voiceless velar stop + voiceless alveolar stop',
    'lks': 'lateral + voiceless velar stop + voiceless alveolar fricative',
    'rpt': 'approximant + voiceless bilabial stop + voiceless alveolar stop',
    'rps': 'approximant + voiceless bilabial stop + voiceless alveolar fricative',
    'rst': 'approximant + voiceless alveolar fricative + voiceless alveolar stop',
    'rts': 'approximant + voiceless alveolar stop + voiceless alveolar fricative',
    'rkt': 'approximant + voiceless velar stop + voiceless alveolar stop',
    'rks': 'approximant + voiceless velar stop + voiceless alveolar fricative',
    'lfθ': 'lateral + voiceless labiodental fricative + voiceless dental fricative',
    'lθs': 'lateral + voiceless dental fricative + voiceless alveolar fricative',
    'skt': 's + voiceless velar stop + voiceless alveolar stop',
    'sks': 's + voiceless velar stop + voiceless alveolar fricative',
    'spt': 's + voiceless bilabial stop + voiceless alveolar stop',
    'sps': 's + voiceless bilabial stop + voiceless alveolar fricative',
    'sts': 's + voiceless alveolar stop + voiceless alveolar fricative',
}

def get_example_phrase(sound1: str, sound2: str) -> Tuple[str, str]:
    """
    Generate or retrieve an example phrase for coarticulation.
    Returns (phrase, ipa_transcription)
    """
    # Check if we have a specific example from the database
    if EXAMPLES_LOADED:
        example = get_example(sound1, sound2)
        if example:
            return example

    # Fallback: Generate generic examples
    # Common words ending with various sounds (for word-final position)
    final_words = {
        'p': ('cup', '/kʰʌp̚/'),
        'b': ('cab', '/kʰæb̚/'),
        't': ('cat', '/kʰæt̚/'),
        'd': ('bad', '/bæd̚/'),
        'k': ('back', '/bæk̚/'),
        'g': ('bag', '/bæɡ̚/'),
        'f': ('safe', '/seɪf/'),
        'v': ('save', '/seɪv/'),
        'θ': ('bath', '/bæθ/'),
        'ð': ('bathe', '/beɪð/'),
        's': ('pass', '/pʰæs/'),
        'z': ('jazz', '/dʒæz/'),
        'ʃ': ('wash', '/wɑʃ/'),
        'ʒ': ('rouge', '/ɹuʒ/'),
        'h': ('', ''),  # h doesn't occur word-finally
        'tʃ': ('catch', '/kʰætʃ/'),
        'dʒ': ('judge', '/dʒʌdʒ/'),
        'm': ('jam', '/dʒæm/'),
        'n': ('can', '/kʰæn/'),
        'ŋ': ('sing', '/sɪŋ/'),
        'l': ('call', '/kʰɔl/'),
        'r': ('car', '/kʰɑɹ/'),
        'w': ('', ''),  # w doesn't occur word-finally
        'j': ('', ''),  # j doesn't occur word-finally
    }

    # Common words beginning with various sounds (for word-initial position)
    initial_words = {
        'p': ('pay', '/pʰeɪ/'),
        'b': ('bay', '/beɪ/'),
        't': ('take', '/tʰeɪk/'),
        'd': ('day', '/deɪ/'),
        'k': ('came', '/kʰeɪm/'),
        'g': ('game', '/ɡeɪm/'),
        'f': ('five', '/faɪv/'),
        'v': ('very', '/ˈvɛɹi/'),
        'θ': ('think', '/θɪŋk/'),
        'ð': ('the', '/ðə/'),
        's': ('say', '/seɪ/'),
        'z': ('zero', '/ˈziɹoʊ/'),
        'ʃ': ('show', '/ʃoʊ/'),
        'ʒ': ('', ''),  # rare word-initially
        'h': ('home', '/hoʊm/'),
        'tʃ': ('change', '/tʃeɪndʒ/'),
        'dʒ': ('just', '/dʒʌst/'),
        'm': ('my', '/maɪ/'),
        'n': ('new', '/nu/'),
        'ŋ': ('', ''),  # doesn't occur word-initially
        'l': ('late', '/leɪt/'),
        'r': ('ray', '/ɹeɪ/'),
        'w': ('way', '/weɪ/'),
        'j': ('yes', '/jɛs/'),
    }

    # Try to create a phrase
    if sound1 in final_words and sound1 and final_words[sound1][0]:
        word1 = final_words[sound1][0]
        ipa1 = final_words[sound1][1]

        if sound2 in initial_words and sound2 and initial_words[sound2][0]:
            word2 = initial_words[sound2][0]
            ipa2 = initial_words[sound2][1]
            phrase = f"{word1} {word2}"
            ipa = f"{ipa1[:-1]} {ipa2[1:]}"  # Combine IPA (remove slashes)
            return (phrase, f"/{ipa.replace('//', '')}/")

    # Ultimate fallback
    return (f"[example of {sound1}+{sound2}]", f"/...{sound1}{sound2}.../")


def create_coarticulation_page(target_sound: str, description: str, all_sounds: Dict[str, str], output_dir: str):
    """
    Create a coarticulation exercise page for a specific sound/cluster.
    """
    filename = f"{target_sound}.md"
    # Replace problematic characters in filename
    filename = filename.replace('ʃ', 'sh').replace('ʒ', 'zh').replace('θ', 'th').replace('ð', 'dh')
    filename = filename.replace('tʃ', 'ch').replace('dʒ', 'j').replace('ŋ', 'ng')

    filepath = os.path.join(output_dir, filename)

    content = f"""# Coarticulation Exercises: /{target_sound}/

**Sound:** {description}

This page contains exercises for coarticulating /{target_sound}/ with all other consonant sounds and clusters in American English. Practice both within-word and across-word-boundary contexts.

---

"""

    # Create exercises for coarticulation with each other sound
    for other_sound, other_desc in sorted(all_sounds.items()):
        if other_sound == target_sound:
            continue  # Skip self-coarticulation

        content += f"## {target_sound} + {other_sound}\n\n"

        # Get example phrase
        phrase, ipa = get_example_phrase(target_sound, other_sound)

        content += f"**{phrase}**  \n"
        content += f"`{ipa}`\n\n"
        content += "---\n\n"

    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename

def main():
    """Generate all coarticulation exercise pages."""

    # Create output directory
    output_dir = 'coarticulation-exercises'
    os.makedirs(output_dir, exist_ok=True)

    # Combine all sounds
    all_sounds = {**CONSONANTS, **CLUSTERS}

    # Create a page for each sound
    created_files = []
    for sound, description in sorted(all_sounds.items()):
        filename = create_coarticulation_page(sound, description, all_sounds, output_dir)
        created_files.append(filename)
        print(f"Created: {filename}")

    # Create index/README
    create_index(all_sounds, output_dir, created_files)

    print(f"\nGenerated {len(created_files)} coarticulation exercise pages.")

def create_index(all_sounds: Dict[str, str], output_dir: str, created_files: List[str]):
    """Create an index page listing all coarticulation exercises."""

    filepath = os.path.join(output_dir, 'README.md')

    content = """# Consonant Coarticulation Exercises

This directory contains comprehensive coarticulation exercises for American English (General American/Neutral Broadcast English).

Each page focuses on one consonant sound or consonant cluster and provides practice examples for coarticulating it with every other consonant sound or cluster in the language.

## Organization

- **Single Consonants:** Individual consonant phonemes
- **Two-Consonant Clusters:** Common clusters in initial and final positions
- **Three-Consonant Clusters:** Complex clusters found in American English

## Single Consonants

### Stops
"""

    stops = ['p', 'b', 't', 'd', 'k', 'g']
    for sound in stops:
        if sound in all_sounds:
            filename = sound + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n### Fricatives\n"
    fricatives = ['f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'h']
    for sound in fricatives:
        if sound in all_sounds:
            filename = sound.replace('ʃ', 'sh').replace('ʒ', 'zh').replace('θ', 'th').replace('ð', 'dh') + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n### Affricates\n"
    affricates = ['tʃ', 'dʒ']
    for sound in affricates:
        if sound in all_sounds:
            filename = sound.replace('tʃ', 'ch').replace('dʒ', 'j') + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n### Nasals\n"
    nasals = ['m', 'n', 'ŋ']
    for sound in nasals:
        if sound in all_sounds:
            filename = sound.replace('ŋ', 'ng') + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n### Liquids & Approximants\n"
    liquids = ['l', 'r', 'w', 'j']
    for sound in liquids:
        if sound in all_sounds:
            filename = sound + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n## Consonant Clusters\n\n"
    content += "### Two-Consonant Clusters\n"

    two_consonant = [k for k in CLUSTERS.keys() if len(k) == 2 or (len(k) == 3 and k[1] == 'ʃ')]
    for sound in sorted(two_consonant):
        if sound in all_sounds:
            filename = sound.replace('ʃ', 'sh').replace('ʒ', 'zh').replace('θ', 'th').replace('ð', 'dh')
            filename = filename.replace('tʃ', 'ch').replace('dʒ', 'j').replace('ŋ', 'ng') + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += "\n### Three-Consonant Clusters\n"
    three_consonant = [k for k in CLUSTERS.keys() if len(k) >= 3 and k not in two_consonant]
    for sound in sorted(three_consonant):
        if sound in all_sounds:
            filename = sound.replace('ʃ', 'sh').replace('ʒ', 'zh').replace('θ', 'th').replace('ð', 'dh')
            filename = filename.replace('tʃ', 'ch').replace('dʒ', 'j').replace('ŋ', 'ng') + '.md'
            content += f"- [/{sound}/]({filename}) - {all_sounds[sound]}\n"

    content += """
## How to Use These Exercises

1. **Focus on articulation:** Pay attention to how your articulators (tongue, lips, teeth, etc.) transition from one sound to another.

2. **Practice slowly first:** Start by saying each phrase slowly, focusing on the precise articulatory movements.

3. **Increase speed gradually:** As you become more comfortable, increase your speaking rate to natural conversational speed.

4. **Record yourself:** Listen to your productions to identify areas that need improvement.

5. **Focus on transitions:** The key to natural coarticulation is smooth transitions between sounds.

## About Coarticulation

Coarticulation is the natural phenomenon where speech sounds influence each other in connected speech. When consonants appear adjacent to each other (either within a word or across word boundaries), their articulation overlaps and they influence each other's production.

Understanding and practicing coarticulation is essential for:
- Clear, natural-sounding speech
- Dialect coaching and accent modification
- Speech-language pathology
- Voice acting and broadcasting
- Language learning and teaching

---

*Generated for American English phonetic training*
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created index: README.md")

if __name__ == '__main__':
    main()
