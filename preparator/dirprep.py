import core.antslogger as log
import preparator.__preparator as preparator

import os
import pathlib
import numpy as np


class DirPrep(preparator.Preparator):
    def __init__(self):
        super(DirPrep, self).__init__()

    @classmethod
    def getSubdirectory(cls, superior_path):
        # get paths where data is in itself
        sub_paths = [subs for subs in os.walk(superior_path) if len(subs[1]) == 0 and len(subs[-1]) != 0]
        sub_paths.sort()
        return sub_paths

    @classmethod
    def getDataDirectory(cls, superior_path, **kwargs):
        # return variable
        return_dir = []

        # kwargs
        file_expander = ''  # default = all files

        if 'expander' in kwargs:
            expander = kwargs.get('expander')
            if isinstance(file_expander, str):
                file_expander = expander
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
        else:
            file_expander = ''  # all files

        subs = DirPrep.getSubdirectory(superior_path=superior_path)

        for sub_i, _ in enumerate(subs):  # 1st sub-dir where data files in itself
            for file_i, _ in enumerate(subs[sub_i][-1]):  # data files in the 1st sub-dir
                if subs[sub_i][-1][file_i].endswith(file_expander):  # select only specified files
                    return_dir.append(os.path.join(subs[sub_i][0],
                                                   subs[sub_i][-1][file_i]))  # append merged directory
        return np.array(return_dir)
