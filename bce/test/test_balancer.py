#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

#
#  NOTE:
#    [1] This file was generated from "test_balancer.in".
#

import bce.public.api as _public_api
import bce.public.database as _public_db
import bce.public.option as _public_option
import bce.public.printer as _public_printer
import bce.option as _opt
import unittest as _unittest


def test_balancer(expression):
    """Test the balancer with a chemical equation.

    :type expression: str
    :param expression: The chemical equation.
    :rtype : bool
    :return: True if succeed.
    """

    #  Create an option object.
    option = _opt.Option()

    #  Set the abbreviation mapping.
    _public_option.MoleculeParserOptionWrapper(option).set_abbreviation_mapping(
        _public_db.BUNDLED_ABBREVIATION_DATABASE
    )

    #  Balance the chemical equation.
    result = _public_api.balance_chemical_equation(
        expression,
        option,
        printer=_public_printer.PRINTER_TEXT,
        unknown_header="X"
    )

    #  Check and return.
    return _public_api.is_chemical_equation_balanced(result, option)


class BalancerTest(_unittest.TestCase):
    """Test class for the balancer."""

    def test_1(self):
        """Run test case 1."""

        self.assertTrue(test_balancer("CoSO4+NH3=CoSO4.6NH3"))

    def test_2(self):
        """Run test case 2."""

        self.assertTrue(test_balancer("CoSO4+MnO2+H2O=Co2O3+MnSO4+H2SO4"))

    def test_3(self):
        """Run test case 3."""

        self.assertTrue(test_balancer("CoSO4+Mn2O3=Co2O3+MnSO4"))

    def test_4(self):
        """Run test case 4."""

        self.assertTrue(test_balancer("CoSO4+PbO2+H2O=Co(OH)3+PbSO4+O2"))

    def test_5(self):
        """Run test case 5."""

        self.assertTrue(test_balancer("CoSO4+PbO2+H2O=Co2O3+PbSO4+H2SO4"))

    def test_6(self):
        """Run test case 6."""

        self.assertTrue(test_balancer("CoSO4+NH4OH+I2=Co2(NH3)10.(SO4)2I2.2H2O+H2O"))

    def test_7(self):
        """Run test case 7."""

        self.assertTrue(test_balancer("CoSO4+KOH=K2CoO2+K2SO4+H2O"))

    def test_8(self):
        """Run test case 8."""

        self.assertTrue(test_balancer("CoSO4+KOH=Co(OH)2+K2SO4"))

    def test_9(self):
        """Run test case 9."""

        self.assertTrue(test_balancer("CoSO4+H2S=CoS+H2SO4"))

    def test_10(self):
        """Run test case 10."""

        self.assertTrue(test_balancer("CoSO4+H3PO4=Co(PO3)2+SO3+H2O"))

    def test_11(self):
        """Run test case 11."""

        self.assertTrue(test_balancer("Mg+O2=MgO"))

    def test_12(self):
        """Run test case 12."""

        self.assertTrue(test_balancer("CoSO4+KI+KIO3+H2O=Co(OH)2+K2SO4+I2"))

    def test_13(self):
        """Run test case 13."""

        self.assertTrue(test_balancer("Co(OH)2+KIO3+H2O=Co(OH)3+KI"))

    def test_14(self):
        """Run test case 14."""

        self.assertTrue(test_balancer("CoSO4+KCN=K2Co(CN)4+K2SO4"))

    def test_15(self):
        """Run test case 15."""

        self.assertTrue(test_balancer("CoSO4+Ba(SCN)2+H2O=BaSO4+Co(SCN)2.4H2O"))

    def test_16(self):
        """Run test case 16."""

        self.assertTrue(test_balancer("CoSO4+NaClO+H2O=Co2O3+NaCl+H2SO4"))

    def test_17(self):
        """Run test case 17."""

        self.assertTrue(test_balancer("CoSO4+Ba(ClO3)2+H2O=BaSO4+Co(ClO3)2.6H2O"))

    def test_18(self):
        """Run test case 18."""

        self.assertTrue(test_balancer("CoSO4+(NH4)3AsO4+H2O=Co3(AsO4)2.8H2O+(NH4)2SO4"))

    def test_19(self):
        """Run test case 19."""

        self.assertTrue(test_balancer("CoSO4+(NH4)2CO3+NH3+H2O+O2=(NH4)2SO4+(Co(NH3)4CO3)2SO4.3H2O"))

    def test_20(self):
        """Run test case 20."""

        self.assertTrue(test_balancer("CoSO4+KMnO4+H2O2=CoMnO3.2H2O+K2SO4+H2SO4+O2"))

    def test_21(self):
        """Run test case 21."""

        self.assertTrue(test_balancer("CoSO4+K4Fe(CN)6=Co2(Fe(CN)6)+K2SO4"))

    def test_22(self):
        """Run test case 22."""

        self.assertTrue(test_balancer("Cl2+H2O2=HCl+O2"))

    def test_23(self):
        """Run test case 23."""

        self.assertTrue(test_balancer("CoSO4+Na2Fe(CN)5NO=CoFe(CN)5NO+Na2SO4"))

    def test_24(self):
        """Run test case 24."""

        self.assertTrue(test_balancer("Co(NO3)2.6H2O+H2O2+NaHCO3=Na3(Co(CO3)3).3H2O+NaNO3+CO2+H2O"))

    def test_25(self):
        """Run test case 25."""

        self.assertTrue(test_balancer("Co(NO3)2+NH3+KI=CoI2.6NH3+KNO3"))

    def test_26(self):
        """Run test case 26."""

        self.assertTrue(test_balancer("Co(NO3)2+NH3+HF+O2=Co(NH3)6(NO2)2F+H2O"))

    def test_27(self):
        """Run test case 27."""

        self.assertTrue(test_balancer("Co(NO3)2+KIO3=Co(IO3)2+KNO3"))

    def test_28(self):
        """Run test case 28."""

        self.assertTrue(test_balancer("Co(NO3)2+NaNO3+HC2H3O2=Na3Co(NO3)6+NaC2H3O2+NO2+H2O"))

    def test_29(self):
        """Run test case 29."""

        self.assertTrue(test_balancer("Co(NO3)2+KHCO3+H2O=KNO3+CoCO3.Co(OH)2+HNO3"))

    def test_30(self):
        """Run test case 30."""

        self.assertTrue(test_balancer("Co(NO3)2+(NH4)2CO3=CoCO3+NH4NO3"))

    def test_31(self):
        """Run test case 31."""

        self.assertTrue(test_balancer("CoCO3+H2O=Co(OH)2+CO2"))

    def test_32(self):
        """Run test case 32."""

        self.assertTrue(test_balancer("Co(NO3)2+(NH4)2CO3+H2O=(NH4)2CO3.CoCO3.4H2O+NH4NO3"))

    def test_33(self):
        """Run test case 33."""

        self.assertTrue(test_balancer("S+C=CS2"))

    def test_34(self):
        """Run test case 34."""

        self.assertTrue(test_balancer("Co(NO3)2+K2CrO4=CoCrO4+KNO3"))

    def test_35(self):
        """Run test case 35."""

        self.assertTrue(test_balancer("Co(NO3)2+H4(Fe(CN)6)+H2O=Co2(Fe(CN)6).7H2O+HNO3"))

    def test_36(self):
        """Run test case 36."""

        self.assertTrue(test_balancer("Co(NO3)2+C4O6H6+NH3.H2O=CoC4O6H4+NH4NO3+H2O"))

    def test_37(self):
        """Run test case 37."""

        self.assertTrue(test_balancer("Li+H2=LiH"))

    def test_38(self):
        """Run test case 38."""

        self.assertTrue(test_balancer("Li+Cl2=LiCl"))

    def test_39(self):
        """Run test case 39."""

        self.assertTrue(test_balancer("Li+O2=Li2O"))

    def test_40(self):
        """Run test case 40."""

        self.assertTrue(test_balancer("Li+O2+CO2=Li2CO3"))

    def test_41(self):
        """Run test case 41."""

        self.assertTrue(test_balancer("Li+N2=Li3N"))

    def test_42(self):
        """Run test case 42."""

        self.assertTrue(test_balancer("Li+P=Li3P"))

    def test_43(self):
        """Run test case 43."""

        self.assertTrue(test_balancer("Li+Si=Li2Si2"))

    def test_44(self):
        """Run test case 44."""

        self.assertTrue(test_balancer("S+Cu=Cu2S"))

    def test_45(self):
        """Run test case 45."""

        self.assertTrue(test_balancer("Li+NH3=LiNH2+H2"))

    def test_46(self):
        """Run test case 46."""

        self.assertTrue(test_balancer("Li+CO=Li2C2+O2"))

    def test_47(self):
        """Run test case 47."""

        self.assertTrue(test_balancer("Li+CO2=Li2C2+O2"))

    def test_48(self):
        """Run test case 48."""

        self.assertTrue(test_balancer("Li+H2S=LiHS+H2"))

    def test_49(self):
        """Run test case 49."""

        self.assertTrue(test_balancer("Li+HCl=LiCl+H2"))

    def test_50(self):
        """Run test case 50."""

        self.assertTrue(test_balancer("Li+HCN=LiCN+H2"))

    def test_51(self):
        """Run test case 51."""

        self.assertTrue(test_balancer("Li+H2SO4=Li2SO4+H2"))

    def test_52(self):
        """Run test case 52."""

        self.assertTrue(test_balancer("Li+H<e+>=Li<e+>+H2"))

    def test_53(self):
        """Run test case 53."""

        self.assertTrue(test_balancer("LiH+NH3=LiNH2+H2"))

    def test_54(self):
        """Run test case 54."""

        self.assertTrue(test_balancer("LiH+H2O=LiOH+H2"))

    def test_55(self):
        """Run test case 55."""

        self.assertTrue(test_balancer("P4+HNO3=H3PO4+NO2+H2O"))

    def test_56(self):
        """Run test case 56."""

        self.assertTrue(test_balancer("LiH+HCl=LiCl+H2"))

    def test_57(self):
        """Run test case 57."""

        self.assertTrue(test_balancer("LiH+BeCl2=BeH2+LiCl"))

    def test_58(self):
        """Run test case 58."""

        self.assertTrue(test_balancer("LiH+AlCl3=Li(AlH4)+LiCl"))

    def test_59(self):
        """Run test case 59."""

        self.assertTrue(test_balancer("Li2O+Si=Li+SiO2"))

    def test_60(self):
        """Run test case 60."""

        self.assertTrue(test_balancer("Li2O+Al=Li+Al2O3"))

    def test_61(self):
        """Run test case 61."""

        self.assertTrue(test_balancer("Li2O+CaO+Si=Li+SiO2.2CaO"))

    def test_62(self):
        """Run test case 62."""

        self.assertTrue(test_balancer("Li2O+CaO+Al=Li+CaO.Al2O3"))

    def test_63(self):
        """Run test case 63."""

        self.assertTrue(test_balancer("Li2O+H2O=LiOH"))

    def test_64(self):
        """Run test case 64."""

        self.assertTrue(test_balancer("Li2O+H<e+>=Li<e+>+H2O"))

    def test_65(self):
        """Run test case 65."""

        self.assertTrue(test_balancer("LiOH=Li2O+H2O"))

    def test_66(self):
        """Run test case 66."""

        self.assertTrue(test_balancer("HNO3+Fe=Fe(NO3)3+NO2+H2O"))

    def test_67(self):
        """Run test case 67."""

        self.assertTrue(test_balancer("LiOH+H2O2+H2O=LiO2.H2O2.3H2O"))

    def test_68(self):
        """Run test case 68."""

        self.assertTrue(test_balancer("LiOH+H2O2+H2O=Li2O2.H2O2.3H2O"))

    def test_69(self):
        """Run test case 69."""

        self.assertTrue(test_balancer("LiOH+HCN=LiCN+H2O"))

    def test_70(self):
        """Run test case 70."""

        self.assertTrue(test_balancer("LiOH+HClO4=LiClO4+H2O"))

    def test_71(self):
        """Run test case 71."""

        self.assertTrue(test_balancer("KHC2O4.H2C2O4+KMnO4+H2SO4=MnSO4+K2SO4+CO2+H2O"))

    def test_72(self):
        """Run test case 72."""

        self.assertTrue(test_balancer("H2+Ca(CN)2+NaAlF4+FeSO4+MgSiO3+KI+H3PO4+PbCrO4+BrCl+CF2Cl2+SO2=PbBr2+" +
                                      "CrCl3+MgCO3+KAl(OH)4+Fe(SCN)3+PI3+Na2SiO3+CaF2+H2O"))

    def test_73(self):
        """Run test case 73."""

        self.assertTrue(test_balancer("P4+P2I4+H2O=PH4I+H3PO4"))

    def test_74(self):
        """Run test case 74."""

        self.assertTrue(test_balancer("NH3+O2=HNO3+H2O"))

    def test_75(self):
        """Run test case 75."""

        self.assertTrue(test_balancer("NH3+O2=HNO2+H2O"))

    def test_76(self):
        """Run test case 76."""

        self.assertTrue(test_balancer("NH3+O2=N2+H2O"))

    def test_77(self):
        """Run test case 77."""

        self.assertTrue(test_balancer("HNO3+Fe=Fe(NO3)3+NO+H2O"))

    def test_78(self):
        """Run test case 78."""

        self.assertTrue(test_balancer("NH3+O2=N2O+H2O"))

    def test_79(self):
        """Run test case 79."""

        self.assertTrue(test_balancer("NH3+O2=NO+H2O"))

    def test_80(self):
        """Run test case 80."""

        self.assertTrue(test_balancer("NH3+O2=NH4NO3+H2O"))

    def test_81(self):
        """Run test case 81."""

        self.assertTrue(test_balancer("NH3+S=(NH4)2S+N4S4"))

    def test_82(self):
        """Run test case 82."""

        self.assertTrue(test_balancer("(NH4)2S+AgI=Ag2S+NH4I"))

    def test_83(self):
        """Run test case 83."""

        self.assertTrue(test_balancer("NH3+Na=NaNH2+H2"))

    def test_84(self):
        """Run test case 84."""

        self.assertTrue(test_balancer("NaNH2+H2O=NaOH+NH3"))

    def test_85(self):
        """Run test case 85."""

        self.assertTrue(test_balancer("NH3+NO=N2+H2O"))

    def test_86(self):
        """Run test case 86."""

        self.assertTrue(test_balancer("NH3+NO2=N2+H2O"))

    def test_87(self):
        """Run test case 87."""

        self.assertTrue(test_balancer("NH3+CO2+H2O=(NH4)2CO3"))

    def test_88(self):
        """Run test case 88."""

        self.assertTrue(test_balancer("HNO3+Fe=Fe(NO3)3+N2O+H2O"))

    def test_89(self):
        """Run test case 89."""

        self.assertTrue(test_balancer("(NH4)2CO3+CO2+H2O=NH4HCO3"))

    def test_90(self):
        """Run test case 90."""

        self.assertTrue(test_balancer("NH3+Cu2O=Cu3N+H2O"))

    def test_91(self):
        """Run test case 91."""

        self.assertTrue(test_balancer("NH3+HCl=NH4Cl"))

    def test_92(self):
        """Run test case 92."""

        self.assertTrue(test_balancer("NH3+HClO=NCl3+H2O"))

    def test_93(self):
        """Run test case 93."""

        self.assertTrue(test_balancer("NCl3=N2+Cl2"))

    def test_94(self):
        """Run test case 94."""

        self.assertTrue(test_balancer("NH3+HClO=NH2Cl+H2O"))

    def test_95(self):
        """Run test case 95."""

        self.assertTrue(test_balancer("NH3+H2SO4=(NH4)2SO4"))

    def test_96(self):
        """Run test case 96."""

        self.assertTrue(test_balancer("NH3+HNO2=N2+H2O"))

    def test_97(self):
        """Run test case 97."""

        self.assertTrue(test_balancer("NH3+HNO3=NH4NO3"))

    def test_98(self):
        """Run test case 98."""

        self.assertTrue(test_balancer("NH3+H3PO4=(NH4)3PO4"))

    def test_99(self):
        """Run test case 99."""

        self.assertTrue(test_balancer("HNO3+Fe=Fe(NO3)3+N2+H2O"))

    def test_100(self):
        """Run test case 100."""

        self.assertTrue(test_balancer("NH3+KBr.IBr=KBr+NH4Br+NI3"))

    def test_101(self):
        """Run test case 101."""

        self.assertTrue(test_balancer("NH3+NaClO=NaOH+NH2Cl"))

    def test_102(self):
        """Run test case 102."""

        self.assertTrue(test_balancer("NH2Cl+NaOH+NH3=N2H4+NaCl+H2O"))

    def test_103(self):
        """Run test case 103."""

        self.assertTrue(test_balancer("NH3+NaClO=N2H4+NaCl+H2O"))

    def test_104(self):
        """Run test case 104."""

        self.assertTrue(test_balancer("NH3+MnSO4+H2O2+H2O=Mn(OH)3+(NH4)2SO4"))

    def test_105(self):
        """Run test case 105."""

        self.assertTrue(test_balancer("NH3+HgCl2=Hg(NH2)Cl+NH4Cl"))

    def test_106(self):
        """Run test case 106."""

        self.assertTrue(test_balancer("NH3+COCl2=CO(NH2)2+NH4Cl"))

    def test_107(self):
        """Run test case 107."""

        self.assertTrue(test_balancer("NH3+SOCl2=SO(NH2)2+NH4Cl"))

    def test_108(self):
        """Run test case 108."""

        self.assertTrue(test_balancer("NH3+SO2Cl2=SO2(NH2)2+NH4Cl"))

    def test_109(self):
        """Run test case 109."""

        self.assertTrue(test_balancer("NH3+C6H4N4OCl+H2O=C6H8N5O2+NH4Cl"))

    def test_110(self):
        """Run test case 110."""

        self.assertTrue(test_balancer("HNO3+Fe=Fe(NO3)3+NH4NO3+H2O"))

    def test_111(self):
        """Run test case 111."""

        self.assertTrue(test_balancer("2A2BC3.3D2C=3A2BC3+D2C"))

    def test_112(self):
        """Run test case 112."""

        self.assertTrue(test_balancer("N2H4=NH3+N2"))

    def test_113(self):
        """Run test case 113."""

        self.assertTrue(test_balancer("N2H4+O2=N2+H2O"))

    def test_114(self):
        """Run test case 114."""

        self.assertTrue(test_balancer("N2H4+Na=NaN2H3+H2"))

    def test_115(self):
        """Run test case 115."""

        self.assertTrue(test_balancer("N2H4+H2O=N2H5<e+>+OH<e->"))

    def test_116(self):
        """Run test case 116."""

        self.assertTrue(test_balancer("N2H4+H2O2=HNO3+H2O"))

    def test_117(self):
        """Run test case 117."""

        self.assertTrue(test_balancer("N2H4+H2O2=N2+H2O"))

    def test_118(self):
        """Run test case 118."""

        self.assertTrue(test_balancer("N2H4+HNO2=HN3+H2O"))

    def test_119(self):
        """Run test case 119."""

        self.assertTrue(test_balancer("N2H4+H<e+>=N2H5<e+>"))

    def test_120(self):
        """Run test case 120."""

        self.assertTrue(test_balancer("HN3=N2+H2"))

    def test_121(self):
        """Run test case 121."""

        self.assertTrue(test_balancer("HN3+HClO=ClN3+H2O"))

    def test_122(self):
        """Run test case 122."""

        self.assertTrue(test_balancer("S+HNO3=SO2+NO+H2O"))

    def test_123(self):
        """Run test case 123."""

        self.assertTrue(test_balancer("NH2OH=NH3+N2O+H2O"))

    def test_124(self):
        """Run test case 124."""

        self.assertTrue(test_balancer("NH2OH=N2+H<e+>+<e->+H2O"))

    def test_125(self):
        """Run test case 125."""

        self.assertTrue(test_balancer("NH2OH+OH<e->=N2+H2O+<e->"))

    def test_126(self):
        """Run test case 126."""

        self.assertTrue(test_balancer("NH2OH+HNO2=N2O+H2O"))

    def test_127(self):
        """Run test case 127."""

        self.assertTrue(test_balancer("NH2CN+H2O=CO(NH2)2"))

    def test_128(self):
        """Run test case 128."""

        self.assertTrue(test_balancer("NH2CN+NH3=(NH2)2CNH"))

    def test_129(self):
        """Run test case 129."""

        self.assertTrue(test_balancer("NCl3=Cl2+N2"))

    def test_130(self):
        """Run test case 130."""

        self.assertTrue(test_balancer("NCl3+H2O=HClO+NH3"))

    def test_131(self):
        """Run test case 131."""

        self.assertTrue(test_balancer("N4S4=N2+S"))

    def test_132(self):
        """Run test case 132."""

        self.assertTrue(test_balancer("NH4Cl=HCl+NH3"))

    def test_133(self):
        """Run test case 133."""

        self.assertTrue(test_balancer("P+CuSO4+H2O=Cu3P+H3PO4+H2SO4"))

    def test_134(self):
        """Run test case 134."""

        self.assertTrue(test_balancer("NH4Cl+Cl2=HCl+NCl3"))

    def test_135(self):
        """Run test case 135."""

        self.assertTrue(test_balancer("NH4Cl+Br2=NH4ClBr2"))

    def test_136(self):
        """Run test case 136."""

        self.assertTrue(test_balancer("NH4Cl+NaHCO3+Br2=NaBr+NaCl+CO2+N2+H2O"))

    def test_137(self):
        """Run test case 137."""

        self.assertTrue(test_balancer("NH4Cl+MO=MCl2+M+N2+H2O"))

    def test_138(self):
        """Run test case 138."""

        self.assertTrue(test_balancer("NH4Cl+MO=MCl2+NH3+H2O"))

    def test_139(self):
        """Run test case 139."""

        self.assertTrue(test_balancer("NH4Cl+KOH+CH2O=N2(CH2)3+KCl+H2O"))

    def test_140(self):
        """Run test case 140."""

        self.assertTrue(test_balancer("NH4Cl+H2SO4=(NH4)2SO4+HCl"))

    def test_141(self):
        """Run test case 141."""

        self.assertTrue(test_balancer("NH4Cl+HNO3=N2O+HCl+H2O"))

    def test_142(self):
        """Run test case 142."""

        self.assertTrue(test_balancer("NH4Cl+KNO2=NH4NO2+KCl"))

    def test_143(self):
        """Run test case 143."""

        self.assertTrue(test_balancer("NH4NO2=N2+H2O"))

    def test_144(self):
        """Run test case 144."""

        self.assertTrue(test_balancer("Al+HNO3=Al(NO3)3+NO+H2O"))

    def test_145(self):
        """Run test case 145."""

        self.assertTrue(test_balancer("NH4Cl+KNO2=KCl+N2+H2O"))

    def test_146(self):
        """Run test case 146."""

        self.assertTrue(test_balancer("NH4Cl+NH4HSO4=(NH4)2SO4+HCl"))

    def test_147(self):
        """Run test case 147."""

        self.assertTrue(test_balancer("NH4<e+>+I<e->+ClO<e->=NHI2+NH3+Cl<e->+H2O"))

    def test_148(self):
        """Run test case 148."""

        self.assertTrue(test_balancer("NH4Cl+KOH+K2(HgI4)=Hg2NH2OI+KCl+KI+H2O"))

    def test_149(self):
        """Run test case 149."""

        self.assertTrue(test_balancer("KI+HgCl2=HgI2+KCl"))

    def test_150(self):
        """Run test case 150."""

        self.assertTrue(test_balancer("HgI2+KI=K2(HgI4)"))

    def test_151(self):
        """Run test case 151."""

        self.assertTrue(test_balancer("NH4Cl+NaHC4H4O6=(NH4)HC4H4O6+NaCl"))

    def test_152(self):
        """Run test case 152."""

        self.assertTrue(test_balancer("(NH4)2S+HNO3=NH4NO3+H2S"))

    def test_153(self):
        """Run test case 153."""

        self.assertTrue(test_balancer("(NH4)2S+H2O=NH4HS+NH4OH"))

    def test_154(self):
        """Run test case 154."""

        self.assertTrue(test_balancer("H2S+HNO3=NO+S+H2O"))

    def test_155(self):
        """Run test case 155."""

        self.assertTrue(test_balancer("H2SO4+Fe=Fe2(SO4)3+SO2+H2O"))

    def test_156(self):
        """Run test case 156."""

        self.assertTrue(test_balancer("NO+O2=NO2"))

    def test_157(self):
        """Run test case 157."""

        self.assertTrue(test_balancer("NH4NO2=N2+H2O"))

    def test_158(self):
        """Run test case 158."""

        self.assertTrue(test_balancer("(NH4)2S+CH3COOH=CH3COONH4+H2S"))

    def test_159(self):
        """Run test case 159."""

        self.assertTrue(test_balancer("(NH4)2S+Al2(SO4)3+H2O=Al(OH)3+(NH4)2SO4+H2S"))

    def test_160(self):
        """Run test case 160."""

        self.assertTrue(test_balancer("(NH4)2S2+CH3COOH=CH3COONH4+H2S+S"))

    def test_161(self):
        """Run test case 161."""

        self.assertTrue(test_balancer("(NH4)2S3+HCl=NH4Cl+H2S+S"))

    def test_162(self):
        """Run test case 162."""

        self.assertTrue(test_balancer("NH4HS+NaOH=Na2S+NH3+H2O"))

    def test_163(self):
        """Run test case 163."""

        self.assertTrue(test_balancer("NH4SCN=H2NCSNH2"))

    def test_164(self):
        """Run test case 164."""

        self.assertTrue(test_balancer("NH4HF2+F2=NF3+HF"))

    def test_165(self):
        """Run test case 165."""

        self.assertTrue(test_balancer("NH4ClO3=NH4Cl+O2"))

    def test_166(self):
        """Run test case 166."""

        self.assertTrue(test_balancer("KClO3=KCl+O2"))

    def test_167(self):
        """Run test case 167."""

        self.assertTrue(test_balancer("NH4Cl+NaBrO=N2+NaBr+HCl+H2O"))

    def test_168(self):
        """Run test case 168."""

        self.assertTrue(test_balancer("NH4ClO4=Cl2+O2+N2+H2O"))

    def test_169(self):
        """Run test case 169."""

        self.assertTrue(test_balancer("NH4ClO4+Zn=ZnO+N2+Cl2+H2O"))

    def test_170(self):
        """Run test case 170."""

        self.assertTrue(test_balancer("NH4ClO4+H2SO4=HClO4+(NH4)2SO4"))

    def test_171(self):
        """Run test case 171."""

        self.assertTrue(test_balancer("(NH4)2SO4=H2SO4+NH3"))

    def test_172(self):
        """Run test case 172."""

        self.assertTrue(test_balancer("(NH4)2SO4=NH3+SO2+N2+H2O"))

    def test_173(self):
        """Run test case 173."""

        self.assertTrue(test_balancer("(NH4)2SO4+O2=HNO3+H2SO4+H2O"))

    def test_174(self):
        """Run test case 174."""

        self.assertTrue(test_balancer("(NH4)2SO3+H2SO4=(NH4)2SO4+SO2+H2O"))

    def test_175(self):
        """Run test case 175."""

        self.assertTrue(test_balancer("NH4NO3=NH3+HNO3"))

    def test_176(self):
        """Run test case 176."""

        self.assertTrue(test_balancer("NH4NO3=NO+N2+H2O"))

    def test_177(self):
        """Run test case 177."""

        self.assertTrue(test_balancer("KMnO4=K2MnO4+MnO2+O2"))

    def test_178(self):
        """Run test case 178."""

        self.assertTrue(test_balancer("NH4NO3=N2O3+N2+H2O"))

    def test_179(self):
        """Run test case 179."""

        self.assertTrue(test_balancer("NH4NO3=NO2+N2+H2O"))

    def test_180(self):
        """Run test case 180."""

        self.assertTrue(test_balancer("NH4NO3=HNO3+N2+H2O"))

    def test_181(self):
        """Run test case 181."""

        self.assertTrue(test_balancer("NH4NO3=N2O+H2O"))

    def test_182(self):
        """Run test case 182."""

        self.assertTrue(test_balancer("NH4NO3=N2+O2+H2O"))

    def test_183(self):
        """Run test case 183."""

        self.assertTrue(test_balancer("NH4NO3+O2=HNO3+H2O"))

    def test_184(self):
        """Run test case 184."""

        self.assertTrue(test_balancer("NH4NO3+H2=N2+H2O"))

    def test_185(self):
        """Run test case 185."""

        self.assertTrue(test_balancer("NH4NO3+H2O=NH3.H2O+HNO3"))

    def test_186(self):
        """Run test case 186."""

        self.assertTrue(test_balancer("NH4NO3+NaOH=NaNO3+NH3+H2O"))

    def test_187(self):
        """Run test case 187."""

        self.assertTrue(test_balancer("NH4NO3+NaNO2=NH4NO2+NaNO3"))

    def test_188(self):
        """Run test case 188."""

        self.assertTrue(test_balancer("HCl+MnO2=MnCl2+Cl2+H2O"))

    def test_189(self):
        """Run test case 189."""

        self.assertTrue(test_balancer("NH4NO3+K2Cr2O7=(NH4)2Cr2O7+KNO3"))

    def test_190(self):
        """Run test case 190."""

        self.assertTrue(test_balancer("NH4NO3+CH2O=C6H12N4+HNO3+H2O"))

    def test_191(self):
        """Run test case 191."""

        self.assertTrue(test_balancer("K2CO3+NH4NO3=KNO3+(NH4)2CO3"))

    def test_192(self):
        """Run test case 192."""

        self.assertTrue(test_balancer("NH4NO2=N2+H2O"))

    def test_193(self):
        """Run test case 193."""

        self.assertTrue(test_balancer("NH4H2PO4+(NH4)2MoO4+HNO3=NH4NO3+(NH4)3(PO4.12MoO3).2H2O+H2O"))

    def test_194(self):
        """Run test case 194."""

        self.assertTrue(test_balancer("((NH4)3(PO4.12MoO3).2H2O)+NaOH=(NH4)2MoO4+Na2MoO4+(NH4)2HPO4+H2O"))

    def test_195(self):
        """Run test case 195."""

        self.assertTrue(test_balancer("(NH4)2HPO4+(NH4)2MoO4+HNO3=(NH4)3(PO4.12MoO3).H2O+NH4NO3+H2O"))

    def test_196(self):
        """Run test case 196."""

        self.assertTrue(test_balancer("(NH4)2HPO4+FeCl3=NH4H2PO4.FePO4+NH4Cl"))

    def test_197(self):
        """Run test case 197."""

        self.assertTrue(test_balancer("(NH4)3PO4=NH3+H3PO4"))

    def test_198(self):
        """Run test case 198."""

        self.assertTrue(test_balancer("(NH4)3PO4+Ca(OH)2=Ca3(PO4)2+NH3+H2O"))

    def test_199(self):
        """Run test case 199."""

        self.assertTrue(test_balancer("Cu+HNO3=Cu(NO3)2+NO+H2O"))

    def test_200(self):
        """Run test case 200."""

        self.assertTrue(test_balancer("(NH4)3PO4+Fe(NO3)2+H2O=Fe(NH4)PO4.2H2O+NH4NO3"))

    def test_201(self):
        """Run test case 201."""

        self.assertTrue(test_balancer("NH4HCO3=NH3+H2O+CO2"))

    def test_202(self):
        """Run test case 202."""

        self.assertTrue(test_balancer("NH4HCO3+NaCl=NaHCO3+NH4Cl"))

    def test_203(self):
        """Run test case 203."""

        self.assertTrue(test_balancer("(NH4)2CO3=NH3+CO2+H2O"))

    def test_204(self):
        """Run test case 204."""

        self.assertTrue(test_balancer("(NH4)2CO3+CO2+H2O=NH4HCO3"))

    def test_205(self):
        """Run test case 205."""

        self.assertTrue(test_balancer("(NH4)2CO3+NaOH=Na2CO3+NH3+H2O"))

    def test_206(self):
        """Run test case 206."""

        self.assertTrue(test_balancer("(NH4)2CO3+K2CO3=KOH+NH3+CO2"))

    def test_207(self):
        """Run test case 207."""

        self.assertTrue(test_balancer("NH4CNO=CO(NH2)2"))

    def test_208(self):
        """Run test case 208."""

        self.assertTrue(test_balancer("CO(NH2)2=HNCO+NH3"))

    def test_209(self):
        """Run test case 209."""

        self.assertTrue(test_balancer("CO(NH2)2=NH2CONHCONH2+NH3"))

    def test_210(self):
        """Run test case 210."""

        self.assertTrue(test_balancer("CuSO4.5H2O=CuSO4+H2O"))

    def test_211(self):
        """Run test case 211."""

        self.assertTrue(test_balancer("CO(NH2)2+H2O=(NH4)2CO3"))

    def test_212(self):
        """Run test case 212."""

        self.assertTrue(test_balancer("CO(NH2)2+HNO2=CO2+N2+N2O"))

    def test_213(self):
        """Run test case 213."""

        self.assertTrue(test_balancer("CO(NH2)2+HNO3=CO(NH2)2.HNO3"))

    def test_214(self):
        """Run test case 214."""

        self.assertTrue(test_balancer("CO(NH2)2+NaNO2+H2SO4=Na2SO4+CO2+N2+H2O"))

    def test_215(self):
        """Run test case 215."""

        self.assertTrue(test_balancer("N2O=N2+O2"))

    def test_216(self):
        """Run test case 216."""

        self.assertTrue(test_balancer("NO+H2=H2O2+N2"))

    def test_217(self):
        """Run test case 217."""

        self.assertTrue(test_balancer("NO+(H)=NH3+H2O"))

    def test_218(self):
        """Run test case 218."""

        self.assertTrue(test_balancer("NO+F2=NO2F+N2"))

    def test_219(self):
        """Run test case 219."""

        self.assertTrue(test_balancer("NO+Cl2=NOCl"))

    def test_220(self):
        """Run test case 220."""

        self.assertTrue(test_balancer("NO+O2=NO2"))

    def test_221(self):
        """Run test case 221."""

        self.assertTrue(test_balancer("Na2CO3.2H2O+H2O=Na2CO3.10H2O"))

    def test_222(self):
        """Run test case 222."""

        self.assertTrue(test_balancer("F2+Cl2=ClF"))

    def test_223(self):
        """Run test case 223."""

        self.assertTrue(test_balancer("NO+P=P4O6+N2"))

    def test_224(self):
        """Run test case 224."""

        self.assertTrue(test_balancer("NO+NO2=N2O3"))

    def test_225(self):
        """Run test case 225."""

        self.assertTrue(test_balancer("NO+CO=N2+CO2"))

    def test_226(self):
        """Run test case 226."""

        self.assertTrue(test_balancer("NO+KOH=KNO2+N2+H2O"))

    def test_227(self):
        """Run test case 227."""

        self.assertTrue(test_balancer("NO+HNO3=N2O3+H2O"))

    def test_228(self):
        """Run test case 228."""

        self.assertTrue(test_balancer("NO+HNO3+H2O=HNO2"))

    def test_229(self):
        """Run test case 229."""

        self.assertTrue(test_balancer("HNO2=N2O3+H2O"))

    def test_230(self):
        """Run test case 230."""

        self.assertTrue(test_balancer("NO+HNO3+H2SO4=HSNO5+H2O"))

    def test_231(self):
        """Run test case 231."""

        self.assertTrue(test_balancer("NO+MnO4<e->+H<e+>=Mn<2e+>+NO3<e->+H2O"))

    def test_232(self):
        """Run test case 232."""

        self.assertTrue(test_balancer("N2O3=NO2+NO"))

    def test_233(self):
        """Run test case 233."""

        self.assertTrue(test_balancer("2Na2CO3.2H2O+H2O=Na2CO3.3H2O"))

    def test_234(self):
        """Run test case 234."""

        self.assertTrue(test_balancer("N2O3+Hg+H2SO4=Hg2SO4+NO+H2O"))

    def test_235(self):
        """Run test case 235."""

        self.assertTrue(test_balancer("N2O3+H2O=HNO2"))

    def test_236(self):
        """Run test case 236."""

        self.assertTrue(test_balancer("N2O3+NaOH=NaNO2+H2O"))

    def test_237(self):
        """Run test case 237."""

        self.assertTrue(test_balancer("N2O3+H2SO4=NOHSO4+H2O"))

    def test_238(self):
        """Run test case 238."""

        self.assertTrue(test_balancer("N2O3+KMnO4+H2SO4=K2SO4+MnSO4+HNO3+H2O"))

    def test_239(self):
        """Run test case 239."""

        self.assertTrue(test_balancer("N2O3+C6H4SO2OHNH2+CH3COOH=C6H4SO2OHN2(CH3COO)+H2O"))

    def test_240(self):
        """Run test case 240."""

        self.assertTrue(test_balancer("NO2+H2O=HNO3+HNO2"))

    def test_241(self):
        """Run test case 241."""

        self.assertTrue(test_balancer("HNO2+O2=HNO3"))

    def test_242(self):
        """Run test case 242."""

        self.assertTrue(test_balancer("NO2+H2O=HNO3+NO"))

    def test_243(self):
        """Run test case 243."""

        self.assertTrue(test_balancer("NO2+NO+H2O=HNO2"))

    def test_244(self):
        """Run test case 244."""

        self.assertTrue(test_balancer("Pb(N3)2+Cr(MnO4)2=Cr2O3+MnO2+Pb3O4+NO"))

    def test_245(self):
        """Run test case 245."""

        self.assertTrue(test_balancer("NO2+NO+KOH=KNO2+H2O"))

    def test_246(self):
        """Run test case 246."""

        self.assertTrue(test_balancer("NO2+NO+H2SO4=H(NO)SO4+H2O"))

    def test_247(self):
        """Run test case 247."""

        self.assertTrue(test_balancer("H(NO)SO4+SO2+H2O=H2SO4+NO"))

    def test_248(self):
        """Run test case 248."""

        self.assertTrue(test_balancer("NO2+NO+Na2CO3=NaNO2+CO2"))

    def test_249(self):
        """Run test case 249."""

        self.assertTrue(test_balancer("NO2+NO+Na2CO3+H2O=NaHCO3+NaNO2"))

    def test_250(self):
        """Run test case 250."""

        self.assertTrue(test_balancer("NO2+CO=NO+CO2"))

    def test_251(self):
        """Run test case 251."""

        self.assertTrue(test_balancer("NO2+NaOH=NaNO3+NaNO2+H2O"))

    def test_252(self):
        """Run test case 252."""

        self.assertTrue(test_balancer("NO2+KOH=KNO3+KNO2+H2O"))

    def test_253(self):
        """Run test case 253."""

        self.assertTrue(test_balancer("NO2+H2S=NO+SO3+H2O"))

    def test_254(self):
        """Run test case 254."""

        self.assertTrue(test_balancer("NO2+H2SO4=NOHSO4+HNO3"))

    def test_255(self):
        """Run test case 255."""

        self.assertTrue(test_balancer("NaCl+MnO2+H2SO4=NaHSO4+MnCl2+H2O+Cl2"))

    def test_256(self):
        """Run test case 256."""

        self.assertTrue(test_balancer("NO2+Na2CO3=NaNO3+NaNO2+CO2"))

    def test_257(self):
        """Run test case 257."""

        self.assertTrue(test_balancer("NO2+KMnO4+H2SO4+H2O=MnSO4+K2SO4+HNO3"))

    def test_258(self):
        """Run test case 258."""

        self.assertTrue(test_balancer("N2O5=N2O4+O2"))

    def test_259(self):
        """Run test case 259."""

        self.assertTrue(test_balancer("N2O5=N2O3+O2"))

    def test_260(self):
        """Run test case 260."""

        self.assertTrue(test_balancer("N2O5=NO2+O2"))

    def test_261(self):
        """Run test case 261."""

        self.assertTrue(test_balancer("N2O5+NO=NO2"))

    def test_262(self):
        """Run test case 262."""

        self.assertTrue(test_balancer("N2O5+H2O=HNO3"))

    def test_263(self):
        """Run test case 263."""

        self.assertTrue(test_balancer("N2O5+H2O2=HNO4+H2O"))

    def test_264(self):
        """Run test case 264."""

        self.assertTrue(test_balancer("N2O4=NO2"))

    def test_265(self):
        """Run test case 265."""

        self.assertTrue(test_balancer("N2O4+H2O+O2=HNO3"))

    def test_266(self):
        """Run test case 266."""

        self.assertTrue(test_balancer("SO2+KMnO4+H2O=MnSO4+K2SO4+H2SO4"))

    def test_267(self):
        """Run test case 267."""

        self.assertTrue(test_balancer("N2O+Cu=CuO+N2"))

    def test_268(self):
        """Run test case 268."""

        self.assertTrue(test_balancer("NO+Cu=CuO+N2"))

    def test_269(self):
        """Run test case 269."""

        self.assertTrue(test_balancer("N2O3+Cu=CuO+N2"))

    def test_270(self):
        """Run test case 270."""

        self.assertTrue(test_balancer("NO2+Cu=CuO+N2"))

    def test_271(self):
        """Run test case 271."""

        self.assertTrue(test_balancer("N2O5+Cu=CuO+N2"))

    def test_272(self):
        """Run test case 272."""

        self.assertTrue(test_balancer("HNO2=HNO3+NO+H2O"))

    def test_273(self):
        """Run test case 273."""

        self.assertTrue(test_balancer("HNO2=N2O3+H2O"))

    def test_274(self):
        """Run test case 274."""

        self.assertTrue(test_balancer("HNO2=NO2+NO+H2O"))

    def test_275(self):
        """Run test case 275."""

        self.assertTrue(test_balancer("HNO2+Br2+H2O=HNO3+HBr"))

    def test_276(self):
        """Run test case 276."""

        self.assertTrue(test_balancer("HNO2+O2=HNO3"))

    def test_277(self):
        """Run test case 277."""

        self.assertTrue(test_balancer("Cu+O2+CO2+H2O=Cu2(OH)2CO3"))

    def test_278(self):
        """Run test case 278."""

        self.assertTrue(test_balancer("HNO2+NO2=HNO3+NO"))

    def test_279(self):
        """Run test case 279."""

        self.assertTrue(test_balancer("HNO2+HI=NO+I2+H2O"))

    def test_280(self):
        """Run test case 280."""

        self.assertTrue(test_balancer("HNO2+H2SO4=NOHSO4+H2O"))

    def test_281(self):
        """Run test case 281."""

        self.assertTrue(test_balancer("NOHSO4+H2O=H2SO4+HNO2"))

    def test_282(self):
        """Run test case 282."""

        self.assertTrue(test_balancer("HNO2+HNO3=NO2+H2O"))

    def test_283(self):
        """Run test case 283."""

        self.assertTrue(test_balancer("HNO2+CS(NH2)2=HSCN+N2+H2O"))

    def test_284(self):
        """Run test case 284."""

        self.assertTrue(test_balancer("HNO2+CS(NH2)2=NHCNSH2+NO+H2O"))

    def test_285(self):
        """Run test case 285."""

        self.assertTrue(test_balancer("HNO2+C6H4NH2SO3H.HC2H3O2=C6H4N2SO3H.C2H3O2+H2O"))

    def test_286(self):
        """Run test case 286."""

        self.assertTrue(test_balancer("NO2<e->+S<2e->+H<e+>=NO+H2O+S"))

    def test_287(self):
        """Run test case 287."""

        self.assertTrue(test_balancer("NO2<e->+Al+OH<e->+H2O=Al(OH)4<e->+NH3"))

    def test_288(self):
        """Run test case 288."""

        self.assertTrue(test_balancer("BaSO3+HNO3=BaSO4+NO+H2O"))

    def test_289(self):
        """Run test case 289."""

        self.assertTrue(test_balancer("SO3<2e->+NO2<e->+H<e+>=SO4<2e->+NO+H2O"))

    def test_290(self):
        """Run test case 290."""

        self.assertTrue(test_balancer("MnO4<e->+NO2<e->+H<e+>=Mn<2e+>+NO3<e->+H2O"))

    def test_291(self):
        """Run test case 291."""

        self.assertTrue(test_balancer("ClO3<e->+NO2<e->=Cl<e->+NO3<e->"))

    def test_292(self):
        """Run test case 292."""

        self.assertTrue(test_balancer("KNO2=K2O+NO+O2"))

    def test_293(self):
        """Run test case 293."""

        self.assertTrue(test_balancer("NH4NO2=H2O+N2"))

    def test_294(self):
        """Run test case 294."""

        self.assertTrue(test_balancer("HNO2+H2SO4+Hg=Hg2SO4+NO+H2O"))

    def test_295(self):
        """Run test case 295."""

        self.assertTrue(test_balancer("K4Fe(CN)6+HNO2+CH3COOH=K3Fe(CN)6+CH3COOK+NO+H2O"))

    def test_296(self):
        """Run test case 296."""

        self.assertTrue(test_balancer("FeCl3+KNO2+H2O=FeO(OH)+KCl+HNO3+NO"))

    def test_297(self):
        """Run test case 297."""

        self.assertTrue(test_balancer("(N2H4)2.H2SO4+KNO2=N2+K2SO4+KOH+H2O"))

    def test_298(self):
        """Run test case 298."""

        self.assertTrue(test_balancer("N2H4.H2SO4+AgNO2=AgN3+H2SO4+H2O"))

    def test_299(self):
        """Run test case 299."""

        self.assertTrue(test_balancer("C2H2+KMnO4+H2SO4=K2SO4+MnSO4+HCOOH+H2O"))

    def test_300(self):
        """Run test case 300."""

        self.assertTrue(test_balancer("HNO3=NO2+O2+H2O"))

    def test_301(self):
        """Run test case 301."""

        self.assertTrue(test_balancer("HNO3+(H)=NH3+H2O"))

    def test_302(self):
        """Run test case 302."""

        self.assertTrue(test_balancer("HNO3+F2=FNO3+HF"))

    def test_303(self):
        """Run test case 303."""

        self.assertTrue(test_balancer("HNO3+H2O2=NO4+H2O"))

    def test_304(self):
        """Run test case 304."""

        self.assertTrue(test_balancer("HNO3+H2O2=HNO4+H2O"))

    def test_305(self):
        """Run test case 305."""

        self.assertTrue(test_balancer("HNO3+HOC6H4SO3H=HOC6H2(NO2)2SO3H+H2O"))

    def test_306(self):
        """Run test case 306."""

        self.assertTrue(test_balancer("HOC6H2(NO2)2SO3H+NH4OH=HOC6H2(NO2)2SO3NH4+H2O"))

    def test_307(self):
        """Run test case 307."""

        self.assertTrue(test_balancer("HNO3+C20H16N4=C20H16N4.HNO3"))

    def test_308(self):
        """Run test case 308."""

        self.assertTrue(test_balancer("H2N2O2=N2O+H2O"))

    def test_309(self):
        """Run test case 309."""

        self.assertTrue(test_balancer("H2N2O2+NH2OH=N2+H2O"))

    def test_310(self):
        """Run test case 310."""

        self.assertTrue(test_balancer("K2Cr2O7+Fe3O4+H2SO4=K2SO4+Fe2(SO4)3+Cr2(SO4)3+H2O"))

    def test_311(self):
        """Run test case 311."""

        self.assertTrue(test_balancer("Ag2O+H2NOH=H2N2O2+Ag+H2O"))

    def test_312(self):
        """Run test case 312."""

        self.assertTrue(test_balancer("Ag2N2O2+HCl=AgCl+H2N2O2"))

    def test_313(self):
        """Run test case 313."""

        self.assertTrue(test_balancer("PO4<3e->+MoO4<2e->+NH4<e+>+H<e+>=(NH4)3(P(Mo12O40)).6H2O+H2O"))

    def test_314(self):
        """Run test case 314."""

        self.assertTrue(test_balancer("CO;HCN;NH3;H2O"))

    def test_315(self):
        """Run test case 315."""

        self.assertTrue(test_balancer("KMnO4;Cl2;MnCl2;HCl;KCl;H2O"))

    def test_316(self):
        """Run test case 316."""

        self.assertTrue(test_balancer("H2;PI3;Na2SiO3;Ca(CN)2;CrCl3;FeSO4;MgSiO3;KI;H3PO4;PbCrO4;BrCl;" +
                                      "MgCO3;KAl(OH)4;Fe(SCN)3;NaAlF4;CF2Cl2;SO2;PbBr2;CaF2;H2O"))

    def test_317(self):
        """Run test case 317."""

        self.assertTrue(test_balancer("Cu<2e+>;Cu;<e->"))

    def test_318(self):
        """Run test case 318."""

        self.assertTrue(test_balancer("NO;N2O3;NO2"))

    def test_319(self):
        """Run test case 319."""

        self.assertTrue(test_balancer("NH4Cl;K2(HgI4);KCl;KI;H2O;Hg2NH2OI;KOH"))

    def test_320(self):
        """Run test case 320."""

        self.assertTrue(test_balancer("NH4NO3;(NH4)2Cr2O7;KNO3;K2Cr2O7"))

    def test_321(self):
        """Run test case 321."""

        self.assertTrue(test_balancer("Zn+HNO3=Zn(NO3)2+N2O+H2O"))

    def test_322(self):
        """Run test case 322."""

        self.assertTrue(test_balancer("((NH4)3(PO4.12MoO3).2H2O);H2O;(NH4)2MoO4;Na2MoO4;NaOH;(NH4)2HPO4"))

    def test_323(self):
        """Run test case 323."""

        self.assertTrue(test_balancer("KO2=K+O2+K2O"))

    def test_324(self):
        """Run test case 324."""

        self.assertTrue(test_balancer("H2S+H2SO4=S+SO2+H2O"))

    def test_325(self):
        """Run test case 325."""

        self.assertTrue(test_balancer("KMnO4+H2O2+H2SO4=K2SO4+MnSO4+H2O+O2"))

    def test_326(self):
        """Run test case 326."""

        self.assertTrue(test_balancer("PbS+O3=PbSO4+O2"))

    def test_327(self):
        """Run test case 327."""

        self.assertTrue(test_balancer("Ba<2e+>+SO4<2e->+H<e+>+OH<e->=BaSO4+H2O"))

    def test_328(self):
        """Run test case 328."""

        self.assertTrue(test_balancer("HClO3=HClO4+Cl2+O2+H2O"))

    def test_329(self):
        """Run test case 329."""

        self.assertTrue(test_balancer("NH3+CH4+O2=HCN+H2O"))

    def test_330(self):
        """Run test case 330."""

        self.assertTrue(test_balancer("F2+Cl2=ClF3"))

    def test_331(self):
        """Run test case 331."""

        self.assertTrue(test_balancer("NH4<e+>+NO2<e->+H<e+>=N2O+NO+H2O"))

    def test_332(self):
        """Run test case 332."""

        self.assertTrue(test_balancer("KClO3+HCl=KCl+H2O+Cl2+ClO2"))

    def test_333(self):
        """Run test case 333."""

        self.assertTrue(test_balancer("P2I4+P4+H2O=PH4I+H3PO4"))

    def test_334(self):
        """Run test case 334."""

        self.assertTrue(test_balancer("Cu+HNO3=Cu(NO3)2+NO2+NO+H2O"))

    def test_335(self):
        """Run test case 335."""

        self.assertTrue(test_balancer("NH4Al(SO4)2.12H2O=SO2+NH3+N2+SO3+Al2O3+H2O"))

    def test_336(self):
        """Run test case 336."""

        self.assertTrue(test_balancer("KI+O3=KIO3+O2"))

    def test_337(self):
        """Run test case 337."""

        self.assertTrue(test_balancer("Fe+HNO3=Fe(NO3)3+Fe(NO3)2+NO2+H2O"))

    def test_338(self):
        """Run test case 338."""

        self.assertTrue(test_balancer("Na+O2=Na2O+Na2O2"))

    def test_339(self):
        """Run test case 339."""

        self.assertTrue(test_balancer("XeO3+H2O2=Xe+O2+H2O"))

    def test_340(self):
        """Run test case 340."""

        self.assertTrue(test_balancer("XeO3+O3+NaOH=Na4XeO6.2H2O+O2"))

    def test_341(self):
        """Run test case 341."""

        self.assertTrue(test_balancer("K2Cr2O7+CH3CH2OH+H2SO4=Cr2(SO4)3+CH3COOH+K2SO4+H2O"))

    def test_342(self):
        """Run test case 342."""

        self.assertTrue(test_balancer("HXeO4<e->+OH<e->=XeO6<4e->+Xe+O2+H2O"))

    def test_343(self):
        """Run test case 343."""

        self.assertTrue(test_balancer("XeF4+H2O=XeO3+Xe+O2+HF"))

    def test_344(self):
        """Run test case 344."""

        self.assertTrue(test_balancer("Co(SCN)2+KSCN=K2(Co(SCN)4)"))

    def test_345(self):
        """Run test case 345."""

        self.assertTrue(test_balancer("CoSO4+BaCO3+HCN=Ba3(Co(CN)6)2+BaSO4+H2SO4+CO2+H2+H2O"))

    def test_346(self):
        """Run test case 346."""

        self.assertTrue(test_balancer("Co(NO3)2+KNO2+CH3COOH=CH3COOK+K3(Co(NO2)6)+KNO3+NO+H2O"))

    def test_347(self):
        """Run test case 347."""

        self.assertTrue(test_balancer("Co(NO3)2+NH4NO3+NH3+O2=Co(NH3)6(NO3)3+H2O"))

    def test_348(self):
        """Run test case 348."""

        self.assertTrue(test_balancer("Co(NO3)2+(NH4)2CO2+NH3+O2=NH4NO3+Co(NH3)4CO3NO3+H2O"))

    def test_349(self):
        """Run test case 349."""

        self.assertTrue(test_balancer("Co(NO3)2+C4O6H6+NH3.H2O=NH4C4O6H5+Co(OH)2+NH4NO3+H2O"))

    def test_350(self):
        """Run test case 350."""

        self.assertTrue(test_balancer("CuS+CN<e->+OH<e->=Cu(CN)4<3e->+NCO<e->+S+S<2e->+H2O"))

    def test_351(self):
        """Run test case 351."""

        self.assertTrue(test_balancer("N2H4+HNO2=NH3+N2O+H2O"))

    def test_352(self):
        """Run test case 352."""

        self.assertTrue(test_balancer("S+KOH=K2S+K2SO3+H2O"))

    def test_353(self):
        """Run test case 353."""

        self.assertTrue(test_balancer("HN3+HNO2=N2O+N2+H2O"))

    def test_354(self):
        """Run test case 354."""

        self.assertTrue(test_balancer("HN3+F2=NH4F+FN3+N2"))

    def test_355(self):
        """Run test case 355."""

        self.assertTrue(test_balancer("HN3+HNO2=N2O+N2+H2O"))

    def test_356(self):
        """Run test case 356."""

        self.assertTrue(test_balancer("NO2+NO+NH3+H2O=NH4NO2"))

    def test_357(self):
        """Run test case 357."""

        self.assertTrue(test_balancer("CH3COONH4+H2O=CH3COOH+NH3+H2O"))

    def test_358(self):
        """Run test case 358."""

        self.assertTrue(test_balancer("NH4ClO4+HNO3+HCl=HClO4+N2O+Cl2+H2O"))

    def test_359(self):
        """Run test case 359."""

        self.assertTrue(test_balancer("(NH4)2SO8+H2SO4+H2O=(NH4)HSO4+HNO3+H2SO4"))

    def test_360(self):
        """Run test case 360."""

        self.assertTrue(test_balancer("(NH4)2CO3+H2O=NH4OH+NH3+CO2+H2O"))

    def test_361(self):
        """Run test case 361."""

        self.assertTrue(test_balancer("NO+O3=NO2+O2"))

    def test_362(self):
        """Run test case 362."""

        self.assertTrue(test_balancer("NO2+O3=N2O5+O2"))

    def test_363(self):
        """Run test case 363."""

        self.assertTrue(test_balancer("AsCl3+H2O=H3AsO3+HCl"))

    def test_364(self):
        """Run test case 364."""

        self.assertTrue(test_balancer("N2O4+O3=NO3+O2"))

    def test_365(self):
        """Run test case 365."""

        self.assertTrue(test_balancer("NO3+H2O=HNO3+HNO2+O2"))

    def test_366(self):
        """Run test case 366."""

        self.assertTrue(test_balancer("C6H12O6+O2+H2O=CO2+H2O"))

    def test_367(self):
        """Run test case 367."""

        self.assertTrue(test_balancer("AsCl3+KMnO4+HCl=MnCl2+KCl+AsOCl3+Cl2+H2O"))

    def test_368(self):
        """Run test case 368."""

        self.assertTrue(test_balancer("XeF4+C2H4=Xe+(CH2F)2+CH3CHF2"))

    def test_369(self):
        """Run test case 369."""

        self.assertTrue(test_balancer("KCNO+NaOH+Cl2=CO2+N2+KCl+NaCl+H2O"))

    def test_370(self):
        """Run test case 370."""

        self.assertTrue(test_balancer("Fe3C+HNO3=Fe(NO3)3+CO2+NO2+H2O"))

    def test_371(self):
        """Run test case 371."""

        self.assertTrue(test_balancer("Ag3AsO4+Zn+H2SO4=Ag+AsH3+ZnSO4+H2O"))

    def test_372(self):
        """Run test case 372."""

        self.assertTrue(test_balancer("Pt+HNO3+HCl=H2PtCl6+NO+H2O"))

    def test_373(self):
        """Run test case 373."""

        self.assertTrue(test_balancer("NaCr(OH)4+NaClO+NaOH=Na2CrO4+NaCl+H2O"))

    def test_374(self):
        """Run test case 374."""

        self.assertTrue(test_balancer("S8+Ca(OH)2=CaS5+CaS2O3+H2O"))

    def test_375(self):
        """Run test case 375."""

        self.assertTrue(test_balancer("Na2S2+NaClO+NaOH=Na2SO4+NaCl+H2O"))

    def test_376(self):
        """Run test case 376."""

        self.assertTrue(test_balancer("F2+I2=IF7"))

    def test_377(self):
        """Run test case 377."""

        self.assertTrue(test_balancer("Na2S3+NaClO+NaOH=Na2SO4+NaCl+H2O"))

    def test_378(self):
        """Run test case 378."""

        self.assertTrue(test_balancer("Na2S4+NaClO+NaOH=Na2SO4+NaCl+H2O"))

    def test_379(self):
        """Run test case 379."""

        self.assertTrue(test_balancer("Na2S5+NaClO+NaOH=Na2SO4+NaCl+H2O"))

    def test_380(self):
        """Run test case 380."""

        self.assertTrue(test_balancer("Na2S6+NaClO+NaOH=Na2SO4+NaCl+H2O"))

    def test_381(self):
        """Run test case 381."""

        self.assertTrue(test_balancer("Cl2+<e->=Cl<e->"))

    def test_382(self):
        """Run test case 382."""

        self.assertTrue(test_balancer("KMnO4+Fe<2e+>+H<e+>=Mn<2e+>+K<e+>+Fe<3e+>+H2O"))

    def test_383(self):
        """Run test case 383."""

        self.assertTrue(test_balancer("KMnO4+KNO2+H2SO4=MnSO4+K2SO4+KNO3+H2O"))

    def test_384(self):
        """Run test case 384."""

        self.assertTrue(test_balancer("NH3+CH4+O2+NaOH=NaCN+H2O"))

    def test_385(self):
        """Run test case 385."""

        self.assertTrue(test_balancer("CH2OH(CHOH)4CHO+Ag(NH3)2OH=Ag+NH3+CH2OH(CHOH)4COONH4+H2O"))

    def test_386(self):
        """Run test case 386."""

        self.assertTrue(test_balancer("Al2(SO4)3+NH3.H2O=Al(OH)3+(NH4)2SO4"))

    def test_387(self):
        """Run test case 387."""

        self.assertTrue(test_balancer("Cl2+P=PCl3"))

    def test_388(self):
        """Run test case 388."""

        self.assertTrue(test_balancer("NO2+NO+NaOH=NaNO2+H2O"))

    def test_389(self):
        """Run test case 389."""

        self.assertTrue(test_balancer("Kr+F2=KrF2"))

    def test_390(self):
        """Run test case 390."""

        self.assertTrue(test_balancer("KrF2=Kr+F2"))

    def test_391(self):
        """Run test case 391."""

        self.assertTrue(test_balancer("Xe+PtF6=Xe<e+>+PtF6<e->"))

    def test_392(self):
        """Run test case 392."""

        self.assertTrue(test_balancer("XeO3+H<e+>+Cl<e->=Xe+H2O+Cl2"))

    def test_393(self):
        """Run test case 393."""

        self.assertTrue(test_balancer("XeO3+H<e+>+I<e->=Xe+H2O+I3<e->"))

    def test_394(self):
        """Run test case 394."""

        self.assertTrue(test_balancer("XeO3+NH3=Xe+N2+H2O"))

    def test_395(self):
        """Run test case 395."""

        self.assertTrue(test_balancer("XeO3+H2O+Fe<2e+>=Xe+Fe<3e+>+OH<e->"))

    def test_396(self):
        """Run test case 396."""

        self.assertTrue(test_balancer("XeO3+H2O+Mn<2e+>=Xe+MnO2+H<e+>"))

    def test_397(self):
        """Run test case 397."""

        self.assertTrue(test_balancer("XeO3+OH<e->=HXeO4<e->"))

    def test_398(self):
        """Run test case 398."""

        self.assertTrue(test_balancer("C2H5OH+O2=CO2+H2O"))

    def test_399(self):
        """Run test case 399."""

        self.assertTrue(test_balancer("XeOF4+H2O=XeO2F2+HF"))

    def test_400(self):
        """Run test case 400."""

        self.assertTrue(test_balancer("XeO2F2+H2O=XeO3+HF"))

    def test_401(self):
        """Run test case 401."""

        self.assertTrue(test_balancer("XeOF4+H2=Xe+H2O+HF"))

    def test_402(self):
        """Run test case 402."""

        self.assertTrue(test_balancer("XeO4=Xe+O2"))

    def test_403(self):
        """Run test case 403."""

        self.assertTrue(test_balancer("Na4XeO6+H2O=Na<e+>+OH<e->+HXeO6<3e->"))

    def test_404(self):
        """Run test case 404."""

        self.assertTrue(test_balancer("HXeO6<3e->+Mn<2e+>+H<e+>=MnO4<e->+XeO3+H2O"))

    def test_405(self):
        """Run test case 405."""

        self.assertTrue(test_balancer("Na4XeO6+Mn(OH)2+H2O=NaHXeO4+NaMnO4+NaOH"))

    def test_406(self):
        """Run test case 406."""

        self.assertTrue(test_balancer("XePtF6+H2O=Xe+PtO2+HF+O2"))

    def test_407(self):
        """Run test case 407."""

        self.assertTrue(test_balancer("XeF2+SbF5=XeF<e+>+SbF6<e->"))

    def test_408(self):
        """Run test case 408."""

        self.assertTrue(test_balancer("XeF2+H2O=Xe+O2+HF"))

    def test_409(self):
        """Run test case 409."""

        self.assertTrue(test_balancer("HgO=Hg+O2"))

    def test_410(self):
        """Run test case 410."""

        self.assertTrue(test_balancer("XeF2+OH<e->=Xe+O2+F<e->+H2O"))

    def test_411(self):
        """Run test case 411."""

        self.assertTrue(test_balancer("XeF2+H2O+NaBrO3=NaBrO4+HF+Xe"))

    def test_412(self):
        """Run test case 412."""

        self.assertTrue(test_balancer("XeF2+AsF5=Xe2F3<e+>+AsF6<e->"))

    def test_413(self):
        """Run test case 413."""

        self.assertTrue(test_balancer("XeF2+H2O2=Xe+O2+HF"))

    def test_414(self):
        """Run test case 414."""

        self.assertTrue(test_balancer("Cr<3e+>+H2O+XeF2=Xe+CrO4<2e->+H<e+>+HF"))

    def test_415(self):
        """Run test case 415."""

        self.assertTrue(test_balancer("XeF4+Hg=Xe+HgF2"))

    def test_416(self):
        """Run test case 416."""

        self.assertTrue(test_balancer("XeF4+Pt=Xe+PtF4"))

    def test_417(self):
        """Run test case 417."""

        self.assertTrue(test_balancer("XeF4+CF3CFCF2=CF3CF2CF3+Xe"))

    def test_418(self):
        """Run test case 418."""

        self.assertTrue(test_balancer("XeF6+H2O=XeO3+HF"))

    def test_419(self):
        """Run test case 419."""

        self.assertTrue(test_balancer("XeF6+H2O=XeOF4+HF"))

    def test_420(self):
        """Run test case 420."""

        self.assertTrue(test_balancer("H2O2=H2O+O2"))

    def test_421(self):
        """Run test case 421."""

        self.assertTrue(test_balancer("XeF6+SiO2=XeO3+SiF4"))

    def test_422(self):
        """Run test case 422."""

        self.assertTrue(test_balancer("XeF6+CsF=Cs(XeF7)"))

    def test_423(self):
        """Run test case 423."""

        self.assertTrue(test_balancer("XeF6+CsF=Cs2(XeF8)"))

    def test_424(self):
        """Run test case 424."""

        self.assertTrue(test_balancer("XeF6+PtF5=XeF5<e+>+PtF6<e->"))

    def test_425(self):
        """Run test case 425."""

        self.assertTrue(test_balancer("Co(CN)2+KCN+H2O=K3(Co(CN)6)+KOH+H2"))

    def test_426(self):
        """Run test case 426."""

        self.assertTrue(test_balancer("Co(CN)2+CN<e->=Co(CN)6<4e->"))

    def test_427(self):
        """Run test case 427."""

        self.assertTrue(test_balancer("Co(SCN)2+KNH2=Co(NH2)2+KSCN"))

    def test_428(self):
        """Run test case 428."""

        self.assertTrue(test_balancer("Co(SCN)2+AgSCN+H2O=CoAg(SCN)3.2H2O"))

    def test_429(self):
        """Run test case 429."""

        self.assertTrue(test_balancer("Co(IO3)2+NH3=Co(IO3)2.6NH3"))

    def test_430(self):
        """Run test case 430."""

        self.assertTrue(test_balancer("Co(IO3)2.6NH3+NO=Co(IO3)2.NO.5NH3+NH3"))

    def test_431(self):
        """Run test case 431."""

        self.assertTrue(test_balancer("CO2+H2O=O2+C6H12O6"))

    def test_432(self):
        """Run test case 432."""

        self.assertTrue(test_balancer("[Ph]OH+O2=CO2+H2O"))
