# GC Content Analysis Tool

## Overview

This script is designed for analyzing bacterial genome data to extract GC content as a feature. GC content is the percentage of guanine (G) and cytosine (C) bases in a DNA sequence, which can provide insights into genomic stability, taxonomy, and other biological properties.

This tool also provides a starting point for computational predictions of safety and toxicity based on genomic features and machine learning models. It is modular and can be extended to include other features, such as virulence factors or antimicrobial resistance genes.

## Features

### Data Collection
- Accepts local `.fna` or `.fna.gz` files as input.
- Supports gzipped and uncompressed FASTA formats.

### Feature Extraction
- Calculates the GC content for each genome file provided.
- Outputs the results as a CSV file.

### Machine Learning Extension
- The extracted features can be used as inputs for predictive models like Random Forest classifiers.

### Error Handling
- Handles invalid or empty sequences gracefully.
- Debugging messages are provided to ensure the user can identify and resolve issues.

## Installation

### Prerequisites
- Python 3.8+

### Required Libraries
- biopython
- gzip
- pandas

Install the required libraries using pip:
```bash
pip install biopython pandas
```

## Usage

### Step 1: Prepare Your Data
Ensure your genome files are in `.fna` or `.fna.gz` format.

Example genome assemblies for testing:
- Genome assembly ASM886v2
- Genome assembly ASM584v2

### Step 2: Modify the Script
Replace the placeholder file paths in the `genome_files` list with the paths to your local genome files:
```python
genome_files = ["path_to_your_file1.fna.gz", "path_to_your_file2.fna.gz"]
```

### Step 3: Run the Script
Execute the script:
```bash
python gc_content_analysis.py
```

### Step 4: View the Results
- The extracted GC content values are printed to the console.
- A CSV file (`gc_content_results.csv`) containing the results is saved in the current working directory.

## Output Format

### Console Output
The script provides real-time feedback:
```
Processing file: path_to_your_file1.fna.gz
GC Content for path_to_your_file1.fna.gz: 50.25
...
```

### CSV Output
The output CSV file contains two columns:
- Genome: The name of the genome file.
- GC_Content: The calculated GC content percentage.

Example:
```
Genome,GC_Content
path_to_your_file1.fna.gz,50.25
path_to_your_file2.fna.gz,48.67
```

## Extending the Tool

### (i) Computational Prediction of Safety and Toxicity

**Data Collection:** Use this tool to extract genomic features from bacterial genomes.

**Feature Extraction:** Extend the script to include:
- Virulence factors (e.g., using VFDB).
- Antimicrobial resistance genes (e.g., using CARD).

**Machine Learning Models:** Use extracted features as input to predictive models.

### (ii) Methods and Models
- **Bioinformatics Tools:** Integrate BLAST or other annotation tools to identify safety/toxicity markers.
- **Deep Learning:** For complex data, consider using models like Convolutional Neural Networks (CNNs).

### (iii) Manual Annotation
- Use tools like BLAST to manually annotate important genes.
- Include specific annotations for safety markers or resistance genes in the dataset.

## Known Limitations
- Requires valid `.fna` or `.fna.gz` genome files.
- GC content calculation assumes sequences are properly formatted.
- Annotation features (e.g., virulence factors) are not included in this basic version.

## Support
For issues or questions, contact `shyamalimashreyadas@gmail.com`.

## References
- [Biopython Documentation](https://biopython.org/wiki/Documentation)
- [NCBI Genome Assembly Information](https://www.ncbi.nlm.nih.gov/assembly)
