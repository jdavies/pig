# pig
Quick ID generator for fictitious products

Most of the functionality is still hard-coded into the script. There are 2 main
parameters to pass in on the command line:

--mfg (-m) The manufacturer's 2 - 3 character ID.

--num (-n) The number of IDs to generate.

There are 2 optional parametrers to pass in if you want to generate an SVG
file for the IDs:

--output (-o_) The name of the SVG file to create

--title (-t) The base title of the decal/page names. A number will be appended
to this base for each decal/page in the SVG file generated. This is used ONLY
if the output parameter is also defined.

## Example

`python pig.py -n 10 -m UC -o test -t T_My_Decal`

generates the following:

    ***********************************************************
    *                                                         *
    *                    Python ID Generator                  *
    *                            by                           *
    *                        Jeff Davies                      *
    *                                                         *
    * Example:                                                *
    *  python pig.py -m UC -n 10 -o output.svg -t T_My_Decal  *
    ***********************************************************
    -mfg is UC
    -num is 10
    -o is test.svg
    UC-293438-IKM-78
    UC-917375-MIA-49
    UC-478617-CYE-45
    UC-402274-UKH-85
    UC-068950-HKG-67
    UC-520526-AFX-86
    UC-725262-TAY-67
    UC-594867-WAC-56
    UC-795021-CQP-85
    UC-240527-FCB-22
    Generated 10 values

That's all there is!