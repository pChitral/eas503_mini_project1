from mini_project1 import format_data, determine_data_type_of_info_fields


data = [{'CHROM': '4',
         'POS': '123416186',
         'ID': '.',
         'REF': 'A',
         'ALT': 'G',
         'QUAL': '23.25',
         'FILTER': 'PASS',
         'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
         'SAMPLE': {'XG102': {'GT': '0/1',
                              'AD': '51,8',
                              'DP': '59',
                              'GQ': '32',
                              'PL': '32,0,1388'},
                    'XG103': {'GT': '0/0',
                              'AD': '47,0',
                              'DP': '47',
                              'GQ': '99',
                              'PL': '0,114,1353'},
                    'XG104': {'GT': '0/0',
                              'AD': '74,0',
                              'DP': '74',
                              'GQ': '51',
                              'PL': '0,51,1827'},
                    'XG202': {'GT': '0/1',
                              'AD': '51,8',
                              'DP': '59',
                              'GQ': '32',
                              'PL': '32,0,1388'},
                    'XG203': {'GT': '0/0',
                              'AD': '47,0',
                              'DP': '47',
                              'GQ': '99',
                              'PL': '0,114,1353'},
                    'XG204': {'GT': '0/0',
                              'AD': '74,0',
                              'DP': '74',
                              'GQ': '51',
                              'PL': '0,51,1827'},
                    'XG302': {'GT': '0/1',
                              'AD': '51,8',
                              'DP': '59',
                              'GQ': '32',
                              'PL': '32,0,1388'},
                    'XG303': {'GT': '0/0',
                              'AD': '47,0',
                              'DP': '47',
                              'GQ': '99',
                              'PL': '0,114,1353'},
                    'XG304': {'GT': '0/0',
                              'AD': '74,0',
                              'DP': '74',
                              'GQ': '51',
                              'PL': '0,51,1827'},
                    'XG402': {'GT': '0/1',
                              'AD': '51,8',
                              'DP': '59',
                              'GQ': '32',
                              'PL': '32,0,1388'},
                    'XG403': {'GT': '0/0',
                              'AD': '47,0',
                              'DP': '47',
                              'GQ': '99',
                              'PL': '0,114,1353'},
                    'XG404': {'GT': '0/0',
                              'AD': '74,0',
                              'DP': '74',
                              'GQ': '51',
                              'PL': '0,51,1827'}}},
        {'CHROM': '12',
         'POS': '81444551',
         'ID': 'rs10746177',
         'REF': 'T',
         'ALT': 'C',
         'QUAL': '5022.69',
         'FILTER': 'PASS',
         'INFO': 'AC=6;AF=1;AN=6;DP=185;ExcessHet=3.0103;FS=0;MLEAC=6;MLEAF=1;MQ=59.95;QD=27.3;SOR=1.042;VQSLOD=4.51;culprit=QD;DB;POSITIVE_TRAIN_SITE;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=LIN7A,ACSS3;GeneDetail.refGene=dist=112857,dist=27258;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intronic;Gene.ensGene=ENSG00000111058;GeneDetail.ensGene=.;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=12q21.31;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=0.9998;1000g2015aug_afr=0.9992;1000g2015aug_amr=1;1000g2015aug_eur=1;1000g2015aug_sas=1;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=rs10746177;avsnp150=rs10746177;CADD13_RawScore=-0.101662;CADD13_PHRED=1.718;Eigen=-0.4730;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.9988;gnomAD_genome_AFR=0.9961;gnomAD_genome_AMR=1;gnomAD_genome_ASJ=1;gnomAD_genome_EAS=1;gnomAD_genome_FIN=1;gnomAD_genome_NFE=0.9998;gnomAD_genome_OTH=1;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=0.953358;Kaviar_AC=24814;Kaviar_AN=26028;ALLELE_END',
         'SAMPLE': {'XG102': {'GT': '1/1',
                              'AD': '0,72',
                              'DP': '72',
                              'GQ': '99',
                              'PL': '1905,214,0'},
                    'XG103': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1568,168,0'},
                    'XG104': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1563,168,0'},
                    'XG202': {'GT': '1/1',
                              'AD': '0,72',
                              'DP': '72',
                              'GQ': '99',
                              'PL': '1905,214,0'},
                    'XG203': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1568,168,0'},
                    'XG204': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1563,168,0'},
                    'XG302': {'GT': '1/1',
                              'AD': '0,72',
                              'DP': '72',
                              'GQ': '99',
                              'PL': '1905,214,0'},
                    'XG303': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1568,168,0'},
                    'XG304': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1563,168,0'},
                    'XG402': {'GT': '1/1',
                              'AD': '0,72',
                              'DP': '72',
                              'GQ': '99',
                              'PL': '1905,214,0'},
                    'XG403': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1568,168,0'},
                    'XG404': {'GT': '1/1',
                              'AD': '0,56',
                              'DP': '56',
                              'GQ': '99',
                              'PL': '1563,168,0'}}}]
input_to_det_dt_of_info =  {'AC': ['1', '6'], 'AF': ['0.167', '1'], 'AN': ['6'], 'BaseQRankSum': ['-2.542'], 'ClippingRankSum': ['0'], 'DP': ['180', '185'], 'ExcessHet': ['3.0103'], 'FS': ['0'], 'MLEAC': ['1', '6'], 'MLEAF': ['0.167', '1'], 'MQ': ['52.77', '59.95'], 'MQRankSum': ['-4.631'], 'QD': ['0.39', '27.3'], 'ReadPosRankSum': ['1.45'], 'SOR': ['0.758', '1.042'], 'VQSLOD': ['-8.209', '4.51'], 'culprit': ['MQ', 'QD'], 'ANNOVAR_DATE': ['2018-04-16'], 'Func.refGene': ['intergenic'], 'Gene.refGene': ['IL2,IL21', 'LIN7A,ACSS3'], 'GeneDetail.refGene': ['dist=38536,dist=117597', 'dist=112857,dist=27258'], 'Func.ensGene': ['intergenic', 'intronic'], 'Gene.ensGene': ['ENSG00000109471,ENSG00000138684', 'ENSG00000111058'], 'GeneDetail.ensGene': [
            'dist=38306,dist=117597'], 'cytoBand': ['4q27', '12q21.31'], 'CADD13_RawScore': ['0.015973', '-0.101662'], 'CADD13_PHRED': ['2.741', '1.718'], 'Eigen': ['-0.3239', '-0.4730'], 'gnomAD_genome_ALL': ['0.0003', '0.9988'], 'gnomAD_genome_AFR': ['0.0001', '0.9961'], 'gnomAD_genome_AMR': ['0', '1'], 'gnomAD_genome_ASJ': ['0', '1'], 'gnomAD_genome_EAS': ['0.0007', '1'], 'gnomAD_genome_FIN': ['0.0009', '1'], 'gnomAD_genome_NFE': ['0.0002', '0.9998'], 'gnomAD_genome_OTH': ['0.0011', '1'], '1000g2015aug_all': ['0.9998'], '1000g2015aug_afr': ['0.9992'], '1000g2015aug_amr': ['1'], '1000g2015aug_eur': ['1'], '1000g2015aug_sas': ['1'], 'snp138NonFlagged': ['rs10746177'], 'avsnp150': ['rs10746177'], 'Kaviar_AF': ['0.953358'], 'Kaviar_AC': ['24814'], 'Kaviar_AN': ['26028']}
info_field_data_type = determine_data_type_of_info_fields(input_to_det_dt_of_info)

format_data(data, info_field_data_type)
