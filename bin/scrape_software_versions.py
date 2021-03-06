#!/usr/bin/env python
from __future__ import print_function
from collections import OrderedDict
import re

regexes = {
    'AlleleCount': ['v_allelecount.txt', r"(\S+)"],
    'ASCAT': ['v_ascat.txt', r"Version:       (\S+)"],
    'bcftools': ['v_bcftools.txt', r"bcftools (\S+)"],
    'BWA': ['v_bwa.txt', r"Version: (\S+)"],
    'FastQC': ['v_fastqc.txt', r"FastQC v(\S+)"],
    'FreeBayes': ['v_freebayes.txt', r"version:  v(\d\.\d\.\d+)"],
    'GATK': ['v_gatk.txt', r"Version:(\S+)"],
    'htslib': ['v_samtools.txt', r"htslib (\S+)"],
    'Manta': ['v_manta.txt', r"([0-9.]+)"],
    'MultiQC': ['v_multiqc.txt', r"multiqc, version (\S+)"],
    'Nextflow': ['v_nextflow.txt', r"(\S+)"],
    'nf-core/sarek': ['v_pipeline.txt', r"(\S+)"],
    'Qualimap': ['v_qualimap.txt', r"QualiMap v.(\S+)"],
    'R': ['v_r.txt', r"R version (\S+)"],
    'samtools': ['v_samtools.txt', r"samtools (\S+)"],
    'SnpEff': ['v_snpeff.txt', r"version SnpEff (\S+)"],
    'Strelka': ['v_strelka.txt', r"([0-9.]+)"],
    'TIDDIT': ['v_tiddit.txt', r"TIDDIT-(\S+)"], 
    'vcftools': ['v_vcftools.txt', r"([0-9.]+)"],
    'VEP': ['v_vep.txt', r"ensembl-vep          : (\S+)"],
}
results = OrderedDict()
results['nf-core/sarek'] = '<span style="color:#999999;\">N/A</span>'
results['Nextflow'] = '<span style="color:#999999;\">N/A</span>'
results['AlleleCount'] = '<span style="color:#999999;\">N/A</span>'
results['ASCAT'] = '<span style="color:#999999;\">N/A</span>'
results['bcftools'] = '<span style="color:#999999;\">N/A</span>'
results['BWA'] = '<span style="color:#999999;\">N/A</span>'
results['FastQC'] = '<span style="color:#999999;\">N/A</span>'
results['FreeBayes'] = '<span style="color:#999999;\">N/A</span>'
results['GATK'] = '<span style="color:#999999;\">N/A</span>'
results['htslib'] = '<span style="color:#999999;\">N/A</span>'
results['Manta'] = '<span style="color:#999999;\">N/A</span>'
results['MultiQC'] = '<span style="color:#999999;\">N/A</span>'
results['Qualimap'] = '<span style="color:#999999;\">N/A</span>'
results['R'] = '<span style="color:#999999;\">N/A</span>'
results['samtools'] = '<span style="color:#999999;\">N/A</span>'
results['SnpEff'] = '<span style="color:#999999;\">N/A</span>'
results['Strelka'] = '<span style="color:#999999;\">N/A</span>'
results['TIDDIT'] = '<span style="color:#999999;\">N/A</span>' 
results['vcftools'] = '<span style="color:#999999;\">N/A</span>'
results['VEP'] = '<span style="color:#999999;\">N/A</span>'

# Search each file using its regex
for k, v in regexes.items():
    with open(v[0]) as x:
        versions = x.read()
        match = re.search(v[1], versions)
        if match:
            results[k] = "v{}".format(match.group(1))

# Remove software set to false in results
for k in results:
    if not results[k]:
        del(results[k])

# Dump to YAML
print ('''
id: 'software_versions'
section_name: 'nf-core/sarek software versions'
section_href: 'https://github.com/nf-core/sarek'
plot_type: 'html'
description: 'are collected at run time from the software output.'
data: |
    <dl class="dl-horizontal">
''')
for k,v in results.items():
    print("        <dt>{}</dt><dd><samp>{}</samp></dd>".format(k,v))
print ("    </dl>")

# Write out regexes as csv file:
with open('software_versions.csv', 'w') as f:
    for k,v in results.items():
        f.write("{}\t{}\n".format(k,v))
