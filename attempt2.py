from Bio import SeqIO
import gzip
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Specify your local .fna files
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
        print(f"Error processing file {genome_file}: {e}")
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

# Step 5: Normalize GC content (Standardization)
def normalize_gc_content(dataframe):
    """
    Normalize the GC content values using StandardScaler.
    """
    scaler = StandardScaler()
    dataframe["GC_Content_Normalized"] = scaler.fit_transform(dataframe[["GC_Content"]])
    return dataframe

# Apply normalization
data = normalize_gc_content(data)

# Step 6: Visualize the GC content distribution
def plot_gc_content(dataframe):
    """
    Plot GC content distribution to understand data better.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(dataframe["GC_Content"], kde=True, color="blue", bins=15)
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Frequency")
    plt.show()

# Plot GC content
plot_gc_content(data)

# Step 7: Optional - Save the results to a CSV file
data.to_csv("gc_content_results2.csv", index=False)
print("Results saved to gc_content_results2.csv.")

# Future Integration: Annotation using Bioinformatics Tools
# Example of potential integration (pseudo-code, assuming proper setup)
# from kegg import KeggAPI

# def annotate_with_kegg(dataframe):
#     """
#     Example function to integrate KEGG pathway annotations
#     """
#     kegg_annotations = []
#     for genome in dataframe["Genome"]:
#         kegg_result = KeggAPI.get_pathways(genome)
#         kegg_annotations.append(kegg_result)
#     dataframe["KEGG_Annotations"] = kegg_annotations
#     return dataframe
