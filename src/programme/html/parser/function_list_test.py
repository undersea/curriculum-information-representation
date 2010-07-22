import unittest

import function_list as flist


class FunctionListTest(unittest.TestCase):
    def test_get_function_empty_programme(self):
        self.assertFalse(flist.get_function('')())


    def test_programmefunction_class_callable(self):
        self.assertFalse(flist.ProgrammeFunction()())

        
    def test_accountancyfunction_class_callable(self):
        papers = set(['110.309', '110.329', '115.102', '110.109', '115.101', '115.103', '115.105', '115.106', '115.107', '115.108', '110.209', '110.229', '110.249', '110.279', '110.289', '125.230', '155.203', '155.210', '110.303', '110.309', '110.329','110.349','110.379','110.389','125.320','125.330','110.309', '110.329','110.379','110.309', '110.329', '110.379','110.389','219.202','219.203','156.200','156.231','125.320', '125.330', ] )
        
        accountancy = flist.AccountancyFunction()
        accountancy.parse('Bachelor of Accountancy (BAcc)')
        plist = accountancy()

        self.assertEqual(papers-plist, plist-papers)
