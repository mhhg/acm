// Max intersection points of line with chart

// There's a line chart consisting of N points (numbered from 0 to N-1) connected by line segments.
// The K-th point has coordinates x= k, y = Y[k]. There're no horizontal lines; that is, no two consecutive points has the same y-coordinate.

// We can draw an infinitely long horizontal line. What is the maximum number of points of intersection of the line with the chart?

// 1. Given Y = [1, 2, 1, 2, 1, 3, 2], expected 5.
// 2. Given Y = [2, 1, 2, 1, 2, 3, 2, 3, 2], expected 5.
// 3. Given Y = [1000001, 1000000, 1000002, 1000001], expected 3.

use itertools::Itertools;

fn max_intersections(input: &Box<[i32]>) -> i32 {
    let mut max = 0;
    for y in input.iter().unique() {
        let mut bottom_intersections_count = 0;
        let mut middle_intersections_count = 0;

        // println!("y: {:?}", y);
        for (x, chart_current_y) in input.iter().enumerate() {
            let intersect_bottom = y == chart_current_y;
            let mut intersect_middle = false;
            if x > 0 {
                let chart_prev_y = &input[x - 1];
                let grow = chart_prev_y < chart_current_y;
                let decline = chart_prev_y > chart_current_y;

                intersect_middle = (grow && chart_current_y > y && chart_prev_y <= y)
                    || (decline && chart_current_y <= y && chart_prev_y > y);
            }

            if intersect_bottom {
                bottom_intersections_count += 1;
            }
            if intersect_middle {
                middle_intersections_count += 1;
            }

            // println!(
            //     "\t ({}, {}) :: p_y: {} - c_y: {} :: b: {:5?} m: {:?}",
            //     x, y, chart_prev_y, chart_current_y, intersect_bottom, intersect_middle,
            // );
        }

        let more = match middle_intersections_count > bottom_intersections_count {
            true => middle_intersections_count,
            false => bottom_intersections_count,
        };
        if more > max {
            max = more;
        }
        // println!(
        //     "=> bottom_count: {:?}, middle_count: {:?}",
        //     bottom_intersections_count, middle_intersections_count
        // );
    }
    println!("input: {:?}\n => max: {}", input, max);
    max
}

#[cfg(test)]
mod tests {
    #[test]
    fn case_1() {
        let input: Box<[i32]> = Box::new([1, 2, 1, 2, 1, 3, 2]);
        let expected = 5;
        let output = super::max_intersections(&input);
        assert_eq!(
            expected, output,
            "\nExpected: {:?}\nFound: {:?}",
            expected, output
        );
    }

    #[test]
    fn case_2() {
        let input: Box<[i32]> = Box::new([2, 1, 2, 1, 2, 3, 2, 3, 2]);
        let expected = 5;
        let output = super::max_intersections(&input);
        assert_eq!(
            expected, output,
            "\nExpected: {:?}\nFound: {:?}",
            expected, output
        );
    }

    #[test]
    fn case_3() {
        let input: Box<[i32]> = Box::new([100001, 1000000, 100002, 1000001]);
        let expected = 3;
        let output = super::max_intersections(&input);
        assert_eq!(
            expected, output,
            "\nExpected: {:?}\nFound: {:?}",
            expected, output
        );
    }
}
