package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"runtime/debug"

	"gopkg.in/mgo.v2"
)

var mongodbSession *mgo.Session

const DATABASE = "sample"
const MongoDBURL = "localhost:27017"

type User struct {
	Username string `json:"username"`
}

type ResponseMessage struct {
	Name    string `json:"name"`
	Message string `json:"message"`
}

func parseRequestBody(req *http.Request) []byte {
	if body, err := ioutil.ReadAll(req.Body); err != nil {
		panic(err)
	} else {
		return body
	}
}

func setResponseJSON(w http.ResponseWriter, body interface{}) {
	if response, err := json.Marshal(body); err != nil {
		panic(err)
	} else {
		w.Header().Set("Content-Type", "application/json")
		fmt.Fprint(w, string(response))
	}
}

func setupHelloRoute() {
	http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "POST" {
			u := User{
				Username: "Mohammad Haghighat",
			}
			setResponseJSON(w, u)
		} else if r.Method == "GET" {
			fmt.Fprintf(w, "hello world")
		} else {
			fmt.Fprintf(w, "method not allowed")
		}
	})
}

func setupWorldRoute() {
	http.HandleFunc("/world", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "POST" {
			u := User{}
			if err := json.Unmarshal(parseRequestBody(r), &u); err != nil {
				panic(err)
			}
			if u.Username == "mhg" {
				setResponseJSON(w, ResponseMessage{
					Name:    "Success",
					Message: "Hello Mohammad",
				})
			} else {
				fmt.Fprintf(w, "unknown user")
			}
		} else {
			fmt.Fprintf(w, "method not allowed")
		}
	})
}

func setupHandlers() {
	setupHelloRoute()
	setupWorldRoute()
}

func setupDatabaseConnection() {
	session, err := mgo.Dial(MongoDBURL)
	if err != nil {
		panic(err)
	}
	mongodbSession = session
}

func recoverRuntimeErrors() {
	if e := recover(); e != nil {
		log.Printf("[runtime error %q, stack trace is bellow] %v",
			e, debug.Stack())
	}
}

func main() {
	setupDatabaseConnection()
	setupHandlers()
	recoverRuntimeErrors()

	fmt.Println(calculate([][]int{
		[]int{15, 100, -1},
		[]int{51, 41, 3},
		[]int{1, 31, 12},
	}))
	http.ListenAndServe("localhost:8080", nil)
}

func calculate(grid [][]int) []int {
	result := []int{}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			num := grid[i][j]
			var isMin bool = true
			for k := 0; k < len(grid); k++ {
				if num > grid[k][j] {
					isMin = false
					break
				}
			}
			if !isMin {
				continue
			}
			isMin = true
			for k := 0; k < len(grid[i]); k++ {
				if num < grid[i][k] {
					isMin = false
					break
				}
			}
			if !isMin {
				continue
			}
			result = append(result, num)
		}
	}
	return result
}
