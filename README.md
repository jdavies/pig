# pig
Quick ID generator for fictitious products

Most of the functionality is still hard-coded into the script. There  re  2 main parameters to pass in on the command line:

--mfg The manufacturer's 2 - 3 character ID.

--num The nuber of IDs to generate, one per line.

## Example

`python pig.py -n 10 -m UC`

generates the following:

    ********************************
    *                              *
    *      Python ID Generator     *
    *              by              *
    *         Jeff Davies          *
    *                              *
    * Example:                     *
    *  python pig.py -m UC -n 10   *
    ********************************
    -mfg is UC
    -num is 10
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