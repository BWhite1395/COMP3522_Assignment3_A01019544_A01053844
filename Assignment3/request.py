class Request:
    def __init__(self, args):
        """
        Creates a request object with the args
        :param args:
        """
        self.mode = args.mode
        self.inputdata = args.inputdata
        self.inputfile = args.inputfile
        self.expanded = args.expanded
        self.output = args.output
        if self.inputfile:
            with open(self.inputfile, mode='r', encoding='utf-8') as in_file:
                self.inputdata_list = in_file.readlines()
            print(self.inputdata_list)
