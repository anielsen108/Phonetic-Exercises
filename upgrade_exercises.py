#!/usr/bin/env python3
"""
Upgrade all exercise pages to the detailed coarticulation study format.
Based on the b-d.md model.
"""

import os
import glob
from typing import List, Tuple, Dict

# Import curated combinations
from curated_combinations import get_curated_combinations

# Comprehensive sound descriptions
SOUND_DATA = {
    'p': {'symbol': 'p', 'place': 'bilabial', 'manner': 'stop (plosive)', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'short, often aspirated word-initially'},
    'b': {'symbol': 'b', 'place': 'bilabial', 'manner': 'stop (plosive)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'short closure, often unreleased'},
    't': {'symbol': 't', 'place': 'alveolar', 'manner': 'stop (plosive)', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'short, often unreleased word-finally'},
    'd': {'symbol': 'd', 'place': 'alveolar', 'manner': 'stop (plosive)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'variable, flapped intervocalically'},
    'k': {'symbol': 'k', 'place': 'velar', 'manner': 'stop (plosive)', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'short, aspirated in stressed onsets'},
    'g': {'symbol': 'g', 'place': 'velar', 'manner': 'stop (plosive)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'short, often reduced finally'},
    'f': {'symbol': 'f', 'place': 'labiodental', 'manner': 'fricative', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'continuous, variable length'},
    'v': {'symbol': 'v', 'place': 'labiodental', 'manner': 'fricative', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'continuous, may devoice finally'},
    'θ': {'symbol': 'θ', 'place': 'dental', 'manner': 'fricative', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'continuous'},
    'ð': {'symbol': 'ð', 'place': 'dental', 'manner': 'fricative', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'continuous, common in function words'},
    's': {'symbol': 's', 'place': 'alveolar', 'manner': 'fricative (sibilant)', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'continuous, high-energy'},
    'z': {'symbol': 'z', 'place': 'alveolar', 'manner': 'fricative (sibilant)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'continuous, may devoice'},
    'ʃ': {'symbol': 'ʃ', 'place': 'postalveolar', 'manner': 'fricative (sibilant)', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'continuous, lower pitch than /s/'},
    'ʒ': {'symbol': 'ʒ', 'place': 'postalveolar', 'manner': 'fricative (sibilant)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'continuous, rare in English'},
    'h': {'symbol': 'h', 'place': 'glottal', 'manner': 'fricative', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'brief, anticipates following vowel'},
    'tʃ': {'symbol': 'tʃ', 'place': 'postalveolar', 'manner': 'affricate', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'stop + fricative sequence'},
    'dʒ': {'symbol': 'dʒ', 'place': 'postalveolar', 'manner': 'affricate', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'stop + fricative sequence'},
    'm': {'symbol': 'm', 'place': 'bilabial', 'manner': 'nasal', 'voicing': 'voiced', 'airflow': 'nasal', 'duration': 'continuous resonant'},
    'n': {'symbol': 'n', 'place': 'alveolar', 'manner': 'nasal', 'voicing': 'voiced', 'airflow': 'nasal', 'duration': 'continuous resonant'},
    'ŋ': {'symbol': 'ŋ', 'place': 'velar', 'manner': 'nasal', 'voicing': 'voiced', 'airflow': 'nasal', 'duration': 'continuous resonant'},
    'l': {'symbol': 'l', 'place': 'alveolar', 'manner': 'lateral approximant', 'voicing': 'voiced', 'airflow': 'oral (lateral)', 'duration': 'continuous, velarized finally'},
    'r': {'symbol': 'r', 'place': 'alveolar/postalveolar', 'manner': 'approximant (rhotic)', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'continuous, may be syllabic'},
    'w': {'symbol': 'w', 'place': 'labial-velar', 'manner': 'approximant', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'brief glide'},
    'j': {'symbol': 'j', 'place': 'palatal', 'manner': 'approximant', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'brief glide'},
    'nst': {'symbol': 'nst', 'place': 'nasal-alveolar-alveolar', 'manner': 'nasal + fricative + stop', 'voicing': 'voiced then voiceless', 'airflow': 'nasal then oral', 'duration': 'complex cluster'},
    'st': {'symbol': 'st', 'place': 'alveolar', 'manner': 'fricative + stop', 'voicing': 'voiceless', 'airflow': 'oral', 'duration': 'common cluster'},
    'dr': {'symbol': 'dr', 'place': 'alveolar', 'manner': 'stop + approximant', 'voicing': 'voiced', 'airflow': 'oral', 'duration': 'onset cluster'},
}

def get_sound_description(sound: str) -> str:
    """Get descriptive text for a sound."""
    descriptors = {
        'p': 'voiceless bilabial stop', 'b': 'voiced bilabial stop',
        't': 'voiceless alveolar stop', 'd': 'voiced alveolar stop',
        'k': 'voiceless velar stop', 'g': 'voiced velar stop',
        'f': 'voiceless labiodental fricative', 'v': 'voiced labiodental fricative',
        'θ': 'voiceless dental fricative', 'ð': 'voiced dental fricative',
        's': 'voiceless alveolar fricative', 'z': 'voiced alveolar fricative',
        'ʃ': 'voiceless postalveolar fricative', 'ʒ': 'voiced postalveolar fricative',
        'h': 'voiceless glottal fricative',
        'tʃ': 'voiceless postalveolar affricate', 'dʒ': 'voiced postalveolar affricate',
        'm': 'bilabial nasal', 'n': 'alveolar nasal', 'ŋ': 'velar nasal',
        'l': 'alveolar lateral approximant', 'r': 'alveolar approximant',
        'w': 'labial-velar approximant', 'j': 'palatal approximant',
        'nst': 'nasal + fricative + stop cluster',
        'st': 'fricative + stop cluster',
        'dr': 'stop + approximant cluster',
    }
    return descriptors.get(sound, sound)

def generate_coarticulatory_mechanisms(sound1: str, sound2: str, examples: List[Tuple[str, str, str]]) -> List[str]:
    """Generate specific coarticulatory mechanisms for this sound pair."""
    mechanisms = []

    # Get sound properties
    s1_data = SOUND_DATA.get(sound1, {})
    s2_data = SOUND_DATA.get(sound2, {})
    s1_place = s1_data.get('place', '')
    s2_place = s2_data.get('place', '')
    s1_voicing = s1_data.get('voicing', '')
    s2_voicing = s2_data.get('voicing', '')
    s1_manner = s1_data.get('manner', '')
    s2_manner = s2_data.get('manner', '')

    # Place assimilation
    if s1_place != s2_place and s1_place and s2_place:
        mechanisms.append(f"**Anticipatory Place Shift:**\n   "
                         f"The tongue/lips begin moving toward the {s2_place} target before the /{sound1}/ "
                         f"gesture completes. This creates overlap between {s1_place} and {s2_place} articulations.")

    # Voicing continuity or change
    if s1_voicing == s2_voicing == 'voiced':
        mechanisms.append(f"**Voicing Continuity:**\n   "
                         f"Both /{sound1}/ and /{sound2}/ are voiced; the glottis remains adducted throughout. "
                         f"Spectrographically, this appears as a continuous low-frequency voicing bar.")
    elif s1_voicing != s2_voicing:
        mechanisms.append(f"**Voicing Transition:**\n   "
                         f"The glottis shifts from {s1_voicing} to {s2_voicing}. This transition may show "
                         f"partial devoicing or voicing anticipation depending on speech rate.")

    # Stop-specific mechanisms
    if 'stop' in s1_manner and 'stop' in s2_manner:
        mechanisms.append(f"**Stop Release Overlap:**\n   "
                         f"The /{sound1}/ is typically unreleased ([{sound1}̚]), with air pressure maintained "
                         f"until the /{sound2}/ closure forms. The release burst belongs to /{sound2}/.")
    elif 'stop' in s1_manner:
        mechanisms.append(f"**Stop Release Modification:**\n   "
                         f"The /{sound1}/ closure releases directly into the /{sound2}/ articulation, "
                         f"often showing reduced or absent burst energy.")

    # Manner transitions
    if 'fricative' in s1_manner and 'stop' in s2_manner:
        mechanisms.append(f"**Fricative-to-Stop Transition:**\n   "
                         f"The continuous airflow of /{sound1}/ terminates as the /{sound2}/ closure forms. "
                         f"Listeners perceive a sharp acoustic boundary.")
    elif 'nasal' in s1_manner or 'nasal' in s2_manner:
        mechanisms.append(f"**Nasal Coarticulation:**\n   "
                         f"Velum movement coordinates with oral articulation. Nasal airflow may extend "
                         f"into or anticipate the adjacent segment.")

    # Add one mechanism from the notes if available
    if examples:
        note = examples[0][2]
        if len(mechanisms) < 5:
            mechanisms.append(f"**Specific Adaptation:**\n   {note}")

    return mechanisms[:5]  # Limit to 5 mechanisms

def generate_acoustic_signature(sound1: str, sound2: str) -> List[Tuple[str, str, str]]:
    """Generate acoustic and perceptual signature table."""
    signatures = []

    s1_data = SOUND_DATA.get(sound1, {})
    s2_data = SOUND_DATA.get(sound2, {})
    s1_voicing = s1_data.get('voicing', '')
    s2_voicing = s2_data.get('voicing', '')
    s1_manner = s1_data.get('manner', '')

    # Voicing signatures
    if s1_voicing == s2_voicing == 'voiced':
        signatures.append(('Voicing bar', 'Low-frequency band (~100 Hz) throughout', 'Smooth, connected transition'))
    elif 'voiceless' in s1_voicing:
        signatures.append(('Aspiration/noise', 'High-frequency energy from /%s/' % sound1, 'Clear fricative or burst cue'))

    # Manner signatures
    if 'stop' in s1_manner:
        signatures.append(('Closure gap', 'Silent interval (20-80 ms)', 'Perceived stop identity'))
        signatures.append(('Burst/release', 'Brief high-amplitude transient', 'Place-of-articulation cue'))
    elif 'fricative' in s1_manner:
        signatures.append(('Frication noise', 'Continuous aperiodic energy', 'Distinct fricative quality'))
    elif 'nasal' in s1_manner:
        signatures.append(('Nasal formants', 'Low F1 (~250 Hz), distinct nasal pole', 'Nasal resonance quality'))

    # Formant transitions
    signatures.append(('Formant transitions', 'F2/F3 movement into /%s/' % sound2, 'Place identification cue'))

    return signatures[:4]  # Limit to 4 rows

def generate_practice_drill(phrase: str, ipa: str, sound1: str, sound2: str) -> str:
    """Generate articulatory practice section."""
    words = phrase.split()
    first_word = words[0] if words else phrase
    second_part = ' '.join(words[1:]) if len(words) > 1 else sound2

    return f"""### 4.1 Slow-Motion Drill

1. Say **"{first_word}"** slowly, establishing full /{sound1}/ articulation.
2. Say **"{second_part}"** starting with an isolated /{sound2}/.
3. Merge: *{phrase}* — maintain voicing continuity, minimize release between segments.
4. Record and compare:

   * Over-released: Excessive separation between sounds
   * Balanced: Natural liaison as transcribed `{ipa}`
   * Under-articulated: Loss of primary articulatory cues

### 4.2 Gestural Continuity Exercise

* Focus awareness on active articulators for both /{sound1}/ and /{sound2}/.
* Alternate "{sound1}-{sound2}-{sound1}-{sound2}" while maintaining voicing where applicable.
* Notice the articulatory transition: where does one gesture end and the next begin?
* Perform slowly, then gradually increase speed while preserving clarity.
* The movement should feel **fluid** and **economical**, not **segmented**."""

def generate_broader_insights(sound1: str, sound2: str) -> List[Tuple[str, str, str]]:
    """Generate broader coarticulatory insights table."""
    insights = []

    s1_data = SOUND_DATA.get(sound1, {})
    s2_data = SOUND_DATA.get(sound2, {})
    s1_place = s1_data.get('place', '')
    s2_place = s2_data.get('place', '')
    s1_voicing = s1_data.get('voicing', '')
    s2_voicing = s2_data.get('voicing', '')
    s1_manner = s1_data.get('manner', '')
    s2_manner = s2_data.get('manner', '')

    # Place shift
    if s1_place and s2_place:
        insights.append(('Place shift', f'{s1_place} → {s2_place}', f'/{sound1} {sound2}/, similar front-back transitions'))

    # Voicing pattern
    if s1_voicing and s2_voicing:
        insights.append(('Voicing pattern', f'{s1_voicing} to {s2_voicing}', f'Common in /{sound1} {sound2}/ sequences'))

    # Manner transition
    if s1_manner and s2_manner:
        manner1_short = s1_manner.split()[0]
        manner2_short = s2_manner.split()[0]
        insights.append(('Manner transition', f'{manner1_short} → {manner2_short}', f'Affects timing and release'))

    return insights[:3]

def create_upgraded_page(sound1: str, sound2: str, examples: List[Tuple[str, str, str]]) -> str:
    """Create a fully upgraded exercise page."""

    # Primary example (first one)
    primary_phrase, primary_ipa, primary_note = examples[0]

    # Generate allophonic detail (simplified version)
    allophonic_ipa = primary_ipa.replace('/','[').replace('/',']')

    # Get sound data
    s1_desc = get_sound_description(sound1)
    s2_desc = get_sound_description(sound2)
    s1_data = SOUND_DATA.get(sound1, SOUND_DATA.get('p'))  # fallback
    s2_data = SOUND_DATA.get(sound2, SOUND_DATA.get('p'))

    # Build the page
    content = f"""# Coarticulation Study: /{sound1}/ + /{sound2}/

### Sequence: {s1_desc} → {s2_desc}

### Example Phrase: **{primary_phrase}**

**IPA:** `{primary_ipa}`
**Allophonic detail:** `{allophonic_ipa}`

---

## 1. Segmental Foundations

| Segment | Symbol | Place | Manner | Voicing | Airflow | Duration |
|----------|---------|--------|----------|-----------|-----------|-----------|
| First | /{sound1}/ | {s1_data.get('place', 'N/A')} | {s1_data.get('manner', 'N/A')} | {s1_data.get('voicing', 'N/A')} | {s1_data.get('airflow', 'N/A')} | {s1_data.get('duration', 'variable')} |
| Second | /{sound2}/ | {s2_data.get('place', 'N/A')} | {s2_data.get('manner', 'N/A')} | {s2_data.get('voicing', 'N/A')} | {s2_data.get('airflow', 'N/A')} | {s2_data.get('duration', 'variable')} |

* **/{sound1}/**: {primary_note.split(';')[0] if ';' in primary_note else primary_note}
* **/{sound2}/**: {s2_desc.capitalize()} articulation follows with typical place and manner characteristics.

---

## 2. Coarticulatory Mechanisms

"""

    # Add mechanisms
    mechanisms = generate_coarticulatory_mechanisms(sound1, sound2, examples)
    for i, mech in enumerate(mechanisms, 1):
        content += f"{i}. {mech}\n\n"

    # Add acoustic signature
    content += """---

## 3. Acoustic & Perceptual Signature

| Feature                 | Acoustic Manifestation                      | Perceptual Effect               |
| ----------------------- | ------------------------------------------- | ------------------------------- |
"""

    acoustic_sigs = generate_acoustic_signature(sound1, sound2)
    for feature, acoustic, perceptual in acoustic_sigs:
        content += f"| {feature:<23} | {acoustic:<43} | {perceptual:<31} |\n"

    content += """\n---

## 4. Articulatory Practice

"""

    # Add practice drill
    content += generate_practice_drill(primary_phrase, primary_ipa, sound1, sound2)

    # Add broader insights
    content += """

---

## 5. Broader Coarticulatory Insights

| Type                           | Manifestation                         | Similar Pairs       |
| ------------------------------ | ------------------------------------- | ------------------- |
"""

    broader = generate_broader_insights(sound1, sound2)
    for insight_type, manifestation, similar in broader:
        content += f"| **{insight_type:<28}** | {manifestation:<37} | {similar:<19} |\n"

    # Add summary
    voicing_note = "voiced" if s1_data.get('voicing') == s2_data.get('voicing') == 'voiced' else "mixed-voicing"
    place_note = "cross-place" if s1_data.get('place') != s2_data.get('place') else "homorganic"

    content += f"""

Understanding this combination helps refine articulation for all {place_note} sequences involving {s1_data.get('manner', 'these')} and {s2_data.get('manner', 'these')} manners.

---

## 6. Summary Points

* /{sound1}/ + /{sound2}/ is a **{voicing_note}, {place_note} sequence** showing distinctive coarticulatory patterns.
* The transition exhibits **{mechanisms[0].split(':')[0].strip('*').lower() if mechanisms else 'place and manner coordination'}**.
* Perceptually, listeners rely on **formant transitions and temporal cues** to identify both segments.
* Mastery involves **smooth articulatory flow** while maintaining segment identity.

---

### Practice Sentence Variants

| Phrase | IPA | Note |
| ---------- | ----------------- | -------------------------------------- |
"""

    # Add all examples
    for phrase, ipa, note in examples:
        # Truncate long notes
        note_short = note[:50] + '...' if len(note) > 50 else note
        content += f"| {phrase:<10} | `{ipa:<15}` | {note_short:<38} |\n"

    content += "\n---\n\n*Part of a curated collection of coarticulation studies for American English.*\n"

    return content

def sanitize_filename(sound: str) -> str:
    """Convert IPA symbols to filesystem-safe names."""
    return (sound
            .replace('ʃ', 'sh')
            .replace('ʒ', 'zh')
            .replace('θ', 'th')
            .replace('ð', 'dh')
            .replace('tʃ', 'tsh')
            .replace('dʒ', 'dzh')
            .replace('ŋ', 'ng'))

def main():
    """Upgrade all exercise pages."""
    curated = get_curated_combinations()

    exercises_dir = 'exercises'
    upgraded_count = 0

    print(f"Upgrading {len(curated)} exercise pages to detailed format...")

    for (sound1, sound2), examples in curated.items():
        # Generate filename
        s1_safe = sanitize_filename(sound1)
        s2_safe = sanitize_filename(sound2)
        filename = f"{s1_safe}-{s2_safe}.md"
        filepath = os.path.join(exercises_dir, filename)

        # Generate upgraded content
        content = create_upgraded_page(sound1, sound2, examples)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        upgraded_count += 1

        if upgraded_count % 50 == 0:
            print(f"  Upgraded {upgraded_count}/{len(curated)} pages...")

    print(f"\n✓ Successfully upgraded {upgraded_count} exercise pages!")
    print(f"  Format: Detailed coarticulation studies with 6 sections")
    print(f"  Location: {exercises_dir}/")

if __name__ == '__main__':
    main()
