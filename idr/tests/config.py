global organism, idr_base_url, hostname, username, taxonomy_id, endsemble_id, gene_symbol
organism = 'Homo Sapiens'
idr_base_url = 'http://idr.openmicroscopy.org'
hostname = str(idr_base_url[idr_base_url.index('//')+2:])
username = 'public'
password = 'public'
taxonomy_id = '9606'
endsemble_id = 'ENSG00000106526'
gene_symbol = 'ACTR3C'
go_gene_list = ['SOD1', 'SOD2', 'SO']