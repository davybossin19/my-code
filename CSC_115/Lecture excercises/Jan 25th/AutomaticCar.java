public class AutomaticCar implements Vehicle {
	private String model;
	private int distanceTraveled;
	private boolean seatbeltsOn;

	public AutomaticCar(String model, int distanceTraveled){
		this.model = model;
		this.distanceTraveled = distanceTraveled;
		seatbeltsOn = false;
	}

	// What is missing?

	public void drive(int distance) {
		if (safetyCheck()) {
			System.out.println("driving " + distance + " kms");
			this.distanceTraveled += distance;
		} else {
			System.out.println("Not safe to drive");
		}
	}

	public boolean safetyCheck() {
		if (seatbeltsOn) {
			return true;
		} else {
			return false;
		}
	}

	public int getKMs() {
		return distanceTraveled;
	}

	public void fastenSeatBelts() {
		seatbeltsOn = true;
	}

}
