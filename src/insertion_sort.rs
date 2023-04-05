fn insertion_sort(input: &Box<[i32]>) -> Box<[i32]> {
    let mut output: Box<[i32]> = input.to_vec().into_boxed_slice();

    for i in 0..output.len() {
        if i == 0 {
            continue;
        }

        if output[i] < output[i - 1] {
            let tmp = output[i - 1];
            output[i - 1] = output[i];
            output[i] = tmp;

            let mut j = i - 1;
            while j > 0 {
                let tmp = output[j - 1];
                println!("while loop: {:?}, {:?}", j, tmp);
                output[j - 1] = output[j];
                output[j] = tmp;
                j = j - 1;
            }
        }
    }

    return output;
}

fn main() {
    // let boxed_array: Box<[i32]> = Box::new([4, 2, 6, 3]);
    // println!("insertion_sort");
    // println!("input: {:?}", boxed_array);
    // println!("output: {:?}", insertion_sort(boxed_array));
}

#[cfg(test)]
mod tests {
    #[test]
    fn insertion_sort_test() {
        let input: Box<[i32]> = Box::new([3, 1, 2, 8, 5]);
        let expected: Box<[i32]> = Box::new([1, 2, 3, 5, 8]);
        let output: Box<[i32]> = super::insertion_sort(&input);
        assert_eq!(
            expected[..],
            output[..],
            "\nExpected\n{:?}\nfound\n{:?}",
            &expected[..],
            &output[..]
        );
    }
}
