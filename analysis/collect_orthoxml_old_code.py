
import xml.etree.ElementTree as ET
import dill as dill_pickle
from os import listdir
from xml.dom import minidom
import os

print("started ")
working_folder = "/work/FAC/FBM/DBC/cdessim2/default/smajidi1/fastget/qfo2/ali_code_31aug/"
# gene_trees_folder = ""  # working_folder + "/gene_trees_/"
# check gene_trees_folder exist otherwise mkdir this

#address_rhogs_folder = working_folder + "/rhog_g501_done/"  # old3/rhog_all/ /rhog_size_g2_s500/" sample_rootHOG
#species_tree_address = working_folder + "/archive/lineage_tree_qfo.phyloxml"
pickle_folder = working_folder + "/pickle_2sep5pm/"
# add warning when pickle folder is not empty
output_xml_name = "out_ali_2sep5pm_test.xml"
gene_id_pickle_file = working_folder + "group_xml_ortho_adjusted_family_40_2sep5pm.pickle"

#
# orthoxml_file = ET.Element("orthoXML", attrib={"xmlns": "http://orthoXML.org/2011/", "origin": "OMA",
#                                                "originVersion": "Nov 2021", "version": "0.3"})  #

if os.path.getsize(gene_id_pickle_file) > 0:
    with open(gene_id_pickle_file, 'rb') as handle:
        (groups_xml, gene_id_name, orthoxml_file) = dill_pickle.load(handle)
    # gene_id_name[query_species_name] = (gene_idx_integer, query_prot_name)
print("gene_id_name read ")

#
#
# for query_species_name, list_prots in gene_id_name.items():
#
#     species_xml = ET.SubElement(orthoxml_file, "species", attrib={"name": query_species_name, "NCBITaxId": "1"})
#     database_xml = ET.SubElement(species_xml, "database", attrib={"name": "QFO database ", "version": "2020"})
#     genes_xml = ET.SubElement(database_xml, "genes")
#
#     for (gene_idx_integer, query_prot_name) in list_prots:
#         query_prot_name_pure = query_prot_name.split("||")[0].strip().split("|")[1]
#         gene_xml = ET.SubElement(genes_xml, "gene", attrib={"id": str(gene_idx_integer), "protId": query_prot_name_pure})

print("gene_xml created ")
pickle_files_adress = listdir(pickle_folder)
print("number of hog is", len(pickle_files_adress))
hogs_a_rhog_xml_all = []
for pickle_file_adress in pickle_files_adress:
    if os.path.getsize(pickle_folder + pickle_file_adress) > 0:
        with open(pickle_folder + pickle_file_adress, 'rb') as handle:
            hogs_a_rhog_xml_batch = dill_pickle.load(handle)  # hogs_a_rhog_xml_batch is orthoxml_to_newick.py list of hog object.
            hogs_a_rhog_xml_all.extend(hogs_a_rhog_xml_batch)
    else:
        print("empty ", pickle_file_adress)
        # hogs_rhogs_xml_all is orthoxml_to_newick.py list of hog object.

print("after reading number of hogs is  ", len(hogs_a_rhog_xml_all))
# orthoxml_file2 = ET.Element("orthoXML", attrib={"xmlns": "http://orthoXML.org/2011/", "origin": "OMA",
#                                                "originVersion": "Nov 2021", "version": "0.3"})  #

# groups_xml2 = ET.SubElement(orthoxml_file2, "groups")

for hogs_a_rhog_xml in hogs_a_rhog_xml_all:
    groups_xml.append(hogs_a_rhog_xml)

#xml_str = minidom.parseString(ET.tostring(orthoxml_file)).toprettyxml(indent="   ")
xml_str = minidom.parseString(ET.tostring(orthoxml_file)).toprettyxml(indent="   ")
# print(xml_str[:-1000])

with open(working_folder +output_xml_name, "w") as file_xml:
    file_xml.write(xml_str)
file_xml.close()

print("orthoxml is written in  "+ working_folder +output_xml_name)



