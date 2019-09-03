﻿using CommandLine;

namespace Convertor
{
    public class Options
    {
        [Option('f', "filter", Required = false, HelpText = "Profile to filter on 1 = Open Referral, 2 = Service Directory")]
        public int Filter { get; set; }

        [Option('t', "type", Required = false, HelpText = "Type of file to export on gv = ERD, json = JSON Schema, csv = CSV Schema")]
        public string ExportType { get; set; }

        [Option('r', "ref", Required = false, HelpText = "Frame of reference for export")]
        public string ReferenceTable { get; set; }

        [Option('v', "verbose", Required = false, HelpText = "Should the output be verbose or not")]
        public int Verbose { get; set; }

        [Option('t', "title", Required = false, HelpText = "The title that should be used for the document")]
        public string Title { get; set; }

        [Option('m', "multiple", Required = false, HelpText = "1 if the intial object should be expressed as multiple objects")]
        public int Multiple { get; set; }
    }
}
