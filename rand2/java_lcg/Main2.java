import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        ArrayList<Integer> outputs = new ArrayList<Integer>();
        ArrayList<Integer> values = new ArrayList<Integer>();

        StringBuilder givenString = new StringBuilder();
        for(int i=0;i<20;i++){
            givenString.append(Integer.valueOf(random.nextInt(1 << 4)).toString() + " ");
        }

        for(int i=0;i<100;i++){
            values.add(random.nextInt());
        }


        System.out.println("given: "+ givenString.toString());
        System.out.println("next: " + values.toString());

    }
}

/*
output:
given: 0 11 4 7 12 3 3 8 4 7 8 0 9 2 9 7 2 8 5 8 
next: [641418050, -1087572138, 62233483, -2100288371, 1071103109, 1338977141, 194585680, -822882717, 581358163, 354955777, -1370624564, -2051426107, 785903985, -490497732, -1341603391, -1391368270, -1743720472, 1922437884, -1488699025, -165311121, 526382345, 1126225494, -2054604998, 1865426259, -300589647, -268638056, 1194843786, 821356511, -777969458, -1189248643, -1463597582, -1805226991, 4421665, -2041053541, -750899309, -798258695, -719793851, 1521687071, 640357314, 1895813772, 67455727, 1961253053, 2138515944, 1900228791, -1820048778, 328065761, -1365075030, -1095104585, 665105814, 992361770, -1953085879, -29334873, -1899791248, -450456552, -2033602998, -666367654, 169910228, -1849192701, 1835141465, 857902698, -92450877, 1819270734, -1558347158, 1150659217, -1346093521, -1667303203, -1150542816, -1995867849, 1654022660, 1036106947, 1162466674, -1954190773, 1672636011, 115599168, -796658549, 665451861, 1607289420, 1391237098, -649225230, 186816972, 181859349, -633122007, -291107349, -940828508, 1947057594, -1700907033, 1129660956, -1451109589, -923779844, -1466868600, -26627726, -1379120363, 139250668, -1283291368, 1231846469, -859193387, 2091029938, 253998275, -433107271, 10110253]

*/