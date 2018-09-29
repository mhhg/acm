package gorutine

import (
	"fmt"
	"time"
)

var messages chan string

func ping() {
	for {
		t := time.Now().Unix()
		if t%5 == 0 {
			messages <- fmt.Sprintf("%v, %d", "ping", time.Now().Unix())
		}
	}
}

func pong() {

	for {
		t := time.Now().Unix()
		if t%7 == 0 {
			messages <- fmt.Sprintf("%v, %d", "hey pong", time.Now().Unix())
		}
	}
}

func main() {
	messages = make(chan string)
	go ping()
	go pong()

	for {
		msg := <-messages
		fmt.Println(msg)
		time.Sleep(1 * time.Second)
	}
}
