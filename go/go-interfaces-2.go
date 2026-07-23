package main

import (
    "fmt"
 )

 type player interface {
     kickBall() float64
 }

 type soccerPlayer struct {
     name string
     team string
     power float64
 }

 func (s soccerPlayer) kickBall() float64 {
     return s.power * 2
 }
  

 func main() {
     messi := soccerPlayer{name: "Lionel Messi", team: "Barca", power: 7.5}
    
     fmt.Printf("Messi kics %v", messi.kickBall())
 }

