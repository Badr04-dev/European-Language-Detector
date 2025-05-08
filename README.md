# 🌍 Language Detection for European Languages

![Language Detection](https://img.shields.io/badge/Language-Python-blue.svg)

This project implements a robust language detection system for European languages using **n-gram analysis** and **cosine similarity**. It processes text input to identify the language of each phrase with high accuracy, leveraging text preprocessing and optimization techniques like caching for efficiency.

---

## 📖 Project Overview

The goal of this project is to detect the language of text phrases by comparing their n-gram profiles to precomputed language models. Two versions of the program were developed:

- **`language_detection.py`**: A baseline implementation without caching, taking **52 seconds** to process the test dataset.
- **`language_detection3.py`**: An optimized version with disk and memory caching, reducing execution time to **9.7 seconds** (a **5.36x speedup**).

### Key Features
- **Text Preprocessing**: Normalizes text by removing accents, numbers, and punctuation.
- **N-gram Extraction**: Uses trigrams (n=3) with filtering of frequent words to reduce bias.
- **Two-Phase Detection**: Combines a fast initial filtering with precise cosine similarity for efficient language identification.
- **Caching**: Optimizes performance by storing precomputed n-grams and frequent words.
- **Accuracy**: Achieves **100% accuracy** on `dev.txt` and **82% accuracy** on `test.txt`.

### Performance Highlights
- **Without Cache**: 52 seconds per execution.
- **With Cache**: 9.7 seconds after the initial run (first run builds the cache).
- **Accuracy**: Perfect detection on development data and strong performance on test data.

---

## 🚀 How to Run the Project

Follow these steps to execute the language detection program:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/language-detection.git
cd language-detection
```

### 2. Prepare the Data
Ensure the following structure in your project directory:
```
language-detection/
├── TAL/
│   ├── language_files2
│   ├── language_detection.py
│   ├── language_detection3.py
│   ├── test.txt 
│   └── ...
├── dataset-european/
│   ├── baseline.py
│   ├── dev-predict.py
│   ├── eval.py   
├── langidTest.py
├── langidTest2.py
└── README.md
```

### 3. Install Dependencies
Create a `requirements.txt` file with minimal dependencies (standard library modules are sufficient here) and install:
```bash
pip install -r requirements.txt
```

### 4. Run the Program
You can run either version of the program:

- **Without Caching**:
  ```bash
  python language_detection.py
  ```
  Expected runtime: ~52 seconds.

- **With Caching**:
  ```bash
  python language_detection3.py
  ```
  Expected runtime: ~9.7 seconds (after cache is built).

### 5. Check Outputs
- If `test2.txt` contains phrases with `??` as the language, the program updates the file with detected languages.
- For `language_detection.py`, results for known languages are printed to the console.
- Execution times and progress are displayed during runtime.

---

## 📊 Results

The project demonstrates both accuracy and efficiency:
- **Accuracy**:
  - `dev.txt`: **100%** correct language detection.
  - `test.txt`: **82%** correct language detection, reflecting robust handling of varied inputs.
- **Performance**:
  - Baseline (`language_detection.py`): 52 seconds.
  - Optimized (`language_detection3.py`): 9.7 seconds with caching, showcasing the power of optimization.

---

## 🧠 Technical Details

The detection pipeline involves:
1. **Preprocessing**: Text normalization to focus on linguistic patterns.
2. **N-gram Generation**: Trigrams are extracted, excluding frequent words to avoid bias.
3. **Language Models**: Precomputed n-gram profiles for each language.
4. **Detection**: A two-phase approach (fast filtering + cosine similarity) identifies the closest language match.
5. **Caching**: Disk-based (`pickle`) and memory-based (`@lru_cache`) caching in `language_detection3.py` for speed.

The caching mechanism significantly reduces redundant computations, making the optimized version ideal for repeated executions.

---

## 📝 Future Improvements

- **Support for More Languages**: Extend to non-European languages.
- **Dynamic N-gram Size**: Allow configurable n-gram lengths for different use cases.
- **Parallel Processing**: Use multiprocessing to further speed up large-scale detection.
- **Model Compression**: Reduce memory usage for language models.

---

## 🙌 Acknowledgments

This project was developed to explore language detection techniques and the impact of caching on performance. It draws inspiration from statistical NLP methods and modern optimization practices.

For questions or contributions, please contact motaimbadr@gmail.com !

---
