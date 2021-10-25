//David Bossin
//V00906664


public class MazeRunner {
	Maze mazeToSolve;
	A5Stack<MazeLocation> path;
	FilePrinter fileWriter;

	public MazeRunner(Maze aMaze) {
		mazeToSolve = aMaze;
		path = new A5Stack<MazeLocation>();
		fileWriter = new FilePrinter();
	}

	/*
	 * Purpose: Determines whether there is a path from start to finish in this maze
	 * Parameters: MazeLocation start - starting coordinates of this maze
	 *			   MazeLocation finish - finish coordinates of this maze
	 * Returns: true if there is a path from start to finish
	 */
	public boolean solve(MazeLocation start, MazeLocation finish) {
		fileWriter.println("Searching maze from start: "+start+" to finish: "+finish);
		path.push(start);
		return findPath(start, finish);
	}

	/*
	 * Purpose: Recursively determines if there is a path from cur to finish
	 * Parameters: MazeLocation cur - current cordinates in this maze
	 *			   MazeLocation finish - goal coordinates of this maze
	 * Returns: true if there is a path from cur to finish
	 *
	 * NOTE: This method updates the Maze's mazeData array when locations
	 *       are visited to an 'o', and further updates locations to an 'x'
	 *       if it is determined they lead to dead ends. If the finish
	 *       location is found, the Stack named path should contain all of
	 *       loations visited from the start location to the finish.
	 */
	private boolean findPath(MazeLocation cur, MazeLocation finish) {
		int row = cur.getRow();
		int col = cur.getCol();
		mazeToSolve.setChar(row, col, 'o');
		fileWriter.println("\n"+mazeToSolve.toString());

		if (!path.top().equals(cur)) {
			path.push(cur);
		}

		if (path.top().equals(finish)) {
			return true;
		}

		// Checking if space bellow cur is open
		else if (row < mazeToSolve.getRows() - 1 && mazeToSolve.getChar(row + 1,col) == ' ') {
			cur = new MazeLocation(row + 1, col);
			return findPath(cur, finish);
		}

		// Checking if space right of cur is open
		else if (col < mazeToSolve.getCols() - 1 && mazeToSolve.getChar(row, col + 1) == ' ') {
			cur = new MazeLocation(row, col + 1);
			return findPath(cur, finish);
		}

		// Checking if space left of cur is open
		else if (col > 0 && mazeToSolve.getChar(row, col - 1) == ' ') {
			cur = new MazeLocation(row, col - 1);
			return findPath(cur, finish);
		}


		// Checking if space above cur is open
		else if (row > 0 && mazeToSolve.getChar(row - 1, col) == ' ') {
			cur = new MazeLocation(row - 1, col);
			return findPath(cur, finish);
		}

		//condition for dead end
		else {
			mazeToSolve.setChar(row, col, 'x');
			path.pop();
			// If path is empty at this point we know there is no solution
			if (path.isEmpty()) {
				return false;
			}
			cur = path.top();
			return findPath(cur, finish);
		}
	}


	/*
	 * Purpose: Creates a string of maze locations found in the stack
	 * Parameters: None
	 * Returns: A String representation of maze locations
	 */
	public String getPathToSolution() {
		String details = "";
		while(!path.isEmpty()) {
			details = path.pop() + "\n" + details;
		}
		return details;
	}

	/*
	 * Purpose: Print the results of the maze run. Outputs the locations
	 *          visited on the path from start to finish if the maze is
	 *          solvable, or that no path was found if it is not.
	 * Parameters: boolean - whether or not the maze was solved
	 * Returns void - nothing
	 */
	public void printResults(boolean solved) {
		if (solved) {
			fileWriter.println("\n*** Maze Solved ***");
			fileWriter.println(getPathToSolution());
		} else {
			fileWriter.println("\n--- No path to solution found ---");
		}
		fileWriter.close();
	}
}
