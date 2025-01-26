from Bio import SeqIO
import gzip
import pandas as pd

# Step 1: Specify your local .fna files
# Replace with the paths to your local files
genome_files = ["GCF_000005845.2_ASM584v2_genomic.fna", "GCF_000008865.2_ASM886v2_genomic.fna"]

# Debug: Check if files are provided
if not genome_files:
    print("No genome files provided. Please specify your local .fna files.")
    exit()

# Step 2: Function to calculate GC content
def calculate_gc_content(genome_file):
    """
    Calculate the GC content of a genome file.
    Handles .fna.gz and .fna formats.
    """
    try:
        # Determine if the file is gzipped
        if genome_file.endswith(".gz"):
            open_func = gzip.open
        else:
            open_func = open

        # Parse the genome file
        with open_func(genome_file, "rt") as f:
            gc_values = []
            for record in SeqIO.parse(f, "fasta"):
                seq = record.seq
                if len(seq) == 0:
                    continue  # Skip empty sequences
                gc_content = 100.0 * (seq.count("G") + seq.count("C")) / len(seq)
                gc_values.append(gc_content)

        # Return the average GC content for the genome
        if gc_values:
            return sum(gc_values) / len(gc_values)
        else:
            print(f"No valid sequences found in {genome_file}.")
            return None

    except Exception as e:
        print(f"Error processing file {genome_fisle}: {e}")
        return None

# Step 3: Extract GC content for each genome
features = []
for file in genome_files:
    print(f"Processing file: {file}")
    gc_content = calculate_gc_content(file)
    if gc_content is not None:
        features.append({"Genome": file, "GC_Content": gc_content})
        print(f"GC Content for {file}: {gc_content}")
    else:
        print(f"Failed to calculate GC content for {file}")

# Debug: Check if any features were extracted
if not features:
    print("No features extracted. Please check your data.")
    exit()

# Step 4: Create a DataFrame
data = pd.DataFrame(features)
print("Extracted Features:")
print(data)

# Optional: Save the results to a CSV file
data.to_csv("gc_content_results.csv", index=False)
print("Results saved to gc_content_results.csv.")
