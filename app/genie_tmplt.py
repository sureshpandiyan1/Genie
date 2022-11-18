import os


class genie_htm():

    def genie_base(stxt):
        spn = ["<span style='font-size:" + str(scrth) + "px'>Typography</span>" for scrth in stxt]
        with open(os.environ["USERPROFILE"]+ "\Desktop\{0}.html".format("typography-scale"),'w') as htm:
            print("".join(["%s \n" % zz for zz in spn]), file=htm)


