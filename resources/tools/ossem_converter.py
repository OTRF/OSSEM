#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__ = 'OSSEM Converter'
__author__  = 'Ricardo Dias @hxnoyd'
__version__ = "0.1.0"

import os
import yaml
import mistune
import argparse
from natsort import natsorted
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

class ossemParser():
    def __init__(self):
        self.cim_entities = []
        self.cim_entities_indexes = []
        self.cim_ignore = ['domain_or_hostname_or_fqdn.md']
        self.data_dictionaries = []
        self.data_dictionaries_indexes = []
        self.data_dictionaries_ignore = []
        self.ddm_list = []
        self.ddm_list_indexes = []
        self.ds_list = []
        self.ds_list_indexes = []

    def remove_new_lines(self, text):
        if text:
            return text.replace('\n',' ')
        else:
            return text

    def read_yml(self, context, root_path, file_path):
        """ read a yaml file and return dict """
        rootpath = root_path[:root_path.index(context)+1]
        filepath = root_path[root_path.index(context)+1:]
        try:
            yml_file = yaml.load(open(file_path, 'r'), Loader=yaml.Loader)
            filename = file_path.split('/')[-1].split('.')[0]
        except Exception as e:
            print('[!] Failed parsing', file_path)
            return None

        if not yml_file:
            print('[!] Failed parsing {}'.format(file_path))
            return None
        else:
            yml_file['rootpath'] = '/'.join(rootpath)
            yml_file['filepath'] = '/'.join(filepath)
            yml_file['filename'] = filename
            return yml_file

    def parse_yaml(self, path):
        """ parse ossem yaml data """

        cim = 'common_information_model'
        dd = 'data_dictionaries'
        ddm = 'detection_data_model'
        ds = 'attack_data_sources'

        for root, dirs, files in os.walk(path):
            for name in files:
                filepath = root + os.sep + name
                path = root.split('/')

                #parse yaml event files
                if name.endswith('.yml') and 'README' not in name:
                    if cim in path and name not in self.cim_ignore:
                        yml_data = self.read_yml(cim, path, filepath)
                        if yml_data:
                            self.cim_entities.append(yml_data)

                    elif dd in path:
                        yml_data = self.read_yml(dd, path, filepath)
                        if yml_data:
                            self.data_dictionaries.append(yml_data)

                    elif ddm in path:
                        yml_data = self.read_yml(ddm, path, filepath)
                        if yml_data:
                            self.ddm_list.append(yml_data)

                    elif ds in path:
                        yml_data = self.read_yml(ds, path, filepath)
                        if yml_data:
                            self.ds_list.append(yml_data)

                #parse yaml index files
                elif name == 'README.yml':
                    if cim in path:
                        yml_data = self.read_yml(cim, path, filepath)
                        if yml_data:
                            self.cim_entities_indexes.append(yml_data)

                    elif dd in path:
                        yml_data = self.read_yml(dd, path, filepath)
                        if yml_data:
                            self.data_dictionaries_indexes.append(yml_data)

                    elif ddm in path:
                        yml_data = self.read_yml(ddm, path, filepath)
                        if yml_data:
                            self.ddm_list_indexes.append(yml_data)

                    elif ds in path:
                        yml_data = self.read_yml(ds, path, filepath)
                        if yml_data:
                            self.ds_list_indexes.append(yml_data)

    def write_yml(self, root, filename, entry):
        """ writes yml file """
        context = entry['rootpath'].split('/')[-1]
        yml_path = os.path.join(root, context, entry['filepath'])

        #create fullpath if needed
        if not os.path.exists(yml_path):
            os.makedirs(yml_path)

        filepath = os.path.join(yml_path, filename)

        #remove temporary fields
        entry.pop('rootpath')
        entry.pop('filepath')
        entry.pop('filename')

        dd_yaml_file = open(filepath, 'w')
        dd_yaml_file.write(yaml.dump(entry, sort_keys=False))
        dd_yaml_file.close()
        print('[*] Created {}'.format(filepath))

    def export_to_yaml(self, root):
        """ generates a yaml version of OSSEM data """

        #generate data dictionary event yaml
        for entry in self.data_dictionaries:
            filename = '{}.yml'.format(entry['filename'])
            self.write_yml(root, filename, entry)

        #generate data dictionary index yaml
        for entry in self.data_dictionaries_indexes:
            filename = 'README.yml'
            self.write_yml(root, filename, entry)

        #generate cim entities yaml
        for entry in self.cim_entities:
            filename = '{}.yml'.format(entry['filename'])
            self.write_yml(root, filename, entry)

        #generate cim entities index yaml
        for entry in self.cim_entities_indexes:
            filename = 'README.yml'
            self.write_yml(root, filename, entry)

        #generate ddm tables yaml
        for entry in self.ddm_list:
            filename = '{}.yml'.format(entry['filename'])
            self.write_yml(root, filename, entry)

        #generate ddm tables index yaml
        for entry in self.ddm_list_indexes:
            filename = 'README.yml'
            self.write_yml(root, filename, entry)

        #generate ds tables yaml
        for entry in self.ds_list:
            filename = '{}.yml'.format(entry['filename'])
            self.write_yml(root, filename, entry)

        #generate ds tables index yaml
        for entry in self.ds_list_indexes:
            filename = 'README.yml'
            self.write_yml(root, filename, entry)

        return True

    def write_markdown(self, root, entry, template, entry_type=False):
        context = entry['rootpath'].split('/')[-1]
        md_path = os.path.join(root, context, entry['filepath'])
        root_path = entry['rootpath']
        sub_data_sets = []

        #create fullpath if needed
        if not os.path.exists(md_path):
            os.makedirs(md_path)

        #enrich markdown with sub data set
        if entry_type:
            md_file_path = os.path.join(md_path, 'README.md')
            for item in sorted(os.listdir(os.path.join(root_path, entry['filepath']))):
                if os.path.isdir(os.path.join(root_path, entry['filepath'], item)):

                    #indexes poiting to events
                    if item == entry_type:
                        entry['data_set_type'] = item #TODO: capitalize
                        events_root_path = os.path.join(root_path, entry['filepath'], item)
                        for event in natsorted(os.listdir(events_root_path)):
                            if event.endswith('.yml'):
                                event_file_path = os.path.join(events_root_path, event)
                                try:
                                    readme = yaml.load(open(event_file_path, 'r'), Loader=yaml.Loader)
                                    if readme:
                                        sub_data_sets.append({
                                            'title': readme['event_code'] if 'event_code' in readme else readme['title'],
                                            'link': '{}/{}.md'.format(item, event.split('.')[0]),
                                            'description': self.remove_new_lines(readme['description']),
                                            'tags': readme['tags']})
                                except Exception as e:
                                    print('[!] Failed parsing', event_file_path)

                    #indexes pointing to other indexes
                    else:
                        entry['data_set_type'] = 'Data Set'
                        index_root_path = os.path.join(root_path, entry['filepath'], item, 'readme.yml')
                        readme = yaml.load(open(index_root_path, 'r'), Loader=yaml.Loader)
                        if readme:
                            if readme['description']:
                                desc = '{}.'.format(readme['description'].split('.')[0])
                            else:
                                desc = readme['description']
                            sub_data_sets.append({
                                'title': readme['title'],
                                'link': '{}/'.format(item),
                                'description': desc})
        else:
            filename = '{}.md'.format(entry['filename'])
            md_file_path = os.path.join(md_path, filename)

        entry['sub_data_sets'] = sub_data_sets

        with open(md_file_path, 'w') as md:
            md.write(template.render(entry=entry))

        print('[*] Created {}'.format(md_file_path))

    def export_to_markdown(self, root):
        env = Environment(loader=FileSystemLoader('templates/'))
        readme_template = env.get_template('readme_template.md')
        dds_template = env.get_template('data_dictionary_template.md')
        cim_template = env.get_template('cim_entity_template.md')
        ddm_template = env.get_template('ddm_relationships_template.md')
        ds_template = env.get_template('attack_ds_template.md')

        #generate data dictionary event markdown
        for entry in self.data_dictionaries:
            self.write_markdown(root, entry, dds_template)

        # generate data dictionary index markdown
        for entry in self.data_dictionaries_indexes:
            self.write_markdown(root, entry, readme_template, 'events')

        #generate common information model markdown
        for entry in self.cim_entities:
            self.write_markdown(root, entry, cim_template)

        # generate cim index markdown
        for entry in self.cim_entities_indexes:
            self.write_markdown(root, entry, readme_template, 'entities')

        #generate detection data model markdown
        for entry in self.ddm_list:
            self.write_markdown(root, entry, ddm_template)

        #generate detection data model index markdown
        for entry in self.ddm_list_indexes:
            self.write_markdown(root, entry, readme_template, 'tables')

        #generate attack data sources markdown
        for entry in self.ds_list:
            self.write_markdown(root, entry, ds_template)

        #generate attack data sources index markdown
        for entry in self.ds_list_indexes:
            self.write_markdown(root, entry, readme_template, 'tables')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tool to convert OSSEM data')
    #parser.add_argument('--from-md', 
    #    help='path to import OSSEM markdown data from')
    parser.add_argument('--from-yml',
        help='path to import OSSEM yaml data from')
    parser.add_argument('--to-md',
        help='path to export OSSEM markdown data')
    #parser.add_argument('--to-yml',
    #    help='path to export OSSEM yaml data')

    args = parser.parse_args()
    ossem = ossemParser()

    if not args.to_md:
        print('[!] You forgot to select an output. Check the available output arguments with --help.')

    if args.to_md:
        if not args.from_yml:
            print('[!] You can only export to Markdown from YAML')
        else:
            print('[*] Parsing OSSEM from YAML')
            ossem.parse_yaml(args.from_yml)
            print('[*] Exporting OSSEM to Markdown')
            ossem.export_to_markdown(args.to_md)