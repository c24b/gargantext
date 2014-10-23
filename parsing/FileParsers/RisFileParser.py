from django.db import transaction
from parsing.FileParsers.FileParser import FileParser


class RisFileParser(FileParser):
    
    _parameters = {
    }
    
    def _parse(self, parentNode, file):
        metadata = {}
        last_key = None
        last_values = []
        with transaction.atomic():
            for line in self._file:
                if len(line) > 2:
                    parameter_key = line[:2]
                    if parameter_key != b'  ' and parameter_key != last_key:
                        if last_key in self._parameters:
                            parameter = self._parameters[last_key]
                            if parameter["type"] == "metadata":
                                separator = parameter["separator"] if "separator" in parameter else ""
                                metadata[parameter["key"]] = separator.join(last_values)
                            elif parameter["type"] == "delimiter":
                                language = self._languages_fullname[metadata["language"].lower()]
                                # self.create_document(
                                    # parentNode  = parentNode,
                                    # title       = metadata["title"],
                                    # metadata    = metadata,
                                    # guid        = metadata["doi"]
                                # )
                                print(self.format_metadata(metadata))
                                print()
                                metadata = {}
                        last_key = parameter_key
                        last_values = []
                    last_values.append(line[3:-1].decode())
            self._file.close()

