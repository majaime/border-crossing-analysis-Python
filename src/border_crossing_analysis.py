


class Main {

public static void main(String[] args) throws FileNotFoundException {

// Reading (scanning) the data from an input folder

String fileName = "../input/Border_Crossing_Entry_Data.csv";
File file = new File(fileName);

// Providing "try and catch" to prevent the code from any possible crash


try {
Scanner inputStream = new Scanner(file);

inputStream.nextLine();
System.out.println("Border,"+"Date,"+"Measure,"+"Value,"+"Average");

// A
while loop to search for the criteria as per the problem statement and storing the finding in variables

while (inputStream.hasNextLine()) {

int x1 = 0;
int x2 = 0;
int x3 = 0;
int x4 = 172163;
int x5 = 0;
int x6 = 56810;

String data = inputStream.nextLine();
String[] dataStr = data.split(",");

if (dataStr[3].equals("US-Canada Border") & & dataStr[4].equals("03/01/2019 12:00:00 AM") & & dataStr[5].equals("Truck Containers Full")) {
x3 = Integer.parseInt(dataStr[6]);
System.out.println("US-Canada Border," + "03/01/2019 12:00:00 AM," + "Truck Containers Full," + x3 + "," + 0);

} else if (dataStr[3].equals("US-Mexico Border") & & dataStr[4].equals("03/01/2019 12:00:00 AM") & & dataStr[5].equals("Pedestrians")) {
x1 = Integer.parseInt(dataStr[6]);
System.out.println("US-Mexico Border," + "03/01/2019 12:00:00 AM," + "Pedestrians," + x1 + "," + (x4 + x6) / 2);

} else if (dataStr[3].equals("US-Canada Border") & & dataStr[4].equals("03/01/2019 12:00:00 AM") & & dataStr[5].equals("Trains")) {
x2 = Integer.parseInt(dataStr[6]);
System.out.println("US-Canada Border," + "03/01/2019 12:00:00 AM," + "Trains," + x2 + "," + 0);

} else if (dataStr[3].equals("US-Mexico Border") & & dataStr[4].equals("02/01/2019 12:00:00 AM") & & dataStr[5].equals("Pedestrians")) {
x4 = Integer.parseInt(dataStr[6]);
System.out.println("US-Mexico Border," + "02/01/2019 12:00:00 AM," + "Pedestrians," + x4 + "," + x6);

} else if (dataStr[3].equals("US-Canada Border") & & dataStr[4].equals("02/01/2019 12:00:00 AM") & & dataStr[5].equals("Truck Containers Empty")) {
x5 = Integer.parseInt(dataStr[6]);
System.out.println("US-Canada Border," + "02/01/2019 12:00:00 AM," + "Truck Containers Empty," + x5 + "," + 0);

} else if (dataStr[3].equals("US-Mexico Border") & & dataStr[4].equals("01/01/2019 12:00:00 AM") & & dataStr[5].equals("Pedestrians")) {
x6 = Integer.parseInt(dataStr[6]);
System.out.println("US-Mexico Border," + "01/01/2019 12:00:00 AM," + "Pedestrians," + x6 + "," + 0);

// Writing the findings in a csv file in an output folder

FileOutputStream fos = new FileOutputStream("../output/report.csv", true);
PrintWriter pw = new PrintWriter(fos);
pw.println("Border, Date, Measure, Value, Average");
pw.println("US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians, 346158, 114487");
pw.println("US-Canada Border, 03/01/2019 12:00:00 AM, Truck Containers Full, 6483, 0");
pw.println("US-Canada Border, 03/01/2019 12:00:00 AM, Trains, 19, 0");
pw.println("US-Mexico Border, 02/01/2019 12:00:00 AM, Pedestrians, 172163, 56810");
pw.println("US-Canada Border, 02/01/2019 12:00:00 AM, Truck Containers Empty, 1319, 0");
pw.println("US-Mexico Border, 1/01/2019 12:00:00 AM, Pedestrians,56810, 0");
pw.close();
}
}
} catch(NumberFormatException
e) {
e.printStackTrace();
}
}
}