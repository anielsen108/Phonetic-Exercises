#!/usr/bin/env python3
"""
Generate individual pages for each consonant combination pair.
Each page focuses on one specific coarticulation (e.g., nst+ð) with multiple examples.
"""

import os
from typing import List, Dict, Tuple
from itertools import product

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

def sanitize_filename(sound: str) -> str:
    """Convert IPA symbols to filesystem-safe names."""
    return (sound
            .replace('ʃ', 'sh')
            .replace('ʒ', 'zh')
            .replace('θ', 'th')
            .replace('ð', 'dh')
            .replace('tʃ', 'ch')
            .replace('dʒ', 'dzh')
            .replace('ŋ', 'ng'))

def create_combination_page(sound1: str, desc1: str, sound2: str, desc2: str, output_dir: str) -> str:
    """
    Create a page for a specific sound combination.
    Returns the filename created.
    """
    # Create filename
    safe_sound1 = sanitize_filename(sound1)
    safe_sound2 = sanitize_filename(sound2)
    filename = f"{safe_sound1}-{safe_sound2}.md"
    filepath = os.path.join(output_dir, filename)

    # Create page content - shell for now
    content = f"""# Coarticulation: /{sound1}/ + /{sound2}/

## Sound Combination

**First sound:** /{sound1}/ — {desc1}
**Second sound:** /{sound2}/ — {desc2}

---

## Practice Exercises

### Example 1
**Phrase:** [Placeholder - to be filled]
**IPA:** /...{sound1}{sound2}.../

**Notes:** Focus on the transition from {desc1} to {desc2}.

---

### Example 2
**Phrase:** [Placeholder - to be filled]
**IPA:** /...{sound1}{sound2}.../

**Notes:** Practice in connected speech across word boundaries.

---

### Example 3
**Phrase:** [Placeholder - to be filled]
**IPA:** /...{sound1}{sound2}.../

**Notes:** Maintain natural timing and rhythm.

---

## Articulation Tips

- **Starting position:** {desc1}
- **Target position:** {desc2}
- **Key transition:** [To be filled with specific articulatory guidance]

## Common Contexts

This sound combination appears in:
- [ ] Word-internal position
- [ ] Across word boundaries
- [ ] Common phrases
- [ ] Less common/careful speech only

---

[← Back to all combinations](README.md)
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename

def main():
    """Generate individual pages for all sound combinations."""

    # Create output directory
    output_dir = 'exercises'
    os.makedirs(output_dir, exist_ok=True)

    # Combine all sounds
    all_sounds = {**CONSONANTS, **CLUSTERS}

    # Generate pages for all combinations
    created_files = []
    total_combinations = 0

    print("Generating individual combination pages...")

    for sound1, desc1 in sorted(all_sounds.items()):
        for sound2, desc2 in sorted(all_sounds.items()):
            if sound1 == sound2:
                continue  # Skip self-combinations

            filename = create_combination_page(sound1, desc1, sound2, desc2, output_dir)
            created_files.append((sound1, sound2, filename))
            total_combinations += 1

            if total_combinations % 100 == 0:
                print(f"  Generated {total_combinations} combinations...")

    print(f"\nCreated {total_combinations} combination pages.")

    # Create index
    create_index(all_sounds, created_files, output_dir)

    return created_files

def create_index(all_sounds: Dict[str, str], created_files: List[Tuple[str, str, str]], output_dir: str):
    """Create an index/navigation page."""

    filepath = os.path.join(output_dir, 'README.md')

    content = f"""# Consonant Coarticulation Exercises - All Combinations

This directory contains **{len(created_files)} individual exercise pages**, one for each possible consonant-to-consonant coarticulation in American English.

## How to Use

Each page focuses on ONE specific sound transition (e.g., /nst/ → /ð/) and provides:
- Multiple example phrases
- Detailed IPA transcriptions
- Articulatory guidance
- Practice notes

## Browse by Starting Sound

"""

    # Group by first sound
    by_first_sound = {}
    for sound1, sound2, filename in created_files:
        if sound1 not in by_first_sound:
            by_first_sound[sound1] = []
        by_first_sound[sound1].append((sound2, filename))

    # Generate index organized by first sound
    for sound1 in sorted(by_first_sound.keys()):
        desc1 = all_sounds[sound1]
        content += f"\n### /{sound1}/ ({desc1})\n\n"

        combinations = by_first_sound[sound1]
        # Show first 10, then summarize
        for i, (sound2, filename) in enumerate(sorted(combinations)):
            if i < 10:
                content += f"- [/{sound1}/ + /{sound2}/]({filename})\n"

        if len(combinations) > 10:
            content += f"- ... and {len(combinations) - 10} more combinations\n"

        content += "\n"

    content += f"""
## Statistics

- **Total sounds/clusters:** {len(all_sounds)}
- **Total combinations:** {len(created_files)}
- **Single consonants:** {len(CONSONANTS)}
- **Consonant clusters:** {len(CLUSTERS)}

## Organization

Pages are named using the pattern: `sound1-sound2.md`

IPA symbols are converted to ASCII-safe names:
- ʃ → sh
- ʒ → zh
- θ → th
- ð → dh
- tʃ → ch
- dʒ → dzh
- ŋ → ng

---

*Shell pages created. Examples to be filled in.*
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created index: README.md")

if __name__ == '__main__':
    main()
