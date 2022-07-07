
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from sympy.geometry import *

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from convert_bezier_to_linear_approximate_curve import *
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testGetEquallyDividedPointsBetween2Points(self):
        point_a = Point(0.0, 0.0)
        point_b = Point(10.0, 10.0)
        division_num = 10

        points = getEquallyDividedPointsBetween2Points(point_a, point_b, division_num)

        answer = []
        for i in range(division_num):
            answer.append( [float(i), float(i)] )
        #end for
        answer.append( [10.0, 10.0] )

        for i, point in enumerate(points):
            self.assertEqual(point.x, answer[i][0])
            self.assertEqual(point.y, answer[i][1])
            #print( "{}, {}, {}".format(i, point.x, point.y) )
        #end for

    #end def testGetEquallyDividedPointsBetween2Points

    def testGetInternalDivisionPoint(self):
        point_a = Point(1.0, 1.0)
        point_b = Point(10.0, 10.0)

        point = getInternalDivisionPoint(point_a, point_b, 1.0, 2.0)

        answer = [4.0, 4.0]
        self.assertEqual(point.x, answer[0])
        self.assertEqual(point.y, answer[1])
        #print( "{}, {}".format(point.x, point.y) )

    #end def testGetInternalDivisionPoint

    def testConvertBezierToLinearApproximateCurve(self):
        cubic_bezier_curve = readCubicBezierCurveFromSvgFile("data/aaa.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 1.0)

        the_answers = ( (624.369000000000,665.275000000000) ,
                        (624.312736421553,665.176507288630) ,
                        (624.149095454055,664.884935860058) ,
                        (623.885801749271,664.406145772595) ,
                        (623.530579958968,663.745997084548) ,
                        (623.091154734910,662.910349854227) ,
                        (622.575250728863,661.905064139942) ,
                        (621.990592592593,660.736000000000) ,
                        (621.344904977864,659.409017492711) ,
                        (620.645912536443,657.929976676385) ,
                        (619.901339920095,656.304737609329) ,
                        (619.118911780585,654.539160349854) ,
                        (618.306352769679,652.639104956268) ,
                        (617.471387539143,650.610431486880) ,
                        (616.621740740741,648.459000000000) ,
                        (615.765137026239,646.190670553936) ,
                        (614.909301047403,643.811303206997) ,
                        (614.061957455998,641.326758017493) ,
                        (613.230830903790,638.742895043732) ,
                        (612.423646042544,636.065574344023) ,
                        (611.648127524026,633.300655976676) ,
                        (610.912000000000,630.454000000000) ,
                        (610.210207105064,627.626223841918) ,
                        (609.532922146637,624.915736313573) ,
                        (608.881142857143,622.324655976676) ,
                        (608.255866969010,619.855101392938) ,
                        (607.658092214664,617.509191124069) ,
                        (607.088816326531,615.289043731778) ,
                        (606.549037037037,613.196777777778) ,
                        (606.039752078609,611.234511823777) ,
                        (605.561959183674,609.404364431487) ,
                        (605.116656084656,607.708454162617) ,
                        (604.704840513983,606.148899578879) ,
                        (604.327510204082,604.727819241983) ,
                        (603.985662887377,603.447331713638) ,
                        (603.680296296296,602.309555555556) ,
                        (603.412408163265,601.316609329446) ,
                        (603.182996220710,600.470611597020) ,
                        (602.993058201058,599.773680919987) ,
                        (602.843591836735,599.227935860058) ,
                        (602.735594860166,598.835494978944) ,
                        (602.670065003779,598.598476838354) ,
                        (602.648000000000,598.519000000000) ,
                        (601.997954732510,596.169139917696) ,
                        (601.547193415638,594.539674897119) ,
                        (601.238777777778,593.424777777778) ,
                        (601.015769547325,592.618621399177) ,
                        (600.821230452675,591.915378600823) ,
                        (600.598222222222,591.109222222222) ,
                        (600.289806584362,589.994325102881) ,
                        (599.839045267490,588.364860082305) ,
                        (625.695000000000,667.640000000000) ,
                        (625.342771146883,667.169631351951) ,
                        (624.983009283009,666.637310893188) ,
                        (624.616049503541,666.044996072573) ,
                        (624.242226903641,665.394644338964) ,
                        (623.861876578473,664.688213141219) ,
                        (623.475333623199,663.927659928198) ,
                        (623.082933132983,663.114942148760) ,
                        (622.685010202987,662.252017251765) ,
                        (622.281899928373,661.340842686071) ,
                        (621.873937404306,660.383375900537) ,
                        (621.461457725948,659.381574344023) ,
                        (621.044795988461,658.337395465388) ,
                        (620.624287287009,657.252796713491) ,
                        (620.200266716754,656.129735537190) ,
                        (619.773069372860,654.970169385346) ,
                        (619.343030350490,653.776055706816) ,
                        (618.910484744805,652.549351950461) ,
                        (618.475767650969,651.292015565140) ,
                        (618.039214164146,650.006003999711) ,
                        (617.601159379497,648.693274703033) ,
                        (617.161938392186,647.355785123967) ,
                        (616.721886297376,645.995492711370) ,
                        (616.281338190229,644.614354914103) ,
                        (615.840629165909,643.214329181023) ,
                        (615.400094319578,641.797372960991) ,
                        (614.960068746399,640.365443702865) ,
                        (614.520887541536,638.920498855504) ,
                        (614.082885800150,637.464495867769) ,
                        (613.646398617406,635.999392188516) ,
                        (613.211761088465,634.527145266607) ,
                        (612.779308308490,633.049712550900) ,
                        (612.349375372646,631.569051490254) ,
                        (611.922297376093,630.087119533528) ,
                        (611.498409413996,628.605874129581) ,
                        (611.078046581518,627.127272727273) ,
                        (610.661543973820,625.653272775462) ,
                        (610.249236686067,624.185831723008) ,
                        (609.841459813420,622.726907018770) ,
                        (609.438548451043,621.278456111606) ,
                        (609.040837694099,619.842436450377) ,
                        (608.648662637750,618.420805483941) ,
                        (608.262358377160,617.015520661157) ,
                        (607.882260007491,615.628539430885) ,
                        (607.508702623907,614.261819241982) ,
                        (607.142021321569,612.917317543310) ,
                        (606.782551195642,611.596991783726) ,
                        (606.430627341288,610.302799412091) ,
                        (606.086584853669,609.036697877262) ,
                        (605.750758827949,607.800644628099) ,
                        (605.423484359291,606.596597113462) ,
                        (605.105096542857,605.426512782209) ,
                        (604.795930473810,604.292349083199) ,
                        (604.496321247314,603.196063465292) ,
                        (604.206603958531,602.139613377346) ,
                        (603.927113702624,601.124956268222) ,
                        (603.658185574756,600.154049586777) ,
                        (603.400154670089,599.228850781871) ,
                        (603.153356083788,598.351317302364) ,
                        (602.918124911014,597.523406597114) ,
                        (602.694796246931,596.747076114980) ,
                        (602.483705186701,596.024283304821) ,
                        (602.285186825487,595.356985615498) ,
                        (602.099576258452,594.747140495868) ,
                        (601.927208580760,594.196705394791) ,
                        (601.768418887572,593.707637761126) ,
                        (601.623542274053,593.281895043732) ,
                        (601.492913835363,592.921434691468) ,
                        (601.376868666668,592.628214153194) ,
                        (601.275741863129,592.404190877768) ,
                        (601.189868519910,592.251322314050) ,
                        (601.119583732173,592.171565910898) ,
                        (601.065222595081,592.166879117172) ,
                        (601.027120203797,592.239219381731) ,
                        (601.005611653484,592.390544153435) ,
                        (601.001032039305,592.622810881141) ,
                        (601.013716456423,592.937977013710) ,
                        (601.044000000000,593.338000000000) ,
                        (600.928714820177,592.953924345009) ,
                        (600.833387982906,592.654642525294) ,
                        (600.757682671351,592.438182648352) ,
                        (600.701262068678,592.302572821680) ,
                        (600.663789358053,592.245841152775) ,
                        (600.644927722640,592.266015749135) ,
                        (600.644340345605,592.361124718257) ,
                        (600.661690410113,592.529196167637) ,
                        (600.696641099329,592.768258204774) ,
                        (600.748855596419,593.076338937163) ,
                        (600.817997084548,593.451466472303) ,
                        (600.903728746881,593.891668917690) ,
                        (601.005713766584,594.394974380822) ,
                        (601.123615326822,594.959410969196) ,
                        (601.257096610760,595.583006790309) ,
                        (601.405820801563,596.263789951657) ,
                        (601.569451082397,596.999788560739) ,
                        (601.747650636427,597.789030725052) ,
                        (601.940082646818,598.629544552091) ,
                        (602.146410296737,599.519358149356) ,
                        (602.366296769346,600.456499624343) ,
                        (602.599405247813,601.438997084548) ,
                        (602.845398915303,602.464878637470) ,
                        (603.103940954980,603.532172390605) ,
                        (603.374694550011,604.638906451450) ,
                        (603.657322883559,605.783108927504) ,
                        (603.951489138792,606.962807926262) ,
                        (604.256856498873,608.176031555222) ,
                        (604.573088146969,609.420807921881) ,
                        (604.899847266244,610.695165133736) ,
                        (605.236797039864,611.997131298285) ,
                        (605.583600650993,613.324734523025) ,
                        (605.939921282799,614.676002915452) ,
                        (606.305422118445,616.048964583064) ,
                        (606.679766341097,617.441647633358) ,
                        (607.062617133920,618.852080173832) ,
                        (607.453637680080,620.278290311982) ,
                        (607.852491162742,621.718306155305) ,
                        (608.258840765071,623.170155811300) ,
                        (608.672349670232,624.631867387462) ,
                        (609.092681061391,626.101468991289) ,
                        (609.519498121713,627.576988730278) ,
                        (609.952464034363,629.056454711927) ,
                        (610.391241982507,630.537895043732) ,
                        (610.835495149310,632.019337833191) ,
                        (611.284886717937,633.498811187800) ,
                        (611.739079871554,634.974343215058) ,
                        (612.197737793325,636.443962022460) ,
                        (612.660523666416,637.905695717506) ,
                        (613.127100673993,639.357572407690) ,
                        (613.597131999220,640.797620200511) ,
                        (614.070280825263,642.223867203466) ,
                        (614.546210335288,643.634341524052) ,
                        (615.024583712459,645.027071269766) ,
                        (615.505064139942,646.400084548105) ,
                        (615.987314800902,647.751409466566) ,
                        (616.470998878504,649.079074132648) ,
                        (616.955779555914,650.381106653845) ,
                        (617.441320016297,651.655535137657) ,
                        (617.927283442818,652.900387691580) ,
                        (618.413333018643,654.113692423110) ,
                        (618.899131926936,655.293477439747) ,
                        (619.384343350864,656.437770848986) ,
                        (619.868630473591,657.544600758324) ,
                        (620.351656478283,658.611995275259) ,
                        (620.833084548105,659.637982507289) ,
                        (621.312577866222,660.620590561909) ,
                        (621.789799615800,661.557847546618) ,
                        (622.264412980004,662.447781568912) ,
                        (622.736081141999,663.288420736288) ,
                        (623.204467284950,664.077793156245) ,
                        (623.669234592023,664.813926936278) ,
                        (624.130046246383,665.494850183886) ,
                        (624.586565431195,666.118591006565) ,
                        (625.038455329626,666.683177511812) ,
                        (625.485379124839,667.186637807124) ,
                        (625.927000000000,667.627000000000) ,
                        (625.006874415638,664.844228576132) ,
                        (624.119620510288,662.178150090535) ,
                        (623.264822555556,659.626918222222) ,
                        (622.442064823045,657.188686650206) ,
                        (621.650931584362,654.861609053498) ,
                        (620.891007111111,652.643839111111) ,
                        (620.161875674897,650.533530502057) ,
                        (619.463121547325,648.528836905350) ,
                        (618.794329000000,646.627912000000) ,
                        (618.155082304527,644.828909465021) ,
                        (617.544965732510,643.129982979424) ,
                        (616.963563555556,641.529286222222) ,
                        (616.410460045267,640.024972872428) ,
                        (615.885239473251,638.615196609053) ,
                        (615.387486111111,637.298111111111) ,
                        (614.916784230453,636.071870057613) ,
                        (614.472718102881,634.934627127572) ,
                        (614.054872000000,633.884536000000) ,
                        (613.662830193416,632.919750353909) ,
                        (613.296176954733,632.038423868313) ,
                        (612.954496555555,631.238710222222) ,
                        (612.637373267490,630.518763094650) ,
                        (612.344391362140,629.876736164609) ,
                        (612.075135111111,629.310783111111) ,
                        (611.829188786008,628.819057613169) ,
                        (611.606136658436,628.399713349794) ,
                        (611.405563000000,628.050904000000) ,
                        (611.227052082305,627.770783242798) ,
                        (611.070188176955,627.557504757202) ,
                        (610.934555555556,627.409222222222) ,
                        (610.819738489712,627.324089316872) ,
                        (610.725321251029,627.300259720165) ,
                        (610.650888111111,627.335887111111) ,
                        (610.596023341564,627.429125168724) ,
                        (610.560311213992,627.578127572016) ,
                        (610.543336000000,627.781048000000) ,
                        (610.544681971193,628.036040131687) ,
                        (610.563933399177,628.341257646091) ,
                        (610.600674555555,628.694854222222) ,
                        (610.654489711934,629.094983539095) ,
                        (610.724963139918,629.539799275720) ,
                        (610.811679111111,630.027455111111) ,
                        (610.914221897119,630.556104724280) ,
                        (611.032175769547,631.123901794239) ,
                        (611.165125000000,631.729000000000) ,
                        (611.312653860082,632.369553020576) ,
                        (611.474346621399,633.043714534979) ,
                        (611.649787555556,633.749638222222) ,
                        (611.838560934156,634.485477761317) ,
                        (612.040251028807,635.249386831276) ,
                        (612.254442111111,636.039519111111) ,
                        (612.480718452675,636.854028279835) ,
                        (612.718664325103,637.691068016461) ,
                        (612.967864000000,638.548792000000) ,
                        (613.227901748971,639.425353909465) ,
                        (613.498361843621,640.318907423868) ,
                        (613.778828555556,641.227606222222) ,
                        (614.068886156379,642.149603983539) ,
                        (614.368118917695,643.083054386831) ,
                        (614.676111111111,644.026111111111) ,
                        (614.992447008231,644.976927835391) ,
                        (615.316710880659,645.933658238683) ,
                        (615.648487000000,646.894456000000) ,
                        (615.987359637860,647.857474798354) ,
                        (616.332913065844,648.820868312757) ,
                        (616.684731555555,649.782790222222) ,
                        (617.042399378601,650.741394205761) ,
                        (617.405500806584,651.694833942387) ,
                        (617.773620111111,652.641263111111) ,
                        (618.146341563786,653.578835390947) ,
                        (618.523249436214,654.505704460905) ,
                        (618.903928000000,655.420024000000) ,
                        (619.287961526749,656.319947687243) ,
                        (619.674934288066,657.203629201646) ,
                        (620.064430555556,658.069222222222) ,
                        (620.456034600823,658.914880427983) ,
                        (620.849330695473,659.738757497942) ,
                        (621.243903111111,660.539007111111) ,
                        (621.639336119342,661.313782946502) ,
                        (622.035213991770,662.061238683128) ,
                        (622.431121000000,662.779528000000) ,
                        (622.826641415638,663.466804576132) ,
                        (623.221359510288,664.121222090535) ,
                        (623.614859555555,664.740934222222) ,
                        (624.006725823045,665.324094650206) ,
                        (624.396542584362,665.868857053498) ,
                        (624.783894111111,666.373375111111) ,
                        (625.168364674897,666.835802502058) ,
                        (625.549538547325,667.254292905350) )


#        s = ""
        i:int = 0
        for layer_name, curve_set_in_a_layer in linear_approximate_curve:
            for curve in curve_set_in_a_layer:
                for point in curve:
#                    s += "(" + str( point.x) + "," + str(point.y) + ")\n"
                    self.assertAlmostEqual(point.x, the_answers[i][0])
                    self.assertAlmostEqual(point.y, the_answers[i][1])
                    i += 1
                #end for
            #end for
        #end for
#        print(s)
    #end def

#end

#end class

if __name__ == '__main__':
    unittest.main()
#end
