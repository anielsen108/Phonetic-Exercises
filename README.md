# Phonetic Exercises for American English

This repository contains comprehensive phonetic exercises for mastering American English (General American/Neutral Broadcast English) pronunciation.

## Contents

### Individual Coarticulation Exercise Pages

The `exercises/` directory contains **14,280 individual exercise pages** - one for each possible consonant-to-consonant coarticulation in American English.

**Structure:**
- Each page focuses on ONE specific sound transition (e.g., /nst/ → /ð/)
- Multiple example phrases per combination
- Detailed IPA transcriptions showing coarticulation features
- Articulatory guidance and practice notes
- Examples from both within-word and across-word-boundary contexts

**Coverage:**
- 24 single consonants (stops, fricatives, affricates, nasals, liquids, approximants)
- 96 two-consonant clusters (initial and final positions)
- 30 three-consonant clusters
- **Total: 14,280 unique sound combinations**

[Browse All Combinations →](exercises/README.md)

### Organized Summary Pages

The `coarticulation-exercises/` directory provides summary pages organized by starting sound, offering a quick overview of all combinations for each consonant/cluster.

[View Summary Pages →](coarticulation-exercises/README.md)

## Target Audience

These exercises are designed for:
- **Dialect coaches** and **accent reduction specialists**
- **Speech-language pathologists**
- **Voice actors** and **broadcasters**
- **ESL/EFL teachers and students**
- **Linguistics students** studying phonetics
- Anyone seeking to perfect their American English pronunciation

## About American English Phonetics

These exercises focus on **General American** (GenAm) or **Neutral Broadcast English**, the relatively unmarked accent variety used in:
- Network news broadcasting
- Professional voice-over work
- Standard American film and television
- Most American English language teaching

## How to Use

1. Choose a consonant sound or cluster you want to practice
2. Work through the coarticulation exercises systematically
3. Pay attention to the IPA transcriptions, which show precise articulatory details
4. Practice slowly at first, then gradually increase to natural speaking speed
5. Record yourself to monitor progress

## Contributing

To add more examples or improve exercises:

1. Add example phrases to `coarticulation_examples.py`
2. Run `python3 generate_combination_pages.py` to regenerate shell pages
3. Run `python3 fill_combination_pages.py` to fill pages with examples
4. Submit a pull request

You can also manually edit individual pages in the `exercises/` directory to add better examples for specific sound combinations.

## License

Educational use encouraged. Please attribute when redistributing.

---

*For questions or suggestions, please open an issue.*
