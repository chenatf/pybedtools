from bedtool import bedtool, set_tempdir, get_tempdir, cleanup
from features import bedfeature

GENOME_REGISTRY = {
'dm3' : {
        'chr2L': (1, 23011544),
        'chr2LHet': (1, 368872),
        'chr2R': (1, 21146708),
        'chr2RHet': (1, 3288761),
        'chr3L': (1, 24543557),
        'chr3LHet': (1, 2555491),
        'chr3R': (1, 27905053),
        'chr3RHet': (1, 2517507),
        'chr4': (1, 1351857),
        'chrM': (1, 19517),
        'chrU': (1, 10049037),
        'chrUextra': (1, 29004656),
        'chrX': (1, 22422827),
        'chrXHet': (1, 204112),
        'chrYHet': (1, 347038)
     },

'hg18': {'chr1': (1, 247249719),
            'chr10': (1, 135374737),
            'chr10_random': (1, 113275),
            'chr11': (1, 134452384),
            'chr11_random': (1, 215294),
            'chr12': (1, 132349534),
            'chr13': (1, 114142980),
            'chr13_random': (1, 186858),
            'chr14': (1, 106368585),
            'chr15': (1, 100338915),
            'chr15_random': (1, 784346),
            'chr16': (1, 88827254),
            'chr16_random': (1, 105485),
            'chr17': (1, 78774742),
            'chr17_random': (1, 2617613),
            'chr18': (1, 76117153),
            'chr18_random': (1, 4262),
            'chr19': (1, 63811651),
            'chr19_random': (1, 301858),
            'chr1_random': (1, 1663265),
            'chr2': (1, 242951149),
            'chr20': (1, 62435964),
            'chr21': (1, 46944323),
            'chr21_random': (1, 1679693),
            'chr22': (1, 49691432),
            'chr22_h2_hap1': (1, 63661),
            'chr22_random': (1, 257318),
            'chr2_random': (1, 185571),
            'chr3': (1, 199501827),
            'chr3_random': (1, 749256),
            'chr4': (1, 191273063),
            'chr4_random': (1, 842648),
            'chr5': (1, 180857866),
            'chr5_h2_hap1': (1, 1794870),
            'chr5_random': (1, 143687),
            'chr6': (1, 170899992),
            'chr6_cox_hap1': (1, 4731698),
            'chr6_qbl_hap2': (1, 4565931),
            'chr6_random': (1, 1875562),
            'chr7': (1, 158821424),
            'chr7_random': (1, 549659),
            'chr8': (1, 146274826),
            'chr8_random': (1, 943810),
            'chr9': (1, 140273252),
            'chr9_random': (1, 1146434),
            'chrM': (1, 16571),
            'chrX': (1, 154913754),
            'chrX_random': (1, 1719168),
            'chrY': (1, 57772954)},
}


