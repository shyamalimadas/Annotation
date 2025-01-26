# GC Content Analysis with KEGG Pathway Annotation

This script analyzes the GC content of genomic sequences and integrates KEGG pathway annotations to provide a comprehensive view of the data. It works with `.fna` genomic files, calculates GC content, visualizes the distribution, and annotates the data with KEGG pathways.

## Prerequisites

Before running the script, ensure that you have the necessary packages installed:

1. **BioPython** - for parsing genomic sequences.
2. **Pandas** - for data manipulation.
3. **Scikit-learn** - for standardization of GC content.
4. **Matplotlib & Seaborn** - for data visualization.
5. **Bioservices** - for KEGG pathway annotation.

You can install the required packages using `pip`:

```bash
pip install biopython pandas scikit-learn matplotlib seaborn bioservices
```

## Input Data

The script requires genomic files in the `.fna` format (FASTA format). These files should be specified in the `genome_files` list.

Example:
```python
genome_files = ["GCF_000005845.2_ASM584v2_genomic.fna", "GCF_000008865.2_ASM886v2_genomic.fna"]
```

You can use `.fna` files in gzip format as well (e.g., `.fna.gz`).

## Steps Overview

### Step 1: Calculate GC Content

The script calculates the GC content for each genome file. The GC content is the percentage of nucleotides in the sequence that are either guanine (G) or cytosine (C).

### Step 2: Normalize GC Content

The GC content is standardized (normalized) to have a mean of 0 and a standard deviation of 1 using `StandardScaler` from `scikit-learn`.

### Step 3: Visualize GC Content

The distribution of GC content across the genomes is visualized using `matplotlib` and `seaborn` as a histogram with a KDE (Kernel Density Estimate) curve.

### Step 4: KEGG Pathway Annotation

The script integrates KEGG annotations by fetching pathway data for each genome using the KEGG API (`bioservices`). The pathway data is then added to the DataFrame.

### Step 5: Save Results

The results (GC content and KEGG annotations) are saved to a CSV file named `gc_content_with_kegg.csv`.

## Usage

1. Place your `.fna` files in the same directory as this script or provide the correct path in the `genome_files` list.
2. Run the script:
    ```bash
    python gc_content_kegg_analysis.py
    ```

3. The script will output:
    - The normalized GC content for each genome.
    - A visualization of the GC content distribution.
    - A CSV file containing the GC content and KEGG annotations: `gc_content_with_kegg.csv`.

### Example Output Files:
- `gc_content_results3.csv`: Contains GC content values for each genome.
- `gc_content_with_kegg.csv`: Contains GC content and KEGG annotations for each genome.

## Example Output (CSV)

`gc_content_results3.csv`:
```
Genome,GC_Content,GC_Content_Normalized
GCF_000005845.2_ASM584v2_genomic.fna,50.5,0.12
GCF_000008865.2_ASM886v2_genomic.fna,47.3,-0.67
```

`gc_content_with_kegg.csv`:
```
Genome,GC_Content,GC_Content_Normalized,KEGG_Annotations
GCF_000005845.2_ASM584v2_genomic.fna,50.5,0.12,"Pathway 1, Pathway 2"
GCF_000008865.2_ASM886v2_genomic.fna,47.3,-0.67,"Pathway 3, Pathway 4"
```

## Notes

- The KEGG annotation part requires a valid connection to the KEGG API and proper mapping of genome identifiers to KEGG-compatible IDs. In this example, `hsa` is used as a placeholder (for human genomes). You'll need to adapt the logic to map your genomic files to KEGG IDs.
- The script assumes the genome files are in FASTA format. If you encounter any issues with file formats, check that your files are properly formatted.

## Future Enhancements

- **Automated Genome ID Mapping**: The mapping from genomic file names to KEGG IDs could be enhanced to support more genomes automatically.
- **Expanded Data Analysis**: The script can be extended to analyze additional genomic features, such as nucleotide composition, gene count, and more.
- **Pathway Visualization**: Integrating a method to visualize the KEGG pathways could be a future addition, providing a graphical representation of the biological pathways.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
